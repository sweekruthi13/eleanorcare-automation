from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random  # to generate random values, which help in creating dynamic and unique test data in Selenium automation.

def locate_by_id_demo(): # Define the function
                            # # Call the function at the end of the code


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




    # Generate a random email to avoid duplication
    random_email = f"zibra{random.randint(1000, 9999)}@gmail.com" #random.randint(1000, 9999)
                                                                        #This generates a random 4-digit number between 1000 and 9999.
                                                                        # Example outputs: 4321, 7890, 1234, etc.
                                                                        #This is an f-string (formatted string) in Python.
                                                                        #The {random.randint(1000, 9999)} part gets replaced with a random number.


    # Enter details
    driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys("Zibra")
    print("entered first name")
    time.sleep(3)

    driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys("Black")
    print("entered last name")
    time.sleep(3)

    driver.find_element(By.XPATH, "//input[@id='email']").send_keys(random_email)
    print(f"entered email: {random_email}")
    time.sleep(3)

    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("1234")
    print("entered password")
    time.sleep(3)

    driver.find_element(By.ID, "select-employee roles").click()
    print("clicked on select roles")
    time.sleep(5)

    driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("1234569874")
    print("entered phone number")
    time.sleep(3)

    driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
    print("clicked on add button")
    time.sleep(3)

    #click on employees
    driver.find_element(By.XPATH,"//span[@class='px-1'][normalize-space()='Employees']").click()#click on employees
    print("clicked on employees")
    time.sleep(10)

    #click on employees drop down
    driver.find_element(By.XPATH,"//a[normalize-space()='Employees']").click()#clicked on drop down of employees
    print("clicked on employees from the dop down")
    time.sleep(5)

    driver.find_element(By.ID,"edit-employee").click()
    print("clicked on edit employee")
    time.sleep(10)
    driver.find_element(By.XPATH,"//button[normalize-space()='Update']").click()
    print("clicked on update button")
    time.sleep(5)






# Close the browser
time.sleep(5)



# Run the function
locate_by_id_demo()