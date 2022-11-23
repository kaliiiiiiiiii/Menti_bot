import time

# sel_profiles import
from sel_profiles.utils.utils import read_json
from sel_profiles.driver import driver as mydriver

# import menti
from menti import menti

# default profile for sel_profiles
profile = read_json(filename="profiles\\default.json")
profile = profile["Windows"]  # yet supported: "Android", "Windows"
# profile["browser"]["headless"] = True

# start driver
mydriver = mydriver()
driver = mydriver.start(profile)

# init Menti
menti = menti('8867 2568', driver)  # change pin here!

# loop 10 times
for x in range(10):
    # menti.scales([1, 20])  # scale 1 = 15, scale 2 = 10
    time.sleep(0.2)
    menti.multiple_choice(1)  # choose nr. 2 of choices
    menti.submit_reload()  # submit and reload page

# menti.word_cloud("myword")  # write "myword" into cloud field
# menti.looper() # for not yet implemented methods

driver.quit()  # don't forget to stop the driver!
