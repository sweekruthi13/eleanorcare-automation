from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def locate_by_id_demo():
# Initialize the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Step 1: Navigate to the homepage
    driver.get("https://www.eleanorcare.ai/")
    print("Navigated to the EleanorCare homepage")
    driver.maximize_window()
    time.sleep(3)

# Step 2: Click on the Login page
    driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
    time.sleep(3)

# Step 3: Enter email
    driver.find_element(By.ID, "email").send_keys("maintesting@gmail.com")
    time.sleep(3)

# Step 4: Enter password
    driver.find_element(By.ID, "password").send_keys("main@123")
    time.sleep(3)

# Step 5: Show password (optional)
    driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
    time.sleep(3)

# Step 6: Click the Sign-In button
    driver.find_element(By.XPATH, "//button[normalize-space()='SIGN IN']").click()
    print("Clicked on the Sign In button successfully")
    time.sleep(3)

# Step 4: Enter OTP

    driver.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys()
    print("entered otp")
    time.sleep(10)

# Step 8: click on check
    driver.find_element(By.XPATH, "//button[normalize-space()='CHECK']").click()
    print("clicked on check button")
    time.sleep(2)

# Step 9: Click on the dashboard button ( we need to copy real xpath and paste not index xpath)
    driver.find_element(By.XPATH,"//span[@class='px-1'][normalize-space()='Dashboard']").click()
    print("clicked on dashboard")
    time.sleep(3)

#Step 10: Click on donation button
    driver.find_element(By.XPATH, "//span[@class='px-1'][normalize-space()='Donations']").click()
    print("Clicked on donation button")
    time.sleep(3)

#step 11 : click on the Alldonations
    driver.find_element(By.XPATH,"//a[normalize-space()='All Donations']").click()
    print("clicked on all donations")
    time.sleep(3)

#step 12 : click on Add donation to add details for cash payment
    driver.find_element(By.XPATH,"//button[normalize-space()='Add Donation']").click()
    driver.find_element(By.ID, "firstName").send_keys("Test")
    time.sleep(2)
    driver.find_element(By.ID,"lastName").send_keys("T")
    time.sleep(2)
    driver.find_element(By.ID,"phone").send_keys("6362210574")
    time.sleep(2)
    driver.find_element(By.ID,"email").send_keys("sweekruthi@eleanortechnologies.com")
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@id='panNumber']").send_keys("QWERQ1234A")
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@id='agentName']").send_keys("xxx")
    time.sleep(2)
    driver.find_element(By.XPATH,"//textarea[@id='address']").send_keys("Banglore")
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[@id='headlessui-tabs-tab-:r8:']").click()
    time.sleep(2)
    print("clicked on cash")
    driver.find_element(By.XPATH,"//button[@id='headlessui-tabs-tab-:r9:']").click()
    time.sleep(2)
    print("clicked on online")
    driver.find_element(By.XPATH,"//button[@id='headlessui-tabs-tab-:ra:']").click()
    time.sleep(2)
    print("clicked on cheque")

#step 13: Go back to cash and enter the details
    driver.find_element(By.XPATH, "//button[@id='headlessui-tabs-tab-:r8:']").click()
    time.sleep(2)
    print("clicked on cash")
    driver.find_element(By.XPATH,"//input[@id='cashAmount']").send_keys("2000")
    time.sleep(2)
    print("entered amount")

    driver.find_element(By.XPATH,"//input[@id='cashPaymentDate']").click()
    time.sleep(5)
    print("selected payment date")

    driver.find_element(By.XPATH,"//button[normalize-space()='Add']").click()
    time.sleep(5)
    print("click on add button")

# after donor details is entered and click on add we go to all donations and add donations
# to check weather the donation has added or not
    driver.back()
    print("Navigated back to Google")
    time.sleep(2)

    driver.find_element(By.XPATH, "//span[@class='px-1'][normalize-space()='Donations']").click()
    print("Clicked on donation button")
    time.sleep(3)

    driver.find_element(By.XPATH, "//a[normalize-space()='All Donations']").click()
    print("clicked on all donations")
    time.sleep(10)


# #online payment
#     driver.find_element(By.XPATH, "//button[normalize-space()='Add Donation']").click()
#     driver.find_element(By.ID, "firstName").send_keys("Test")
#     time.sleep(2)
#     driver.find_element(By.ID, "lastName").send_keys("T")
#     time.sleep(2)
#     driver.find_element(By.ID,"phone").send_keys("6362210574")
#     time.sleep(2)
#     driver.find_element(By.ID,"email").send_keys("sweekruthi@eleanortechnologies.com")
#     time.sleep(2)
#     driver.find_element(By.XPATH,"//input[@id='panNumber']").send_keys("QWERQ1234A")
#     time.sleep(2)
#     driver.find_element(By.XPATH,"//input[@id='agentName']").send_keys("xxx")
#     time.sleep(2)
#     driver.find_element(By.XPATH,"//textarea[@id='address']").send_keys("Banglore")
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//button[@id='headlessui-tabs-tab-:r8:']").click()
#     time.sleep(2)
#     print("clicked on cash")
#     driver.find_element(By.XPATH, "//button[@id='headlessui-tabs-tab-:r9:']").click()
#     time.sleep(2)
#     print("clicked on online")
#     driver.find_element(By.XPATH, "//button[@id='headlessui-tabs-tab-:ra:']").click()
#     time.sleep(2)
#     print("clicked on cheque")
#
# # step 13: Go back to online and enter the details
#     driver.find_element(By.XPATH, "//button[@id='headlessui-tabs-tab-:r9:']").click()
#     time.sleep(2)
#     print("clicked on online")
#     driver.find_element(By.XPATH, "//input[@id='onlineBank']").send_keys("gpay")
#     time.sleep(2)
#     print("entered gpay")
#     driver.find_element(By.XPATH, "//input[@id='onlineAmount']").send_keys("100")
#     time.sleep(2)
#     print("entered 100")
#
#     driver.find_element(By.XPATH, "//input[@id='onlinePaymentDate']").click()
#     time.sleep(5)
#     print("selected payment date")
#
#     driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
#     time.sleep(5)
#     print("click on add button")
#
# # after donor details is entered and click on add we go to all donations and add donations
# # to check weather the donation has added or not
#     driver.back()
#     print("Navigated back to Google")
#     time.sleep(2)
#
#     driver.find_element(By.XPATH, "//span[@class='px-1'][normalize-space()='Donations']").click()
#     print("Clicked on donation button")
#     time.sleep(3)
#
#     driver.find_element(By.XPATH, "//a[normalize-space()='All Donations']").click()
#     print("clicked on all donations")
#     time.sleep(10)



# step 14: click on calendar drop down to select date
    driver.find_element(By.XPATH,"//button[@class='relative group block bg-primary p-1 rounded']//*[name()='svg']").click() #click on calender drop down
    time.sleep(10)
    print("clicked on calendar drop down")
    driver.find_element(By.XPATH,"//input[@id='toDateFilter']").click() #click on to date
    time.sleep(5)
    print("clicked on to date")
    driver.find_element(By.XPATH,"//input[@id='fromDateFilter']").click() #click on from date
    time.sleep(5)
    print("clicked on from date")
# To select and unselect cash,online,cheque
    driver.find_element(By.XPATH,"//button[normalize-space()='Cash']").click() #to select the cash
    time.sleep(10)
    print("clicked on cash")
    driver.find_element(By.XPATH,"//button[normalize-space()='Cash']").click() #to unselect the cash
    time.sleep(10)
    print("un clicked on cash")
    driver.find_element(By.XPATH,"//button[normalize-space()='Online']").click()#to select the online
    time.sleep(10)
    print("clicked on online")
    driver.find_element(By.XPATH,"//button[normalize-space()='Online']").click() #to unselect the online
    time.sleep(10)
    print("un clicked on online")
    driver.find_element(By.XPATH,"//button[normalize-space()='Cheques']").click() #to select the cheque
    time.sleep(10)
    print("clicked on cheque")
    driver.find_element(By.XPATH, "//button[normalize-space()='Cheques']").click() #to unselect the cheque
    time.sleep(10)
    print("un clicked on cheque")

#To select Cash with confirm payments and unconfirmed payments
    driver.find_element(By.XPATH,"//button[normalize-space()='Cash']").click() # select on cash
    time.sleep(10)
    print("clicked on cash")
    driver.find_element(By.XPATH,"//button[normalize-space()='Confirmed']").click()  #select on confirm payments for cash
    time.sleep(10)
    print("clicked on confirm payment for cash")
    driver.find_element(By.XPATH, "//button[normalize-space()='Confirmed']").click()  # unselect on confirm payments for cash
    time.sleep(10)
    print("unselect the confirm payments")
    driver.find_element(By.XPATH,"//button[normalize-space()='Unconfirmed']").click() #select on unconfirmed payments
    time.sleep(10)
    print("clicked on unconfirmed payments")
    driver.find_element(By.XPATH, "//button[normalize-space()='Unconfirmed']").click()  # unselect on unconfirmed payments
    time.sleep(10)
    print("unselect the unconfirmed payments")
    driver.find_element(By.XPATH, "//button[normalize-space()='Cash']").click()  # unselect on cash
    time.sleep(10)
    print("unselect the cash")

#To select online with confirm and unconfirmed payments
    driver.find_element(By.XPATH,"//button[normalize-space()='Online']").click() #click on online
    time.sleep(5)
    print("click on online")
    driver.find_element(By.XPATH,"//button[normalize-space()='Confirmed']").click() # select on confirm button
    time.sleep(5)
    print("click on confirmed for online")
    driver.find_element(By.XPATH,"//button[normalize-space()='Confirmed']").click()# un select on confirm button
    time.sleep(5)
    print("un select confirm payment for online")
    driver.find_element(By.XPATH,"//button[normalize-space()='Unconfirmed']").click() # click on unconfirmed button
    time.sleep(5)
    print("click on unconfirmed button for online")
    driver.find_element(By.XPATH,"//button[normalize-space()='Unconfirmed']").click() # un select unconfirmed button
    time.sleep(5)
    print("un select the unconfirmed button for online")
    driver.find_element(By.XPATH,"//button[normalize-space()='Online']").click() #unselect on online
    time.sleep(5)
    print("un select on online")

#To select cheque with confirm and unconfirmed payments
    driver.find_element(By.XPATH,"//button[normalize-space()='Cheques']").click() #click on cheque
    time.sleep(5)
    print("click on cheque button")
    driver.find_element(By.XPATH, "//button[normalize-space()='Confirmed']").click()  # select on confirm button
    time.sleep(5)
    print("click on confirmed for online")
    driver.find_element(By.XPATH, "//button[normalize-space()='Confirmed']").click()  # un select on confirm button
    time.sleep(5)
    print("un select confirm payment for online")
    driver.find_element(By.XPATH, "//button[normalize-space()='Unconfirmed']").click()  # click on unconfirmed button
    time.sleep(5)
    print("click on unconfirmed button for online")
    driver.find_element(By.XPATH, "//button[normalize-space()='Unconfirmed']").click()  # un select unconfirmed button
    time.sleep(5)
    print("un select the unconfirmed button for online")
    driver.find_element(By.XPATH, "//button[normalize-space()='Cheques']").click()  # un check on cheque
    time.sleep(5)
    print("unselect on cheque button")


# step 15: Sub organization drop down button for sorting date and check with cash,online,cheque,confirmed and unconfirmed
    driver.find_element(By.XPATH,"//div[@class='text-sm__input-container css-19bb58m']").click() #click on the suborg dropdown
    time.sleep(10)
    print("clicked on the sub organization drop down")
    driver.find_element(By.XPATH,"//button[@class='relative group block bg-primary "
                                 "p-1 rounded']//*[name()='svg']").click()#click on drop down for date
    time.sleep(10)
    print("clicked on calendar drop down")
    driver.find_element(By.XPATH,"//input[@id='toDateFilter']").click()#click on to date
    time.sleep(5)
    print("clicked on to date")
    driver.find_element(By.XPATH,"//input[@id='fromDateFilter']").click() #click on from date
    time.sleep(5)
    print("clicked on from date")
    driver.find_element(By.XPATH, "//button[normalize-space()='Cash']").click()  # select on cash
    time.sleep(10)
    print("clicked on cash")
    driver.find_element(By.XPATH, "//button[normalize-space()='Confirmed']").click()  # select on confirm payments for cash
    time.sleep(10)
    print("clicked on confirm payment for cash")
    driver.find_element(By.XPATH, "//button[normalize-space()='Confirmed']").click()  # unselect on confirm payments for cash
    time.sleep(10)
    print("unselect the confirm payments")
    driver.find_element(By.XPATH, "//button[normalize-space()='Unconfirmed']").click()  # select on unconfirmed payments
    time.sleep(10)
    print("clicked on unconfirmed payments")
    driver.find_element(By.XPATH, "//button[normalize-space()='Unconfirmed']").click()  # unselect on unconfirmed payments
    time.sleep(10)
    print("unselect the unconfirmed payments")
    driver.find_element(By.XPATH, "//button[normalize-space()='Cash']").click()  # unselect on cash
    time.sleep(10)
    print("unselect the cash")

    driver.find_element(By.XPATH,"//button[normalize-space()='Online']").click() #click on online
    time.sleep(5)
    print("click on online")
    driver.find_element(By.XPATH,"//button[normalize-space()='Confirmed']").click() # select on confirm button
    time.sleep(5)
    print("click on confirmed for online")
    driver.find_element(By.XPATH,"//button[normalize-space()='Confirmed']").click()# un select on confirm button
    time.sleep(5)
    print("un select confirm payment for online")
    driver.find_element(By.XPATH,"//button[normalize-space()='Unconfirmed']").click() # click on unconfirmed button
    time.sleep(5)
    print("click on unconfirmed button for online")
    driver.find_element(By.XPATH,"//button[normalize-space()='Unconfirmed']").click() # un select unconfirmed button
    time.sleep(5)
    print("un select the unconfirmed button for online")
    driver.find_element(By.XPATH,"//button[normalize-space()='Online']").click() #unselect on online
    time.sleep(5)
    print("un select on online")

    driver.find_element(By.XPATH,"//button[normalize-space()='Cheques']").click() #click on cheque
    time.sleep(5)
    print("click on cheque button")
    driver.find_element(By.XPATH, "//button[normalize-space()='Confirmed']").click()  # select on confirm button
    time.sleep(5)
    print("click on confirmed for online")
    driver.find_element(By.XPATH, "//button[normalize-space()='Confirmed']").click()  # un select on confirm button
    time.sleep(5)
    print("un select confirm payment for online")
    driver.find_element(By.XPATH, "//button[normalize-space()='Unconfirmed']").click()  # click on unconfirmed button
    time.sleep(5)
    print("click on unconfirmed button for online")
    driver.find_element(By.XPATH, "//button[normalize-space()='Unconfirmed']").click()  # un select unconfirmed button
    time.sleep(5)
    print("un select the unconfirmed button for online")
    driver.find_element(By.XPATH, "//button[normalize-space()='Cheques']").click()  # un check on cheque
    time.sleep(5)
    print("unselect on cheque button")
    driver.find_element(By.XPATH,"//div[@class='text-sm__input-container css-19bb58m']").click() #click on the suborg dropdown
    time.sleep(10)
    print("clicked on the sub organization drop down")

#step 16 : upload file button
    driver.find_element(By.XPATH,"//button[normalize-space()='Upload file']").click() #click on upload file button
    time.sleep(5)
    print("click on the file upload button")


    driver.find_element(By.XPATH,"//button[contains(@class,'-mb-[1px] block border border-transparent p-3.5 py-2 hover:text-primary "
                                 "dark:hover:border-b-black')][normalize-space()='Cash']").click() #click on cash
    time.sleep(5)
    print("clicked on cash in upload file button")
    driver.find_element(By.XPATH, "//a[normalize-space()='Click here']").click()  # download sample csv for cash
    time.sleep(3)
    print("download sample csv for cash")


    driver.find_element(By.XPATH,"//button[contains(@class,'-mb-[1px] block border border-transparent p-3.5 py-2"
                                 " hover:text-primary dark:hover:border-b-black')][normalize-space()='Online']").click() #click on online
    time.sleep(5)
    print("clicked on online in upload file button")
    driver.find_element(By.XPATH, "//a[normalize-space()='Click here']").click()  # download sample csv for online
    time.sleep(3)
    print("Download sample CSV for online")


    driver.find_element(By.XPATH,"//button[contains(@class,'-mb-[1px] block border border-transparent p-3.5 py-2 hover:text-primary"
                                 " dark:hover:border-b-black')][normalize-space()='Cheques']").click() #click on cheque
    time.sleep(5)
    print("clicked on cheque file upload button")
    driver.find_element(By.XPATH,"//a[normalize-space()='Click here']").click()# click on download sample csv click here
    time.sleep(5)
    print("download sample CSV file for cheque")


#Choose file in upload file button
    # driver.find_element(By.XPATH,"//button[contains(@class,'-mb-[1px] block border border-transparent p-3.5 py-2 hover:text-primary "
    #                              "dark:hover:border-b-black')][normalize-space()='Cash']").click() #click on cash
    # time.sleep(5)
    # print("clicked on cash ")
    # driver.find_element(By.XPATH,"//input[@type='file']").click() # click on the choose file button to upload the old files
    # time.sleep(5)
    # print("click on the choose file button")
    #
    #
    # driver.find_element(By.XPATH,"//button[contains(@class,'-mb-[1px] block border border-transparent p-3.5 py-2 "
    #                              "hover:text-primary dark:hover:border-b-black')][normalize-space()='Online']").click() #click on online
    # time.sleep(5)
    # print("click on online")
    # driver.find_element(By.XPATH,"//input[@type='file']").click() #click on choose file in online
    # time.sleep(5)
    # print("clicked on choose file for online")
    #
    #
    # driver.find_element(By.XPATH,"//button[contains(@class,'-mb-[1px] block border border-transparent p-3.5 py-2 hover:text-primary"
    #                              " dark:hover:border-b-black')][normalize-space()='Cheques']").click() #click on cheque
    # time.sleep(5)
    # print("clicked on cheque")
    # driver.find_element(By.XPATH,"//input[@type='file']").click() #clicked on choose file in cheque
    # time.sleep(5)
    # print("clicked on choose file button in cheque")


# close the upload file tab using x mark
    driver.find_element(By.XPATH,"//button[@class='absolute top-4 text-gray-400 outline-none hover:text-gray-800 "
                                 "ltr:right-4 rtl:left-4 dark:hover:text-gray-600']//*[name()='svg']").click() #clicked on x mark
    time.sleep(5)
    print("clicked on x mark of upload file button to close the tab")

    driver.find_element(By.XPATH, "//span[@class='px-1'][normalize-space()='Donations']").click()
    print("Clicked on donation button")
    time.sleep(3)

    driver.find_element(By.XPATH, "//a[normalize-space()='All Donations']").click()
    print("clicked on all donations")
    time.sleep(10)

#To download duplicate entries, you need to select a two-month range from
#the calendar. If your sub-organization has any duplicate entries within that period, they will be displayed in the excel which is downloaded.
    driver.find_element(By.XPATH,"//button[@class='relative group block bg-primary p-1 rounded']//*[name()='svg']").click() #click on calender drop down
    time.sleep(10)
    print("clicked on calendar drop down")
    driver.find_element(By.XPATH,"//input[@id='toDateFilter']").click() #click on to date
    time.sleep(5)
    print("clicked on to date")
    driver.find_element(By.XPATH,"//input[@id='fromDateFilter']").click() #click on from date
    time.sleep(5)
    print("clicked on from date")
    driver.find_element(By.XPATH,"//button[normalize-space()='Download Duplicates']").click() #download the duplicate file for
                                                                                                    # 2 months in the form of excel
    time.sleep(5)
    print("clicked on download duplicate button")



# Close the browser
time.sleep(5)



# Run the function
locate_by_id_demo()