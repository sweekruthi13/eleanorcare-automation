from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def locate_by_id_demo():
# Initialize the Chrome driver

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Navigate to the homepage
    #driver.get("https://www.eleanorcare.ai/")
    driver.get("http://localhost:3000/")
    print("Navigated to the EleanorCare homepage")
    driver.maximize_window()
    time.sleep(3)

    #driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
    #time.sleep(3)

#Enter email
    driver.find_element(By.ID, "email").send_keys("maintesting@gmail.com")
    time.sleep(3)

#Enter password
    driver.find_element(By.ID, "password").send_keys("main@123")
    time.sleep(3)
#Click the Sign-In button
    driver.find_element(By.XPATH, "//button[normalize-space()='SIGN IN']").click()
    print("Clicked on the Sign In button successfully")
    time.sleep(3)

#Enter OTP

    driver.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys()
    print("entered otp")
    time.sleep(10)

#click on check
    driver.find_element(By.XPATH, "//button[normalize-space()='CHECK']").click()
    print("clicked on check button")
    time.sleep(7)

#click on accounts button
    driver.find_element(By.XPATH,"//span[@class='px-1'][normalize-space()='Donations']").click()#clicked on donations
    print("clicked on donation")
    time.sleep(5)
    driver.find_element(By.XPATH,"//a[normalize-space()='Accounts']").click()#clicked on accounts
    print("clicked on accounts")
    time.sleep(3)
    driver.find_element(By.XPATH,"//button[normalize-space()='Add Account']").click()#click on add accounts
    print("clicked on add accounts")
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@id='name']").send_keys("accounts")#entered name
    print("entered name")
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@id='accNumber']").send_keys("123qwer1234qw")#entered acc number
    print("entered acc number")
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@id='accType']").send_keys("savings")#entered acc type
    print("entered acc type")
    time.sleep(3)
    driver.find_element(By.ID,"select-tags-dropdown").click()
    print("clicked on select tag")
    time.sleep(5)
    driver.find_element(By.XPATH,"//button[normalize-space()='Add']").click()#clicked on add
    print("click on add button")
    time.sleep(3)











# Close the browser
time.sleep(5)



# Run the function
locate_by_id_demo()