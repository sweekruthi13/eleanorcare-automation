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
    time.sleep(2)
#Task drop down
    driver.find_element(By.XPATH,"//span[@class='px-1'][normalize-space()='Tasks']").click()#click on the task drop down
    time.sleep(5)
    print("clicked on task dropdown")
    driver.find_element(By.XPATH, "//a[normalize-space()='Tasks']").click()  # click on the task button
    print("clicked on tasks")
    time.sleep(3)

#Add a new task
    driver.find_element(By.XPATH,"//button[@class='btn btn-primary w-full']").click() #click on the add new task button
    time.sleep(10)
    print("clicked on add new task button")
    driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Auto test adding task") #enter task title
    time.sleep(3)
    print("Enter task title")
    driver.find_element(By.XPATH,"//div[@id='react-select-14-placeholder']").click() #enter the Assignees
    time.sleep(10)
    print("Click on Assignees")
    driver.find_element(By.XPATH,"//select[@id='priority']").click() #select the priority
    time.sleep(3)
    print("click on priority")
    driver.find_element(By.XPATH, "//div[@class='ql-editor ql-blank']").send_keys("Complete the task which have "
                                                                                 "been assigned to you") #enter the description
    time.sleep(3)
    print("Entered the description")
    driver.find_element(By.XPATH,"//button[@class='btn btn-primary ltr:ml-4 rtl:mr-4']").click()#click on add button
    time.sleep(3)
    print("Click on add button")

# Close the browser
time.sleep(5)



# Run the function
locate_by_id_demo()