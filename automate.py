import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from PIL import Image
from bs4 import BeautifulSoup
import base64


class ChromeBrowser(webdriver.Chrome):
    def __init__(self, user_data_dir=f"{os.path.abspath(os.getcwd())}\\Chrome\\userdata"):
        """

        :type user_data_dir: it should be Absolute path. if user will pass relative path it won't work.
        """
        options = webdriver.ChromeOptions()

        # setting up dir to keep saving browser data, in case if user login his/her account it won't log out.
        options.add_argument(f"user-data-dir={user_data_dir}")

        # Here Calling Constructor of Chrome Class and passing options argument that will help to set Data dir.
        super().__init__(options=options)

    def open_url(self, url):
        self.get(url)

    def get_list_of_tabs(self):
        return self.window_handles

    def switch_to_tab(self, tab):
        self.switch_to.window(tab)

    def close_all_tabs(self):
        active_window = self.current_window_handle
        for handle in self.window_handles:
            if handle != active_window:
                self.switch_to.window(handle)
                self.close()


class WhatsApp:
    def __init__(self):
        self.XPATH_MESSAGE_BOX = "//div[@id='main']/footer/div[1]/div[1]/span[2]/div[1]/div[2]/div[1]/div[1]/div[2]"
        self.XPATH_SEND_BUTTON = "//div[@id='main']/footer/div[1]/div[1]/span[2]/div[1]/div[2]/div[2]/button"
        self.XPATH_CHAT_LIST = "//div[@aria-label='Chat list']"

        # Xpath for media attachment.
        self.XPATH_ATTACH_BUTTON = "//span[@data-icon='clip']"
        self.XPATH_ATTACH_PHOTOS_VIDEO_INPUT_FIELD = "//button[@aria-label='Photos & Videos']/input"
        self.XPATH_ATTACH_STICKER_INPUT_FIELD = "//button[@aria-label='Sticker']/input"
        self.XPATH_ATTACH_CAMERA_INPUT_FIELD = "//button[@aria-label='Camera']/input"
        self.XPATH_ATTACH_DOCUMENT_INPUT_FIELD = "//button[@aria-label='Document']/input"
        self.XPATH_ATTACH_CONTACT_INPUT_FIELD = "//button[@aria-label='Contact']/input"
        self.XPATH_ATTACH_SEND_BUTTON = "//div[@role='button'][@aria-label='Send']"

        # XPATH's for Login screen (Loading window)
        self.XPATH_QR_CODE = "//canvas[@aria-label='Scan me!']"
        self.XPATH_RELOAD_QR = "//div[@class='landing-window']/div[1]/div[1]/div[2]/div[1]/span[1]/button"

        # XPATH's to extract data from active chat contact element.
        self.XPATH_ACTIVE_CONTACT_ELEMENT_NAME = "div[1]//span[@dir='auto']"
        self.XPATH_ACTIVE_CONTACT_ELEMENT_IMAGE = "div[1]/div[1]/div[1]/div[1]/div[1]/img"

        # Dir for whatsAPP data and files.
        self.WHATSAPP_DATA_DIR = 'WhatsApp Data'
        self.TEMP_DIR = os.path.join(self.WHATSAPP_DATA_DIR, 'temp')
        self.PROFILE_PICTURES_DIR = os.path.join(self.WHATSAPP_DATA_DIR, "profiles")
        self.create_dirs()

        # opening Google Chrome.
        self.Browser = ChromeBrowser()

        # opening WhatsApp web website.
        self.Browser.get('http://web.whatsapp.com')

        # Active chats list
        self.active_chat_list = None

    def restart(self):
        pass

    def is_running(self):
        pass

    def clear_chat(self, users, options=None):
        pass

    def mute_notifications(self, users, options=None):
        pass

    def delete_chat(self, users, options=None):
        pass

    def create_dirs(self):
        try:
            os.makedirs(self.TEMP_DIR)
            os.makedirs(self.PROFILE_PICTURES_DIR)
        except FileExistsError:
            pass

    def get_active_chat_list(self):
        """
        :return: it will return list all active chats.
        Structure of that list will be like :
        [ {'name': name_of_user, 'image': profile_picture_url, 'element': web_element}, {....}, {...}]
        """
        active_chats_list = []

        # Here extracting the container that will be containing list of all active chats
        try:
            chat_list = self.Browser.find_element(by=By.XPATH, value=self.XPATH_CHAT_LIST)
        except NoSuchElementException:
            print("Log: There is No Active Chats")
            return None

        count = 1
        while True:
            # Here extracting the contact element. one by one
            try:
                contact_element = chat_list.find_element(by=By.XPATH, value=f'div[{count}]')
                count += 1
            except NoSuchElementException:
                break

            # Here extracting name of the user.
            try:
                name = contact_element.find_element(By.XPATH, self.XPATH_ACTIVE_CONTACT_ELEMENT_NAME).\
                    get_attribute('title')
            except NoSuchElementException:
                name = None

            # Here extracting the url of profile picture.
            try:
                avtar = contact_element.find_element(by=By.XPATH, value=self.XPATH_ACTIVE_CONTACT_ELEMENT_IMAGE)
                avtar = avtar.get_attribute('src')
            except NoSuchElementException:
                avtar = None

            # Here creating dict for each and every contact.
            contact = {'name': name, 'image': avtar, 'element': contact_element}
            active_chats_list.append(contact)

        if len(active_chats_list) > 0:
            self.active_chat_list = active_chats_list
            return active_chats_list
        return None

    def click_on_user_profile(self, user_name):
        # First checking that if self.active_chat_lis is None then call get_active_chat_list
        if self.active_chat_list is None:
            if self.get_active_chat_list() is None:
                print("Log: There is not active chats")
                return False

        # Here clicking on user to open chat area.
        for contact in self.active_chat_list:
            if contact['name'] == user_name:
                contact['element'].click()
                break
        else:
            print("Invalid User Name, Please Check")
            return False
        return True

    def send_msg(self, user_name, _message):
        # Here clicking on user to open chat area.
        if not self.click_on_user_profile(user_name):
            return False

        # Here assigning the message in message box.
        try:
            message_box = self.Browser.find_element(by=By.XPATH, value=self.XPATH_MESSAGE_BOX)
            message_box.send_keys(_message)

        except NoSuchElementException:
            print("Log: Unable to locate message box")
            return False

        # Here, Let's click on send button.
        try:
            self.Browser.find_element(by=By.XPATH, value=self.XPATH_SEND_BUTTON).click()
        except NoSuchElementException:
            print("Log: Unable to find the send button")
            return False

        return True

    def send_file(self, user_name, files):
        # Here let's first click on user profile.
        if not self.click_on_user_profile(user_name):
            return False

        # Here let's click on attach button
        try:
            self.Browser.find_element(by=By.XPATH, value=self.XPATH_ATTACH_BUTTON).click()
        except NoSuchElementException:
            print("Log: Unable to locate attach button")
            return False

        try:
            # Finding the document input field
            document_input_field = self.Browser.find_element(by=By.XPATH, value=self.XPATH_ATTACH_DOCUMENT_INPUT_FIELD)
        except NoSuchElementException:
            print("Log: Unable to Locate Document Input Field")
            return False

        # Here attaching files using send_keys() method.
        try:
            if type(files) == list:

                # in case there is more than one file that's why used for loop.
                for _file in files:
                    document_input_field.send_keys(_file)
            else:
                document_input_field.send_keys(files)
        except InvalidArgumentException:
            print("Log: Invalid file")
            return False

        # Now click on send Button.
        """
        After you will attach all file, some time it may take to some time to make send button visible.
        that's it's better to use sleep function to wait for 1sec
        """
        time.sleep(1)
        try:
            self.Browser.find_element(by=By.XPATH, value=self.XPATH_ATTACH_SEND_BUTTON).click()
        except NoSuchElementException:
            print("Log: Unable to Locate send button")
            return False

        return True

    def save_all_profile_pictures(self):
        # Here first get list of all active chat.
        if self.active_chat_list is None:
            self.get_active_chat_list()

        # here let's download all images one by one.
        for chat_header in self.active_chat_list:
            # if there is no profile picture for give contact than continue to next contact.
            if chat_header['image'] is None:
                continue

            image_src = chat_header['image']
            result = self.Browser.execute_async_script("""
                                    var uri = arguments[0];
                                    var callback = arguments[1];
                                    var toBase64 = function(buffer){for(var r,n=new Uint8Array(buffer),t=n.length,a=new Uint8Array(4*Math.ceil(t/3)),i=new Uint8Array(64),o=0,c=0;64>c;++c)i[c]="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".charCodeAt(c);for(c=0;t-t%3>c;c+=3,o+=4)r=n[c]<<16|n[c+1]<<8|n[c+2],a[o]=i[r>>18],a[o+1]=i[r>>12&63],a[o+2]=i[r>>6&63],a[o+3]=i[63&r];return t%3===1?(r=n[t-1],a[o]=i[r>>2],a[o+1]=i[r<<4&63],a[o+2]=61,a[o+3]=61):t%3===2&&(r=(n[t-2]<<8)+n[t-1],a[o]=i[r>>10],a[o+1]=i[r>>4&63],a[o+2]=i[r<<2&63],a[o+3]=61),new TextDecoder("ascii").decode(a)};
                                    var xhr = new XMLHttpRequest();
                                    xhr.responseType = 'arraybuffer';
                                    xhr.onload = function(){ callback(toBase64(xhr.response)) };
                                    xhr.onerror = function(){ callback(xhr.status) };
                                    xhr.open('GET', uri);
                                    xhr.send();
                                    """, image_src)
            if type(result) == int:
                print(f"Log: Request failed with status {result}")
                continue

            # converting image to base64.
            final_image = base64.b64decode(result)

            # Here let's save the image

            image_file_path = os.path.join(self.PROFILE_PICTURES_DIR, chat_header['name']+'.jpg')
            with open(image_file_path, 'wb') as f:
                f.write(final_image)

            # Here let's set image path in active chat list. and remove url.
            chat_header['image'] = image_file_path

    def get_qr_code(self):
        """
        Note: at every 20sec cycle qr code will get update.
        :return: qr code path.
        """
        # Here let's check status of qr code, is there any need to reload qr or not.
        try:
            # let's locate the reload button on page
            reload_button = self.Browser.find_element(by=By.XPATH, value=self.XPATH_RELOAD_QR)
            reload_button.click()
        except NoSuchElementException:
            pass

        # Here let's check if qr code is still loading.
        reload_button_bool = False
        qr_code_bool = False
        try:
            # if it's not able to find qr code that's mean it's not there.
            self.Browser.find_element(by=By.XPATH, value=self.XPATH_QR_CODE)
        except NoSuchElementException:
            qr_code_bool = True

        try:
            # if it's not able to find reload button that's mean it's not there.
            self.Browser.find_element(by=By.XPATH, value=self.XPATH_RELOAD_QR)
        except NoSuchElementException:
            reload_button_bool = True

        # if both of element( reload button and qr_code) that's mean it's loading the qr code.
        if reload_button_bool and qr_code_bool:
            return None

        """
        Here let's extract the qr code from web page.
        1. will take screenshot of whole page
        2. then it will find the position and height and width of qr code
        3. with the help of PIL library, will crop qr code from screenshot.
        4. Done.
        """
        # creating path of screen_shot file.
        screenshot = os.path.join(self.TEMP_DIR, "screenshot.png")
        try:
            os.remove(screenshot)
        except FileNotFoundError:
            pass

        # First taking Screen Shot of whole page.
        self.Browser.save_screenshot(screenshot)

        # Here locating Qr code.
        try:
            qr_code = self.Browser.find_element(by=By.XPATH, value=self.XPATH_QR_CODE)
        except NoSuchElementException:
            print("Log: Unable to locate qr code")
            return None

        # Here extracting information about size and potion of qr code on page.
        qr_location = qr_code.location
        qr_size = qr_code.size

        padding = 5
        x = qr_location['x'] - padding
        y = qr_location['y'] - padding
        width = x + qr_size['width'] + (padding * 2)
        height = y + qr_size['height'] + (padding * 2)

        # making path to save qr code
        qr_code_image = os.path.join(self.TEMP_DIR, 'qr_code.png')
        try:
            # in case file is not there it will be able to handle error otherwise will remove the previous file.
            os.remove(qr_code_image)
        except FileNotFoundError:
            pass

        # Here let's crop qr code from screenshot.
        try:
            im = Image.open(screenshot)
            im = im.crop((int(x), int(y), int(width), int(height)))
            im.save(qr_code_image)
        except:
            print("Log: Unable to crop qr code from screenshot.")
            return None

        return qr_code_image

    def test(self):
        element = self.Browser.find_element(by=By.XPATH, value="//span[.='Most popular']")
        element = self.Browser.execute_script("return arguments[0].scrollIntoView();", element)
        print(element)

    def close(self):
        self.Browser.close()


if __name__ == '__main__':

    whats_app = WhatsApp()

    while True:
        print("---------------------- Menu -----------------------")
        print("1. Get List of active chats")
        print("2. Search Element by XPath")
        print("3. Send Message")
        print("5. Save Qr Code")
        print("6. Send File")
        print("7. Page Source")
        print("8. Save Image")
        print("4. Exit")
        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            for chat in whats_app.get_active_chat_list():
                print(chat['name'])

        elif choice == 2:
            x_path = input("Enter XPath : ")
            element = whats_app.Browser.find_element_by_xpath(x_path)
            print(element)

        elif choice == 3:
            user = input("Enter the Name of user to whom you want to send message: ")
            message = input("Enter the message that you want to send: ")
            print(whats_app.send_msg(user, message))

        elif choice == 4:
            break

        elif choice == 5:
            print(whats_app.get_qr_code())

        elif choice == 6:
            name = input("Enter the user name: ")
            file = input("Enter the file Name: ")
            print(whats_app.send_file(name, file))

        elif choice == 7:
            htmlcode = (whats_app.Browser.page_source).encode('utf-8')
            print(htmlcode)
            soup = BeautifulSoup(htmlcode, features="html.parser")
            print(soup)

        elif choice == 8:
            whats_app.save_all_profile_pictures()


    whats_app.close()
