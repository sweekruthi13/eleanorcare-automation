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

# click on employees to select and team from employee dropdown
    driver.find_element(By.XPATH,"//span[@class='px-1'][normalize-space()='Employees']").click()#clicked on employee button
    print("clicked on employee button")
    time.sleep(3)
    driver.find_element(By.XPATH,"//a[normalize-space()='Teams']").click()#clicked on teams
    print("clicked on team button")
    time.sleep(3)
    driver.find_element(By.XPATH,"//button[normalize-space()='Add team']").click()#clicked on add team
    print("clicked on add team button")
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@id='name']").send_keys("team11")# entered name
    print("Entered name")
    time.sleep(3)
    driver.find_element(By.XPATH,"//textarea[@id='description']").send_keys("complete the task")# entered description
    print("entered description")
    time.sleep(3)
    #driver.find_element(By.XPATH,"")#click on manager drop down
    #print("clicked on manager")
    #time.sleep(3)

    driver.find_element(By.XPATH,"//button[normalize-space()='Add']")#clicked on add button
    print("clicked on add button")
    time.sleep(3)



# Close the browser
time.sleep(5)



# Run the function
locate_by_id_demo()