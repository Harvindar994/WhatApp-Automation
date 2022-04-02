import sys
import time
import os
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
import urllib.request


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

        # opening Google Chrome.
        self.Browser = ChromeBrowser()

        # opening WhatsApp web website.
        self.Browser.get('http://web.whatsapp.com')

        # Active chats list
        self.active_chat_list = None

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

        count = 1
        while True:
            # Here extracting the user element. one by one
            try:
                contact_element = chat_list.find_element(by=By.XPATH, value=f'div[{count}]')
                count += 1
            except NoSuchElementException:
                break

            # Here extracting name of the user.
            try:
                name = contact_element.find_element(by=By.XPATH, value='div[1]/div[1]/div[2]/div[1]/div[1]/span['
                                                                       '1]/span[1]').text
            except NoSuchElementException:
                name = None

            # Here extracting the url of profile picture.
            try:
                avtar = contact_element.find_element(by=By.XPATH, value="div[1]/div[1]/div[1]/div[1]/div[1]/img")
                avtar = avtar.get_attribute('src')
            except NoSuchElementException:
                avtar = None

            # Here creating dict for each and every contact.
            contact = {'name': name, 'image': avtar, 'element': contact_element}
            active_chats_list.append(contact)

        self.active_chat_list = active_chats_list
        return active_chats_list

    def send_msg(self, user, message):
        # First checking that if self.active_chat_lis is None then call get_active_chat_list
        if self.active_chat_list is None:
            self.get_active_chat_list()

        # Here clicking on user to open chat area.
        for contact in self.active_chat_list:
            if contact['name'] == user:
                contact['element'].click()
                break

        # Here assigning the message in message box.
        try:
            message_box = self.Browser.find_element(by=By.XPATH, value=self.XPATH_MESSAGE_BOX)
            message_box.send_keys(message)

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

    def save_image(self, url):
        pass

    def close(self):
        self.Browser.close()


whats_app = WhatsApp()

while True:
    print("---------------------- Menu -----------------------")
    print("1. Get List of active chats")
    print("2. Search Element by XPath")
    print("3. Send Message")
    print("3. Exit")
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

whats_app.close()
