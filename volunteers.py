from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def locate_by_id_demo():
# Initialize the Chrome driver

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Navigate to the homepage
    driver.get("https://www.eleanorcare.ai/")
    print("Navigated to the EleanorCare homepage")
    driver.maximize_window()
    time.sleep(3)

    driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
    time.sleep(3)

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

#click on employees to select the volunteers drop down
    driver.find_element(By.XPATH,"//span[@class='px-1'][normalize-space()='Employees']").click()#clicked on employee
    print("clicked on employee to select volunteer")
    time.sleep(3)
    driver.find_element(By.XPATH,"//a[normalize-space()='Volunteers']").click()#clicked on volunteers
    print("clicked on volunteer")
    time.sleep(3)
    driver.find_element(By.XPATH,"//button[normalize-space()='Add Volunteer']").click()#click on add volunteers
    print("clicked on add volunteer")
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@id='firstName']").send_keys("shift")#entered first name
    print("entered first name")
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@id='lastName']").send_keys("S")#entered last name
    print("entered last name")
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@id='email']").send_keys("s@gmail.com")#entered email
    print("entered email")
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@id='phone']").send_keys("2365897456")#entered phone number
    print("entered phone number")
    time.sleep(3)
    driver.find_element(By.XPATH,"//button[normalize-space()='Add']").click()#clicked on add button
    print("clicked on add button")
    time.sleep(3)


# Close the browser
time.sleep(5)



# Run the function
locate_by_id_demo()