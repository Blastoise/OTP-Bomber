![OTP-Bomber](https://socialify.git.ci/Blastoise/OTP-Bomber/image?description=1&descriptionEditable=%F0%9F%A7%91%F0%9F%8F%BB%E2%80%8D%F0%9F%92%BB%20%F0%9F%98%88%20%F0%9F%92%AC%20Send%20OTP%27s%20in%20bulk%20to%20annoy%20people.&font=KoHo&forks=1&issues=1&language=1&owner=1&pattern=Circuit%20Board&pulls=1&stargazers=1&theme=Dark)

[![forthebadge](https://forthebadge.com/images/badges/open-source.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/60-percent-of-the-time-works-every-time.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

OTP-Bomber is a simple python script that can be used to send OTP's in bulk to people. It uses the selenium library for browser automation and uses the login/registration process of various websites for sending OTP's. It uses only those websites where user can register/login via OTP, which is the case in most of the websites because nobody wants to lose customers and I utilised that simple fact to create this project.


## Dependencies

- selenium
- urllib3
- Google Chrome Web Broswer(above Chrome version 60)
- Chrome Web Driver

## Setup Instructions

- First download the appropriate Chrome Web Driver using the this [link](https://chromedriver.chromium.org/downloads).
- Install the other two dependencies using the `requirements.txt` present in the root of the project using the following command:

  > pip3 install -r requirements.txt

- Please read the [NOTE](#note) section to know where to specify the location of Chrome Web Driver and for editing other settings.

## Usage

Run the script using the following command (Assuming you are in the root of the project):
> python3 main.py

## NOTE

There are few things that can be modified according to your need.
1. The most important variable that can be modified is the `webdriverLocation` variable that stores the full path of the directory where the Chrome Web Driver is situated. By default it will search for the Web Driver in the root of the project.
2. Another important thing to note is that each of the `Bomber` function takes a parameter called `waitingTime` which is by default set to 2. This parameter describes the number of seconds to wait for the page to be loaded. So you can pass appropriate value according to your internet speed.

## Contributing to OTP-Bomber

Feel free to add new Bomber functions in their respective file inside `services` folder present in the root of the project


## Disclaimer

This is script should be used only for learning purposes.
