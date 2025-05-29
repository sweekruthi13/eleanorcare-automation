import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# ✅ Function to generate a unique 10-digit Indian phone number
def generate_unique_phone():
    first_digit = random.choice(['9', '8', '7'])
    other_digits = ''.join(str(random.randint(0, 9)) for _ in range(9))
    return first_digit + other_digits

def locate_by_id_demo():
    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Navigate to the homepage
    driver.get("https://eleanor-web-pr-164.onrender.com/")
    print("Navigated to the EleanorCare homepage")
    driver.maximize_window()
    time.sleep(3)

    # Login
    driver.find_element(By.ID, "email").send_keys("maintesting@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("main@123")
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[normalize-space()='SIGN IN']").click()
    print("Clicked on the Sign In button successfully")
    time.sleep(3)

    # Enter OTP manually
    driver.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys("")
    print("Waiting for OTP input...")
    time.sleep(10)

    # Click on CHECK
    driver.find_element(By.XPATH, "//button[normalize-space()='CHECK']").click()
    print("Clicked on check button")
    time.sleep(5)

    # Click on Donations -> All Donors -> Add Donor
    driver.find_element(By.XPATH,"//span[@class='px-1'][normalize-space()='Donations']").click()
    print("Clicked on Donations")
    time.sleep(3)

    driver.find_element(By.XPATH, "//a[normalize-space()='All Donors']").click()
    print("Clicked on All Donors")
    time.sleep(3)

    driver.find_element(By.XPATH, "//button[normalize-space()='Add Donor']").click()
    print("Clicked on Add Donor")
    time.sleep(2)

    # Fill the donor form
    driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Test")
    print("Entered the donor name")
    time.sleep(1)

    driver.find_element(By.XPATH,"//input[@id='email']").send_keys("test@gmail.com")
    print("Entered email")
    time.sleep(1)

    # ✅ Use generated unique phone number
    unique_phone = generate_unique_phone()
    driver.find_element(By.XPATH,"//input[@id='phone']").send_keys(unique_phone)
    print("Entered phone number:", unique_phone)
    time.sleep(1)

    driver.find_element(By.XPATH,"//input[@id='pan']").send_keys("QWERT1231R")
    print("Entered PAN number")
    time.sleep(1)

    driver.find_element(By.XPATH,"//input[@id='addressLine1']").send_keys("Bangalore")
    print("Entered address line 1")
    time.sleep(1)

    driver.find_element(By.XPATH,"//input[@id='addressLine2']").send_keys("Mysore")
    print("Entered address line 2")
    time.sleep(1)

    driver.find_element(By.XPATH,"//input[@id='state']").send_keys("Karnataka")
    print("Entered state")
    time.sleep(1)

    driver.find_element(By.XPATH,"//input[@id='country']").send_keys("India")
    print("Entered country")
    time.sleep(1)

    driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
    print("Clicked on Add Donor")
    time.sleep(5)

    driver.quit()

# Run the function
locate_by_id_demo()
