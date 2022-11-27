# Menti_bot V1

* Spoof // Bot for [Mentimeter](https://www.menti.com/) using [Selenium](https://github.com/SeleniumHQ/selenium) library with [chromedriver](https://chromedriver.chromium.org/downloads)

### Feel free to test my code!

## Getting Started

### Dependencies

* [Python>=3.7](https://www.python.org/downloads/)
* Windows 10 (keypress detection doesn't work for Linux yet!)
* Requirements.txt

### Installing

* Install Requirements```pip install -r requirements.txt```

### Usage

#### Set your PIN in main.py at:
```python
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
menti = menti('8867 2568', driver)  # change pin here!

# loop 10 times
for x in range(10):
    # menti.scales([1, 20])  # scale 1 = 15, scale 2 = 10
    time.sleep(0.2)
    menti.multiple_choice(1)  # choose nr. 1 of choices
    menti.submit_reload()  # submit and reload page

# menti.word_cloud("myword")  # write "myword" into cloud field
# menti.looper() # for not yet implemented methods

driver.quit()  # don't forget to stop the driver!


```

###  using ``` menti.looper()```
* Choose your answers
* Press "x" to reload and submit when reaching "Submit" button
* Press "q" to close and exit driver

## Help

Please feel free to open an issue or fork!

## Known Bugs

None yet

## Todo // Features

* [x] clear_cookies
* [x] detect_url based on PIN
* [ ] automation for: 
  * [x] multiple-choice
  * [x] word-cloud
  * [x] scales


## Deprecated

nothing yet

## Authors

[Aurin Aegerter](mailto:aurin.aegerter@stud.gymthun.ch)

## Version History

* Menti_botV1
  * first version as importable file

## License

Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

## Disclaimer

I am not responsible what you use the code for!!! Also no warranty!

## Acknowledgments

Inspiration, code snippets, etc.

* [Selenium-Profiles](https://github.com/kaliiiiiiiiii/Selenium_Profiles)
* [mentimeter.com](https://www.mentimeter.com/)
* [Selenium](https://github.com/SeleniumHQ/selenium)
* [selenium-documentation](https://www.selenium.dev/documentation/)
* [README-Template](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
* [Undetected-Chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver)
