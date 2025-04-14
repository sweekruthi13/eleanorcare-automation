from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random  # to generate random values, which help in creating dynamic and unique test data in Selenium automation.

def locate_by_id_demo(): # Define the function
                            # # Call the function at the end of the code

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Navigate to the homepage
    #driver.get("https://www.eleanorcare.ai/")
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
    time.sleep(10)

#Enter OTP

    driver.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys()
    print("entered otp")
    time.sleep(10)

#click on check
    driver.find_element(By.XPATH, "//button[normalize-space()='CHECK']").click()
    print("clicked on check button")
    time.sleep(10)

#click on employees to select the volunteers drop down
    driver.find_element(By.XPATH,"//span[@class='px-1'][normalize-space()='Employees']").click()#clicked on employee
    print("clicked on employee to select volunteer")
    time.sleep(5)
    driver.find_element(By.XPATH,"//a[normalize-space()='Volunteers']").click()#clicked on volunteers
    print("clicked on volunteer")
    time.sleep(5)
    driver.find_element(By.XPATH,"//button[normalize-space()='Add Volunteer']").click()#click on add volunteers
    print("clicked on add volunteer")
    time.sleep(5)



    # Generate a random email to avoid duplication
    random_email = f"zibra{random.randint(1000, 9999)}@gmail.com"  # random.randint(1000, 9999)# This generates a random 4-digit number between 1000 and 9999.
                                                                                                # Example outputs: 4321, 7890, 1234, etc.
                                                                                                # This is an f-string (formatted string) in Python.
                                                                                                # The {random.randint(1000, 9999)} part gets replaced with a random number.



    driver.find_element(By.XPATH,"//input[@id='firstName']").send_keys("shift")#entered first name
    print("entered first name")
    time.sleep(5)
    driver.find_element(By.XPATH,"//input[@id='lastName']").send_keys("S")#entered last name
    print("entered last name")
    time.sleep(5)
    driver.find_element(By.XPATH, "//input[@id='email']").send_keys(random_email)
    print(f"entered email: {random_email}")
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@id='password']").send_keys("1234")#entered password
    print("entered password")
    time.sleep(5)
    driver.find_element(By.XPATH,"//input[@class='form-input flatpickr-input']").click()
    print("clicked on account expiry date")
    time.sleep(5)



    try:
        role_dropdown = driver.find_element(By.ID, "Select-volunteer roles")
        role_dropdown.click()
        time.sleep(5)

        default_role = driver.find_element(By.XPATH, "//div[text()='Donation entry']")  # Replace with actual role name
        default_role.click()
        print("Selected a default role")
    except Exception as e:
            print("Skipping role selection as it's not found:", e)
    time.sleep(5)


# driver.find_element(By.ID,"Select-volunteer roles").click() #selected roles
# print("clicked on roles")
# time.sleep(5)
    driver.find_element(By.XPATH,"//input[@id='phone']").send_keys("2365897456")#entered phone number
    print("entered phone number")
    time.sleep(5)
    driver.find_element(By.XPATH,"//button[normalize-space()='Add']").click()#clicked on add button
    print("clicked on add button")
    time.sleep(5)




# Close the browser
time.sleep(5)



# Run the function
locate_by_id_demo()