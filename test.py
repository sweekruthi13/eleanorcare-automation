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

#more action
# GPT search button
#     driver.find_element(By.ID, "donations-more-action").click()
#     time.sleep(5)
#     print("clicked on the more action")
#     driver.find_element(By.XPATH, "//li[normalize-space()='GPTSearch']").click()
#     time.sleep(5)
#     print("clicked on gpt search")
#
#     driver.find_element(By.XPATH,"//input[@placeholder='Search with our AI integrated platform']").send_keys("Show donation for march 2024")#entered in gpt search
#     print("entered characters")
#     time.sleep(5)
#
#     driver.find_element(By.XPATH,"//button[normalize-space()='Search']").click()  # click on search once you clicked on the content
#     time.sleep(5)
#     print("clicked on search button")

# Actions

# click on the Alldonations
    driver.find_element(By.XPATH, "//span[@class='px-1'][normalize-space()='Donations']").click()
    print("Clicked on donation button")
    time.sleep(3)
    driver.find_element(By.XPATH, "//a[normalize-space()='All Donations']").click()
    print("clicked on all donations")
    time.sleep(3)

    driver.find_element(By.ID, "payment-verified").click()
    print("clicked on verify payments")
    time.sleep(10)
    driver.find_element(By.ID, "payment-confirmed").click()
    print("clicked on confirm payments")
    time.sleep(10)

# driver.find_element(By.ID,"download-duplicate-button").click()  # download the duplicate file for                                                                                                # 2 months in the form of Excel
    # time.sleep(5)
    # print("clicked on download duplicate button")
# #upload file button
#     driver.find_element(By.XPATH,"//li[normalize-space()='Upload from file']").click() #click on upload file button
#     time.sleep(4)
#     print("click on file upload button")



    #
    # driver.find_element(By.ID,"cash-header").click()
    # print("clicked on cash")
    # time.sleep(5)
    #
    #
    # driver.find_element(By.ID,"online-header").click()
    # print("clicked on online")
    # time.sleep(5)
    #
    # driver.find_element(By.ID,"cheque-header").click()
    # print("clicked on cheque")
    # time.sleep(5)


# Run the function
locate_by_id_demo()