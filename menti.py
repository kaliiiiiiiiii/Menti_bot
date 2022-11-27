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
    def __init__(self, pin: str or int, driver):
        self.pin = str(pin).replace(' ', '')
        self.driver = driver
        self.url = self.get_url()

    # get url based on PIN
    def get_url(self):
        self.driver.get("https://www.menti.com/")
        self.driver.find_element(By.XPATH, '//*[@id="enter-vote-key"]').send_keys(self.pin + "\n")
        time.sleep(3)
        return self.driver.current_url

    def word_cloud(self, word: str):
        fields = self.driver.find_elements(By.XPATH, '//*[@name="wordcloud-input"]')
        for field in fields:
            field.send_keys(word)

    def multiple_choice(self, choice: int):
        # noinspection SpellCheckingInspection
        choices = self.driver.find_elements(By.XPATH, '//*[starts-with(@data-testid,"choice")]')
        if choice < 1:
            raise ValueError("Choice needs to be positive!")
        if len(choices) < choice:
            raise ValueError("Can't choose choice "+str(choice)+" , only "+str(len(choices))+" choices available.")
        choices[choice-1].click()

    def scales(self, values: list):
        sliders = self.driver.find_elements(By.XPATH, '//*[starts-with(@name,"scale-input")]')
        if not len(sliders) == len(values):
            raise ValueError("number of sliders must equal number of values!")

        for slider, value in zip(sliders, values):  # for slider

            # get slider values
            mini = float(slider.get_attribute("min"))
            maxi = float(slider.get_attribute("max"))
            step = float(slider.get_attribute("step"))
            start_val = float(slider.get_attribute("value"))

            if (mini > value) or (maxi < value):
                raise ValueError(
                    "Value must be between " + str(mini) + " and " + str(maxi) + " !, got " + str(value) + " instead.")
            if not (value / step).is_integer():
                raise ValueError("Value " + str(value) + " needs to be divisible by steps = " + str(step) + " !")

            if start_val < value:
                for x in range(round(int(((value - start_val) / step)))):
                    time.sleep(0.02)
                    slider.send_keys(Keys.RIGHT)
            elif start_val < value:
                for x in range(round(int(((start_val - value) / step)))):
                    time.sleep(0.02)
                    slider.send_keys(Keys.LEFT)
            else:
                pass

    def submit_reload(self):
        # noinspection PyBroadException
        try:
            self.sendkeys(Keys.ENTER)
        except:
            warnings.warn("ENTER key could not be pressed!")
            traceback.print_exc()
        self.driver.delete_all_cookies()  # might not be implemented in other drivers than Sel-Profiles?
        self.driver.get(self.url)

    # noinspection PyBroadException
    def looper(self):
        while True:
            # noinspection GrazieInspection
            while True:  # wait for manual choose..
                if self.key_down(0x58):  # x pressed ==> submit, clear cookies and reload page
                    break
                if self.key_down(0x51):  # "q" pressed ==> quit
                    self.driver.quit()
                    raise ValueError('"q" pressed.. quitting!')
                time.sleep(0.02)
            self.submit_reload()

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
