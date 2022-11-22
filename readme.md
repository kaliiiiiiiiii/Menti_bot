# Menti_bot V1

* Spoof // Bot for [Mentimeter](https://www.menti.com/) using [Selenium](https://github.com/SeleniumHQ/selenium) library with [chromedriver](https://chromedriver.chromium.org/downloads)

### Feel free to test my code!

## Getting Started

### Dependencies

* [Python3](https://www.python.org/downloads/)
* Windows 10 (keypress detection doesn't work for Linux yet!)
* [Selenium-Profiles](https://github.com/kaliiiiiiiiii/Selenium-Profiles) ([Undetected-Chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver) and [selenium.webdriver](https://www.selenium.dev/documentation/webdriver/) not tested)
* Requirements.txt

### Installing

* Install Requirements```pip install -r requirements.txt```

### Usage

#### Set your PIN in main.py at:
```python
# init Menti
menti = menti(' 7425 0971', driver)  # change pin here!
```

#### Execute mein.py

* Choose your answers
* Press "x" to reload and submit when reaching "Submit" button
* Press "q" to close and exit driver

## Help

Please feel free to open an issue or fork!
```commandline
# no helper info yet
```

## Known Bugs

None yet

## Todo // Features

* [x] clear_cookies
* [x] detect_url based on PIN
* [ ] automation for selecting; input, slider ..


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

* [Selenium-Profiles](https://github.com/kaliiiiiiiiii/Selenium-Profiles)
* [mentimeter.com](https://www.mentimeter.com/)
* [Selenium](https://github.com/SeleniumHQ/selenium)
* [selenium-documentation](https://www.selenium.dev/documentation/)
* [README-Template](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
* [Undetected-Chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver)
