from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def locate_by_id_demo():
# Initialize the Chrome driver

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Navigate to the homepage
    #driver.get("https://www.eleanorcare.ai/")
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

#click on expense
    driver.find_element(By.XPATH,"//span[@class='px-1'][normalize-space()='Expenses']").click()
    print("clicked on expense button")
    time.sleep(5)
    driver.find_element(By.XPATH,"//a[normalize-space()='Expenses']").click() #click on drop down for expense
    print("clicked on expense drop down")
    time.sleep(5)
    driver.find_element(By.XPATH,"//button[normalize-space()='Add expense']").click() #clicked on add expense button
    print("clicked on add expense button")
    time.sleep(5)
    driver.find_element(By.XPATH,"//input[@id='name']").send_keys("test") #entered name
    print("Entered name")
    time.sleep(5)
    driver.find_element(By.XPATH,"//textarea[@id='description']").send_keys("spent expense")#enter description
    print("Entered desciption")
    time.sleep(5)
    driver.find_element(By.XPATH,"//input[@id='paymentDate']").click()#clicked on date
    print("Clicked on payment date")
    time.sleep(5)

    driver.find_element(By.ID,"select-categories").click()
    print("clicked on select categories")
    time,sleep(5)
    driver.find_element(By.ID,"Select-tags").click()
    print("clicked on select tags")
    time.sleep(5)

    driver.find_element(By.XPATH,"//button[normalize-space()='Add Line Item']").click()#clicked on add line item
    print("clicked on add line item")
    time.sleep(5)
    driver.find_element(By.XPATH,"//input[@id='lineItemName']").send_keys("Pencil")#entered item name
    print("entered lineitemname")
    time.sleep(5)
    driver.find_element(By.XPATH,"//textarea[@id='lineItemDescription']").send_keys("purchased the pencil")#entered lineitem description
    print("entered description")
    time.sleep(5)
    driver.find_element(By.XPATH,"//input[@id='lineItemAmount']").send_keys("1000")#entered line item amount
    print("entered line item amount")
    time.sleep(5)
    driver.find_element(By.XPATH,"//button[normalize-space()='Add']").click()#clicked on add button
    print("clicked on add button")
    time.sleep(5)

# again click on expense and check with the filter options
    driver.find_element(By.XPATH, "//span[@class='px-1'][normalize-space()='Expenses']").click()
    print("clicked on expense button")
    time.sleep(5)
    driver.find_element(By.XPATH, "//a[normalize-space()='Expenses']").click()  # click on drop down for expense
    print("clicked on expense drop down")
    time.sleep(5)
#selected date filter
    driver.find_element(By.XPATH,"//input[@id='fromDateFilter']").click()#clicked on date filter for from date
    print("clicked on from date")
    time.sleep(5)
    driver.find_element(By.XPATH,"//input[@id='toDateFilter']").click()#clicked on to date filter to date
    print("clicked on to date")
    time.sleep(5)
#selecting categories and tags
    driver.find_element(By.ID,"expense-categories").click()
    print("clicked on expense categories")
    time.sleep(7)
    driver.find_element(By.ID,"expense-tags").click()
    print("clicked on tags")
    time.sleep(5)

#if you want to edit expense
    driver.find_element(By.XPATH, "//span[@class='px-1'][normalize-space()='Expenses']").click()
    print("clicked on expense button")
    time.sleep(5)
    driver.find_element(By.XPATH, "//a[normalize-space()='Expenses']").click()  # click on drop down for expense
    print("clicked on expense drop down")
    time.sleep(5)

    driver.find_element(By.ID,"edit-expense").click()
    print("clicked on edit expense")
    time.sleep(5)

# Close the browser
time.sleep(5)



# Run the function
locate_by_id_demo()