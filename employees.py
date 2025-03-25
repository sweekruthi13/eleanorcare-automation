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
    time.sleep(10)

#click on employees
    driver.find_element(By.XPATH,"//span[@class='px-1'][normalize-space()='Employees']").click()#click on employees
    print("clicked on employees")
    time.sleep(10)

#click on employees drop down
    driver.find_element(By.XPATH,"//a[normalize-space()='Employees']").click()#clicked on drop down of employees
    print("clicked on employees from the dop down")
    time.sleep(5)
#click on add employees
    driver.find_element(By.XPATH,"//button[normalize-space()='Add Employee']").click()#clicked on add employees
    print("clicked on add employees")
    time.sleep(5)
    driver.find_element(By.XPATH,"//input[@id='firstName']").send_keys("zibra")#entered first name
    print("entered first name")
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@id='lastName']").send_keys("black")#entered last name
    print("entered last name")
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@id='email']").send_keys("zibra@gmail.com")#entered email
    print("entered email")
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@id='password']").send_keys("1234")#entered password
    print("entered password")
    time.sleep(3)
    driver.find_element(By.ID,"select-employee roles").click()#clicked on select roles
    print("clicked on select roles")
    time.sleep(5)
    driver.find_element(By.XPATH,"//input[@id='phone']").send_keys("1234569874")#entered phone number
    print("entered phone number")
    time.sleep(3)
    driver.find_element(By.XPATH,"//button[normalize-space()='Add']").click()#clicked on add button
    print("clicked on add button")
    time.sleep(3)
    driver.find_element(By.ID,"edit-employee").click()
    print("clicked on edit employee")
    time.sleep(10)




# Close the browser
time.sleep(5)



# Run the function
locate_by_id_demo()