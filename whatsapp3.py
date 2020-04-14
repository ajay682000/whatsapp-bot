import time, sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def new_chat(user_name):
    # Change the class path in it is changed in future
    # Clicking the search bar
    new_chat = driver.find_element_by_xpath('//div[@class="gQzdc"]')
    new_chat.click()
    # Change the class path in it is changed in future
    # Enter the name of the user in search bar
    new_user = driver.find_element_by_xpath('//div[@class="_2S1VP copyable-text selectable-text"]')
    new_user.send_keys(user_name)
    time.sleep(1)
    try:
        # Selecting the name of the user after searching
        user = driver.find_element_by_xpath('//span/span[@title="{}"]'.format(user_name))
        user.click()
    except NoSuchElementException as es:
        print('Given user "{}" not found in your contacts!!!'.format(user_name))
    except Exception as e:
        driver.close()
        print(e)
        sys.exit()


if __name__ == '__main__':
    # Initiallizing the driver. I have chrome driver installed
    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com/")
    print("Scan the QR code from your phone")
    time.sleep(15)
    # Getting the names dynamically
    print("Enter the names of the user separted by commas:")
    user_name_list = raw_input()
    name = user_name_list.split(",")
    for names in name:
        print(names)

    
    for user_name in name:
        try:
            # For searching the user in recent chat list
            user = driver.find_element_by_xpath('//span/span[@title="{}"]'.format(user_name))
            user.click()

        except NoSuchElementException as se:
            # If the user is not in recent chat but in contacts
            new_chat(user_name)
        # Clicking the text box and writing the message 
        message_box = driver.find_element_by_xpath('//div[@class="_1Plpp"]')
        message_box.send_keys('Automation message sent for testing. ')
        # Sending the message to the user
        message_box = driver.find_element_by_xpath('//button[@class="_35EW6"]')
        message_box.click()
        time.sleep(1)

    time.sleep(1)
    driver.close()
