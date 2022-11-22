# sel_profiles import
from sel_profiles.utils.utils import read_json
from sel_profiles.driver import driver as mydriver

# import menti
from menti import menti

# default profile for sel_profiles
profile = read_json(filename="profiles\\default.json")
profile = profile["Windows"]  # yet supported: "Android", "Windows"

# start driver
mydriver = mydriver()
driver = mydriver.start(profile)

# init Menti
menti = menti('7425 0971', driver)  # change pin here!
