# system imports
import time
import traceback
import warnings

from win32api import GetKeyState  # for "press x to reload"

# selenium imports
from selenium.webdriver.common.by import By  # locate elements
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


# Menti class
# noinspection PyPep8Naming,PyShadowingNames
class menti(object):
    def __init__(self, pin, driver):
        self.pin = str(pin).replace(' ', '')
        self.driver = driver
        self.url = self.get_url()
        self.looper()

    # get url based on PIN
    def get_url(self):
        self.driver.get("https://www.menti.com/")
        self.driver.find_element(By.XPATH, '//*[@id="enter-vote-key"]').send_keys(self.pin + "\n")
        time.sleep(4)
        return self.driver.current_url

    # noinspection PyBroadException
    def looper(self):
        while True:
            self.driver.get(self.url)
            # noinspection GrazieInspection
            while True:  # wait for manual choose..
                if self.key_down(0x58):  # x pressed ==> submit, clear cookies and reload page
                    break
                if self.key_down(0x51):  # "q" pressed ==> quit
                    self.driver.quit()
                    raise ValueError('"q" pressed.. quitting!')
                time.sleep(0.02)
            try:
                self.sendkeys(Keys.ENTER)
            except:
                warnings.warn("ENTER key could not be pressed!")
                traceback.print_exc()
            self.driver.delete_all_cookies()  # might not be implemented in other drivers than Sel-Profiles?

    # detect key_down with pywin32
    # noinspection PyMethodMayBeStatic
    def key_down(self, key):
        state = GetKeyState(key)
        if (state != 0) and (state != 1):
            return True
        else:
            return False

    # send_keys to driver without specific element
    def sendkeys(self, keys):  # send keys without specific Element
        actions = ActionChains(self.driver)
        actions.send_keys(str(keys))
        actions.perform()
