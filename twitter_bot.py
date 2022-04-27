import email
from email import message
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

def account_info():
    with open('account_info.txt', 'r') as f:
        info = f.read().split()
        email = info[0]
        password = info[1]
        #phone = info[2]
    return email, password

email, password = account_info()

tweet = "hii"

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)


driver.get("https://twitter.com/i/flow/login")


email_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input'
next_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div'
#phone_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'
#next2_xpath = '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div'
password_xpath= '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
login_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div'


time.sleep(2)

driver.find_element_by_xpath(email_xpath).send_keys(email)
time.sleep(1)
driver.find_element_by_xpath(next_xpath).click()
time.sleep(1)
# driver.find_element_by_xpath(phone_xpath).send_keys(phone)
# time.sleep(1)
# driver.find_element_by_xpath(next2_xpath).click()
# time.sleep(1)
driver.find_element_by_xpath(password_xpath).send_keys(password)
time.sleep(1)
driver.find_element_by_xpath(login_xpath).click()


tweet_xpath = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a'
# message_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div'
message_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div'
post_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]'
time.sleep(5)

driver.find_element_by_xpath(tweet_xpath).click()
time.sleep(2)
driver.find_element_by_xpath(message_xpath).send_keys(tweet)
time.sleep(2)
driver.find_element_by_xpath(post_xpath).click()


