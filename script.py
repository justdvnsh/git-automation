from selenium import webdriver
import pyautogui
from webdriver_manager.chrome import ChromeDriverManager
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '-p','--password',
    help="your github password",
    type=str
)
parser.add_argument(
    '-n', '--name',
    help='name for the repo',
    type=str
)
arguments = parser.parse_args()

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get("https://github.com/login")

username = driver.find_elements_by_xpath('//*[@id="login_field"]')[0]
username.click()
username.send_keys('justdvnsh')

password = driver.find_elements_by_xpath('//*[@id="password"]')[0]
password.click()
password.send_keys(arguments.password)

submit = driver.find_elements_by_xpath('//*[@id="login"]/form/div[3]/input[4]')[0]
submit.click()

new_repo = driver.find_elements_by_xpath('/html/body/div[4]/div/aside[1]/div[2]/div[2]/div/h2/a')[0]
new_repo.click()

repo_name = driver.find_elements_by_xpath('//*[@id="repository_name"]')[0]
repo_name.click()
repo_name.send_keys(arguments.name)

time.sleep(4)

create_repo = driver.find_elements_by_xpath('//*[@id="new_repository"]/div[3]/button')[0]
create_repo.click()
