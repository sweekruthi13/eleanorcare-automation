
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
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

#campaigns button header
    driver.find_element(By.XPATH,"//span[@class='px-1'][normalize-space()='Campaigns']").click()#click on campaign
    time.sleep(5)
    print("Clicked on the campaign page")
    driver.find_element(By.XPATH,"//a[normalize-space()='All Campaigns']").click()#click on all campaign
    time.sleep(5)
    print("clicked on all campaign")
    driver.find_element(By.XPATH,"//button[normalize-space()='Add Campaign']").click()#click on add campaign
    time.sleep(5)
    print("clicked on add campaign")
    driver.find_element(By.XPATH,"//div[@class='panel mb-5 w-full']//button[1]//*[name()='svg']").click()#clicked on edit button for header
    time.sleep(10)
    print("clicked on edit button for the header")
    driver.find_element(By.XPATH,"//button[@id='headlessui-tabs-tab-:rg:']").click()#clicked on enter text
    time.sleep(10)
    print("entered the text manuvally")
    driver.find_element(By.XPATH,"//button[@class='absolute top-4 text-gray-400 outline-none hover:text-gray-800 "
                                 "ltr:right-4 rtl:left-4 dark:hover:text-gray-600']//*[name()='svg']") #click on x button
    time.sleep(10)
    print("click on the x button")


#To generate AI content for header section
    driver.find_element(By.XPATH,"//div[@class='panel mb-5 w-full']//button[1]//*[name()='svg']").click()#click on edit button for header
    time.sleep(10)
    print("click on edit button for the header")
    driver.find_element(By.XPATH,"//button[@id='headlessui-tabs-tab-:ru:']").click()#click on the generate text for AI
    time.sleep(10)  
    print("clicked on generate text for the AI")
    driver.find_element(By.XPATH,"//button[normalize-space()='Click to generate AI content']").click()#click on "click to generate AI content
    time.sleep(10)
    print("click to generate AI content")
    driver.find_element(By.XPATH,"//button[normalize-space()='Use this text']").click()#click on use this text button
    time.sleep(10)
    print("click on use this text")

#campaign 2nd edit button for content which is below header
    driver.find_element(By.XPATH,"//div[@class='panel mb-5 w-full']//button[2]//*[name()='svg']").click()#click on content edit button
    time.sleep(5)
    print("click on content edit button") 
    driver.find_element(By.XPATH,"//button[@id='headlessui-tabs-tab-:r1f:']").click()#click on enter text for the content
    time.sleep(10)
    print("entered the content")
    driver.find_element(By.XPATH,"//button[@class='absolute top-4 text-gray-400 outline-none hover:text-gray-800 ltr:right-4 "
                                 "rtl:left-4 dark:hover:text-gray-600']//*[name()='svg']//*[name()='path' and "
                                 "contains(@d,'M512 0C229')]")#click on x button
    time.sleep(10)
    print("click on x button")
    driver.find_element(By.XPATH,"//div[@class='panel mb-5 w-full']//button[2]//*[name()='svg']").click()#click on edit button for
                                                                    #content to add AI content
    time.sleep(10)
    print("click on the edit button to enter the AI content")
    driver.find_element(By.XPATH,"//button[@id='headlessui-tabs-tab-:r1m:']").click()#click on generate AI text content
    time.sleep(10)
    print("click on the AI text to add the AI content")
    driver.find_element(By.XPATH,"//button[normalize-space()='Click to generate AI content']").click()#click to generate AI content
    time.sleep(10)
    print("click to generate AI content")
    driver.find_element(By.XPATH,"//button[normalize-space()='Use this text']").click()#click on use this text
    time.sleep(10)
    print("click on use this text")


# Close the browser
time.sleep(5)



# Run the function
locate_by_id_demo()