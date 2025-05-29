import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

def locate_by_id_demo():
    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Navigate to the homepage
    #driver.get("https://www.eleanorcare.ai/")
    driver.get("http://localhost:3000/")
    print("Navigated to the EleanorCare homepage")
    driver.maximize_window()
    time.sleep(3)

    #driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
    #time.sleep(3)

    # Enter email
    driver.find_element(By.ID, "email").send_keys("maintesting@gmail.com")
    time.sleep(3)

    # Enter password
    driver.find_element(By.ID, "password").send_keys("main@123")
    time.sleep(3)

    # Click the Sign-In button
    driver.find_element(By.XPATH, "//button[normalize-space()='SIGN IN']").click()
    print("Clicked on the Sign In button successfully")
    time.sleep(3)

    # Enter OTP
    driver.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys()
    print("Entered OTP")
    time.sleep(10)

    # Click on "CHECK"
    driver.find_element(By.XPATH, "//button[normalize-space()='CHECK']").click()
    print("Clicked on CHECK button")
    time.sleep(7)

    # Navigate to Employees → Teams → Add Team
    driver.find_element(By.XPATH, "//span[@class='px-1'][normalize-space()='Employees']").click()
    print("Clicked on Employees")
    time.sleep(6)

    driver.find_element(By.XPATH, "//a[normalize-space()='Teams']").click()
    print("Clicked on Teams")
    time.sleep(3)

    driver.find_element(By.XPATH, "//button[normalize-space()='Add team']").click()
    print("Clicked on Add Team")
    time.sleep(3)

    driver.find_element(By.XPATH, "//input[@id='name']").send_keys("team11")
    print("Entered Team Name")
    time.sleep(3)

    driver.find_element(By.XPATH, "//textarea[@id='description']").send_keys("Complete the task")
    print("Entered Description")
    time.sleep(3)

    # Click on Manager Dropdown
    dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "select-manager"))
    )
    dropdown.click()
    print("Clicked on Manager dropdown")
    time.sleep(3)

    # Wait for the dropdown options to be visible
   # options_list = WebDriverWait(driver, 10).until(
        #EC.presence_of_element_located((By.CLASS_NAME, "select-manager__menu"))
    #)

    # Select an option using visible text
    #option = WebDriverWait(driver, 10).until(
        #EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'select-manager__option') and text()='Manager Name']"))
    #)
    #option.click()
   # print("Selected Manager")
    #time.sleep(3)

    # Click on Add Button
    driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
    print("Clicked on Add button")
    time.sleep(3)

#click on employees and then teams to edit team
    driver.find_element(By.XPATH, "//span[@class='px-1'][normalize-space()='Employees']").click()
    print("Clicked on Employees")
    time.sleep(3)

    driver.find_element(By.XPATH, "//a[normalize-space()='Teams']").click()
    print("Clicked on Teams")
    time.sleep(3)

    driver.find_element(By.ID,"edit-team").click()
    print("clicked on edit button")
    time.sleep(8)

    driver.find_element(By.XPATH,"//button[normalize-space()='Update']").click()
    print("clicked on update")
    time.sleep(6)

# click on employee and team to delete team
    driver.find_element(By.XPATH, "//span[@class='px-1'][normalize-space()='Employees']").click()
    print("Clicked on Employees")
    time.sleep(3)

    driver.find_element(By.XPATH, "//a[normalize-space()='Teams']").click()
    print("Clicked on Teams")
    time.sleep(3)

    driver.find_element(By.ID,"delete-team").click()
    print("clicked on delete button")
    time.sleep(5)

    driver.find_element(By.XPATH,"//button[normalize-space()='Cancel']").click()
    print("clicked on cancel button")
    time.sleep(5)

    # Close the browser
    driver.quit()

# Run the function
locate_by_id_demo()
