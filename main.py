from automate import *
from interface import *
from PyQt5.QtWidgets import QStackedWidget, QApplication
import sys


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
        self.app = application

        # Creating all the window
        self.LoginWindow = LoginWindow()
        self.addWidget(self.LoginWindow)
        self.LoginWindow_2 = LoginWindow()
        self.addWidget(self.LoginWindow_2)

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


class Application(QApplication):
    def __init__(self, argv=sys.argv):
        super(Application, self).__init__(argv)

        self.window = Windows(self)
        self.window.show()

    def start(self):
        pass


if __name__ == '__main__':
    application = Application(sys.argv)
    sys.exit(application.exec_())






