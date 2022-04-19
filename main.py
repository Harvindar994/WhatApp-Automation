from automate import *
from interface import *
from PyQt5.QtWidgets import QStackedWidget, QApplication
from PyQt5.QtGui import QIcon
from threading import Thread
import sys


"""
Here creating Ui handler for every window. these handlers is Inherited from interface class.
to provide facility to change and edit the user interface with PyQt Designer without changing anything
in the main code.
"""


class MainWindow(UiMainWindow):  # Ui Handler
    def __init__(self):
        super(MainWindow, self).__init__()
        self.connect_buttons()

    def connect_buttons(self):
        """
        Here connecting buttons with there Appropriate functions.
        :return: None
        """
        pass


class LoginWindow(UiLoginWindow):  # Ui Handler
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.connect_buttons()

    def set_qr_code(self, qr_code):
        """
        :param qr_code: it is the path of qr_code image.
        :return: None
        """
        self.label_qr_code.setPixmap(QtGui.QPixmap(qr_code))

    def connect_buttons(self):
        """
        Here connecting buttons with there Appropriate functions.
        :return: None
        """
        pass


class LoadingWindow(UiLoadingWindow):  # Ui Handler
    def __init__(self):
        super(LoadingWindow, self).__init__()
        self.connect_buttons()

    def set_percentage(self, value):
        """
        :param value: it is a int type value percentage of progress bar.
        :return: None
        """
        self.progressBar.setValue(value)

    def connect_buttons(self):
        """
        Here connecting buttons with there Appropriate functions.
        :return: None
        """
        pass


class Windows(QStackedWidget):
    """
    This is help to make stack of window and switching between the.
    it's like switching pages in web browser.
    Example: if you have added three windows in stack.
    [win_1, win_2, win_2]
    you can use switch_window_by_index(index) to switch between windows.
    """
    def __init__(self, application):
        super(Windows, self).__init__()
        # Here setting up main_window that will the self class
        self.setWindowTitle("Brightgoal")
        self.setWindowIcon(QIcon("Interface Assets/Brightgoal logo.png"))
        self.app = application

        # Creating all the window
        self.LoginWindow = LoginWindow()
        self.addWidget(self.LoginWindow)
        self.MainWindow = MainWindow()
        self.addWidget(self.MainWindow)

    def current_win_name(self):
        return self.currentWidget().objectName()

    def current_win_index(self):
        return self.currentIndex()

    def switch_window_by_index(self, index):
        self.setCurrentIndex(index)

    def switch_window_by_name(self, window_name):
        for win_index in range(0, self.count()):
            if window_name == self.widget(win_index).objectName():
                self.setCurrentIndex(win_index)
                return True

        return False

    @staticmethod
    def set_pixmap(element, image):
        element.setPixmap(QtGui.QPixmap(image))


class Task:
    SEND_MESSAGE = 'send_message'

    def __init__(self, whatsapp, windows, task_name, data):
        """
        the task class will be containing all the information and data about the task that needs to be done.
        like if your wants to send the message, then task will be Containing that message data, and all the contact to
        whom user wants to send the message.
        :param whatsapp: it will be the WhatsApp class object.
        :param windows: Windows class object that will be managing all the windows.
        :param task_name: str - "send_message"
        :param data: dict - {contact: [contact_1, contact_2, ...], 'message': msg_string}
        """
        self.whatsApp = whatsapp
        self.windows = windows
        self.name = task_name
        self.data = data
        self.completed = False
        self.running = False
        self.interrupted = False

    def interrupt(self):
        pass

    def execute(self):
        pass


class Application(QApplication):
    def __init__(self, argv=sys.argv):
        super(Application, self).__init__(argv)

        # Here create stack that will be containing all the windows or pages.
        self.windows = Windows(self)
        self.windows.show()

        # Here creating the loading window.
        self.loading_window = LoadingWindow()
        self.loading_window.show()

        # Here setting up closing button
        self.aboutToQuit.connect(self.close)

        # Here Creating WhatsApp Class That will be Responsible for all the automation work.
        self.whatsApp = WhatsApp()

        # Here starting thread for start function that keep background activities uptodate.
        self.backgroundThreadStatus = True
        self.backgroundThread = Thread(target=self.start)
        self.backgroundThread.start()

        # Here creating the task list. That will be containing all the task needs to be done.
        self.Tasks = []

    def close(self):
        # Here first closing the background thread.
        self.backgroundThreadStatus = False

        # Here closing whatsapp also the chrome driver.
        self.whatsApp.close()

        # let's close the application.
        self.quit()

    def create_task(self, task):
        pass

    def login(self):
        while True:
            # here extracting qr code from webpage. using get_qr_code() that is inside the WhatsApp class.
            qr_code = self.whatsApp.get_qr_code()

            # if get_qr_code() will return None that's mean there is no qr code. and we won't change the qr_code Image.
            if qr_code is not None:

                # Here setting up the new qr code image on login window.
                self.windows.set_pixmap(self.windows.LoginWindow.label_qr_code, qr_code)

            """
            Here checking the current web page opened in google chrome.
            on the basic of webpage we will decide user is logged in or not.
            in this case if the current web page is main whatsapp page where you can send and receive
            messages that's mean user is logged in. and we should close the login window.
            """
            current_window = self.whatsApp.current_window()

            # here if current web page is the main whatsapp page then we will be closing the login window.
            if current_window == self.whatsApp.MAIN_WINDOW:
                break

    def loading_win(self):
        self.loading_window.show()
        self.windows.hide()

    def start(self):
        while self.backgroundThreadStatus:
            current_window = self.whatsApp.current_window()
            if current_window == self.whatsApp.LOADING_WINDOW:
                self.windows.hide()
                self.loading_window.show()

            elif current_window == self.whatsApp.LOGIN_WINDOW:
                self.windows.switch_window_by_name("LoginWindow")
                self.login()

            elif current_window == self.whatsApp.MAIN_WINDOW:
                self.windows.switch_window_by_name('MainWindow')
                for task in self.Tasks:
                    task.execute()


if __name__ == '__main__':
    application = Application(sys.argv)
    sys.exit(application.exec_())






