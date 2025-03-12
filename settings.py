
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
#settings
    driver.find_element(By.XPATH,"//span[@class='px-1'][normalize-space()='Settings']").click()#clicked on settings
    print("clicked on settings")
    time.sleep(3)
    driver.find_element(By.XPATH,"//a[normalize-space()='Organization']").click()#clicked on organization
    print("clicked on organization")
    time.sleep(3)
    driver.find_element(By.XPATH,"//button[@class='flex gap-2 border-b border-transparent p-4 hover:border-primary "
                                 "hover:text-primary !border-primary text-primary']").click()#clicked on main
    print("clicked on main")
    time.sleep(3)
    driver.find_element(By.XPATH,"//button[normalize-space()='Sub Organizations']").click()#clicked on suborganization
    print("clicked on sub organization")
    time.sleep(3)
    driver.find_element(By.XPATH,"//img[@alt='userProfile']").click()#click on user profile
    print("clicked on user profile to logout")
    time.sleep(3)
    driver.find_element(By.XPATH,"//div[@class='ml-4 flex cursor-pointer flex-row !py-3 text-danger']").click()#clicked on logout
    print("clicked on logout button")
    time.sleep(3)







# Close the browser
time.sleep(5)



# Run the function
locate_by_id_demo()
