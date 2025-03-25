from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def locate_by_id_demo():
# Initialize the Chrome driver

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Navigate to the homepage
    # driver.get("https://www.eleanorcare.ai/")
    driver.get("http://localhost:3000/")
    print("Navigated to the EleanorCare homepage")
    driver.maximize_window()
    time.sleep(3)

    # driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
    # time.sleep(3)

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
    time.sleep(20)

    driver.find_element(By.XPATH,"//span[normalize-space()='Custom Pages']").click()
    print("clicked on custom page")
    time.sleep(10)
    driver.find_element(By.XPATH,"//a[normalize-space()='All Custom Pages']").click()
    print("clicked on all custom page")
    time.sleep(10)
    driver.find_element(By.XPATH,"//button[normalize-space()='Add Custom Page']").click()
    print("clicked on add custom page")
    time.sleep(10)
    driver.find_element(By.XPATH,"//button[normalize-space()='Save']").click()
    print("clicked on save button")
    time.sleep(5)
    driver.find_element(By.ID,"language-drop-down").click()
    print("clicked on language drop down")
    time.sleep(10)
    driver.find_element(By.ID,"status-dropdown").click()
    print("clicked on status dropdown")
    time.sleep(10)
    driver.find_element(By.ID,"save-button").click()
    print("clicked on save button")
    time.sleep(10)

