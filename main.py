import time

# sel_profiles import
from selenium_profiles.driver import driver as mydriver
from selenium_profiles import profiles

# import menti
from menti import menti

# start driver
mydriver = mydriver()
driver = mydriver.start(profiles.Windows())

# init Menti
menti = menti('3476 0352', driver)  # change pin here!

# loop 10 times
for x in range(-1, 10):
    # menti.scales([1, 20])  # scale 1 = 15, scale 2 = 10
    time.sleep(0.2)
    menti.multiple_choice(2)  # choose nr. 1 of choices
    menti.submit_reload()  # submit and reload page

# menti.word_cloud("myword")  # write "myword" into cloud field
# menti.looper() # for not yet implemented methods

driver.quit()  # don't forget to stop the driver!
