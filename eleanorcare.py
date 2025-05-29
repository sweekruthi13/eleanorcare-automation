from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Function to generate a unique 10-digit Indian phone number
def generate_unique_phone():
    first_digit = random.choice(['9', '8', '7'])
    other_digits = ''.join(str(random.randint(0, 9)) for _ in range(9))
    return first_digit + other_digits

def locate_by_id_demo():
    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Navigate to the homepage
    driver.get("http://localhost:3000")
    print("Navigated to the EleanorCare homepage")
    driver.maximize_window()
    time.sleep(3)

    # Login
    driver.find_element(By.ID, "email").send_keys("sweekruthi@eleanortechnologies.com")
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
    time.sleep(10)
#Click on the dashboard button ( we need to copy real xpath and paste not index xpath)
    driver.find_element(By.XPATH,"//span[@class='px-1'][normalize-space()='Dashboard']").click() 
    print("clicked on dashboard")
    time.sleep(10)

#Click on donation button
    driver.find_element(By.XPATH, "//span[@class='px-1'][normalize-space()='Donations']").click()
    print("Clicked on donation button")
    time.sleep(5)

#click on the Alldonations
    driver.find_element(By.XPATH,"//a[normalize-space()='All Donations']").click()
    print("clicked on all donations")
    time.sleep(5)



#click on Add donation to add details for cash payment
    driver.find_element(By.XPATH,"//button[normalize-space()='Add Donation']").click()
    time.sleep(5)
    print("clicked on add donation")
    driver.find_element(By.ID, "firstName").send_keys("Test")
    time.sleep(2)
    print("clicked on first name")
    driver.find_element(By.ID,"lastName").send_keys("T")
    time.sleep(2)
    print("clicked on last name")
    driver.find_element(By.ID,"phone").send_keys("6362210574")
    time.sleep(2)
    print("clicked on phone")
    driver.find_element(By.ID,"email").send_keys("sweekruthi@eleanortechnologies.com")
    time.sleep(2)
    print("clicked on email")
    driver.find_element(By.XPATH,"//input[@id='panNumber']").send_keys("QWERQ1234A")
    time.sleep(2)
    print("clicked on phone number")
    driver.find_element(By.XPATH,"//input[@id='agentName']").send_keys("xxx")
    time.sleep(2)
    print("clicked on agent name")
    driver.find_element(By.XPATH,"//textarea[@id='address']").send_keys("Banglore")
    time.sleep(5)
    print("entered address")
    driver.find_element(By.ID,"select-campaign-dropdown").click()
    print("clicked on select campaign dropdown")
    time.sleep(5)
    driver.find_element(By.ID,"select-target-account").click()
    print("clicked on target account")
    time.sleep(5)
    driver.find_element(By.ID,"click-cash-donation").click()
    print("clicked on cash")
    time.sleep(2)
    driver.find_element(By.ID,"click-online-donation").click()
    print("clicked on online")
    time.sleep(2)
    driver.find_element(By.ID,"click-cheque-donation").click()
    print("clicked on cheque")
    time.sleep(2)

#Go back to cash and enter the details
    driver.find_element(By.ID,"cash-donation-button").click()
    print("clicked on cash")
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@id='cashAmount']").send_keys("2000")
    print("entered amount")
    time.sleep(2)

    driver.find_element(By.XPATH,"//input[@id='cashPaymentDate']").click()
    time.sleep(5)
    print("selected payment date")

    driver.find_element(By.XPATH,"//button[normalize-space()='Add']").click()
    time.sleep(5)
    print("click on add button")

# #Actions
#     driver.find_element(By.ID,"payment-verified").click()
#     print("clicked on verify payments")
#     time.sleep(10)
#     driver.find_element(By.ID,"payment-confirmed").click()
#     print("clicked on confirm payments")
#     time.sleep(10)


# after donor details is entered and click on add we go to all donations and add donations
# to check weather the donation has added or not
    driver.back()
    print("Navigated back to Google")
    time.sleep(5)

    driver.find_element(By.XPATH, "//span[@class='px-1'][normalize-space()='Donations']").click()
    print("Clicked on donation button")
    time.sleep(5)


    driver.find_element(By.XPATH, "//a[normalize-space()='All Donations']").click()
    print("clicked on all donations")
    time.sleep(10)

#Donations
    driver.find_element(By.XPATH,"//span[@class='px-1'][normalize-space()='Donations']").click()
    print("Clicked on donation button")
    time.sleep(5)
#accounts
    driver.find_element(By.XPATH,"//a[normalize-space()='Accounts']").click()#clicked on accounts
    print("clicked on accounts")
    time.sleep(10)

    driver.find_element(By.XPATH,"//button[normalize-space()='Add Account']").click()#click on Add accounts
    print("clicked on add accounts")
    time.sleep(10)

    driver.find_element(By.XPATH,"//input[@id='name']").send_keys("test") #entered name
    print("Entered name")
    time.sleep(10)

    driver.find_element(By.XPATH,"//input[@id='accNumber']").send_keys("1234567891")#entered account number
    print("entered account number")
    time.sleep(10)

    driver.find_element(By.XPATH,"//input[@id='accType']").send_keys("Current")#entered account type
    print("entered account type")
    time.sleep(10)

    driver.find_element(By.ID, "select-tags-dropdown").click()
    print("clicked on select tag dropdown")
    time.sleep(5)

    driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()  # clicked on add
    print("click on add button")

    time.sleep(5)

    #driver.find_element(By.XPATH,"//span[@class='px-1'][normalize-space()='Donations']").click()
    #print("Clicked on donation button")
    #time.sleep(5)

   # driver.find_element(By.XPATH, "//a[normalize-space()='All Donations']").click()
    #print("clicked on all donations")
    #time.sleep(10)

    # Click on Donations -> All Donors -> Add Donor
    driver.find_element(By.XPATH, "//span[@class='px-1'][normalize-space()='Donations']").click()
    print("Clicked on Donations")
    time.sleep(3)

    driver.find_element(By.XPATH, "//a[normalize-space()='All Donors']").click()
    print("Clicked on All Donors")
    time.sleep(3)

    driver.find_element(By.XPATH, "//button[normalize-space()='Add Donor']").click()
    print("Clicked on Add Donor")
    time.sleep(2)

    # Fill the donor form
    driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Test")
    print("Entered the donor name")
    time.sleep(1)

    driver.find_element(By.XPATH, "//input[@id='email']").send_keys("test@gmail.com")
    print("Entered email")
    time.sleep(1)

    #  Use generated unique phone number
    unique_phone = generate_unique_phone()
    driver.find_element(By.XPATH, "//input[@id='phone']").send_keys(unique_phone)
    print("Entered phone number:", unique_phone)
    time.sleep(1)

    driver.find_element(By.XPATH, "//input[@id='pan']").send_keys("QWERT1231R")
    print("Entered PAN number")
    time.sleep(1)

    driver.find_element(By.XPATH, "//input[@id='addressLine1']").send_keys("Bangalore")
    print("Entered address line 1")
    time.sleep(1)

    driver.find_element(By.XPATH, "//input[@id='addressLine2']").send_keys("Mysore")
    print("Entered address line 2")
    time.sleep(1)

    driver.find_element(By.XPATH, "//input[@id='state']").send_keys("Karnataka")
    print("Entered state")
    time.sleep(1)

    driver.find_element(By.XPATH, "//input[@id='country']").send_keys("India")
    print("Entered country")
    time.sleep(1)

    driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
    print("Clicked on Add Donor")
    time.sleep(5)

#go back to donations  to select the date
    driver.find_element(By.XPATH,"//span[@class='px-1'][normalize-space()='Donations']").click()
    print("clicked on donation")
    time.sleep(10)

    driver.find_element(By.XPATH,"//a[normalize-space()='All Donations']").click()
    print("clicked on all donation")
    time.sleep(10)

#  click on calendar drop down to select date
    driver.find_element(By.XPATH,"//button[@class='relative group block bg-primary p-1 rounded']//*[name()='svg']").click() #click on calendar drop down
    time.sleep(10)
    print("clicked on calendar drop down")
    driver.find_element(By.XPATH,"//input[@id='toDateFilter']").click() #click on to date
    time.sleep(5)
    print("clicked on to date")
    driver.find_element(By.XPATH,"//input[@id='fromDateFilter']").click() #click on from date
    time.sleep(5)
    print("clicked on from date") #clicked on from date
# To select and unselect cash,online,cheque
    driver.find_element(By.XPATH,"//button[normalize-space()='Cash']").click() #to select the cash
    time.sleep(10)
    print("clicked on cash")
    driver.find_element(By.XPATH,"//button[normalize-space()='Cash']").click()   #to unselect the cash
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


#Sub organization drop down button for sorting date and check with cash,online,cheque,confirmed and unconfirmed
    driver.find_element(By.ID,"sub-org-dropdown").click()   #click on the dropdown #click on the sing sing suborg dropdown
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

    driver.find_element(By.XPATH,"//button[normalize-space()='Confirmed']").click() # un select on confirm button
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
    time.sleep(20)
    print("unselect on cheque button")

    # driver.find_element(By.ID,"sub-org-dropdown").click() #click on the dropdown
    # print("clicked on the sub organization drop down")
    # time.sleep(10)

#more action
    driver.find_element(By.ID, "donations-more-action").click()
    time.sleep(4)
    print("clicked on the more action")

#upload file button
    driver.find_element(By.XPATH,"//li[normalize-space()='Upload from file']").click() #click on upload file button
    time.sleep(4)
    print("click on file upload button")


    driver.find_element(By.ID, "cash-header").click()
    print("clicked on cash")
    time.sleep(5)
    driver.find_element(By.XPATH, "//a[normalize-space()='Click here']").click()  # download sample csv for cash
    time.sleep(3)
    print("download sample csv for cash")


    driver.find_element(By.ID, "online-header").click()
    print("clicked on online")
    time.sleep(5)

    driver.find_element(By.XPATH, "//a[normalize-space()='Click here']").click()  # download sample csv for online
    time.sleep(3)
    print("Download sample CSV for online")


    driver.find_element(By.ID, "cheque-header").click()
    print("clicked on cheque")
    time.sleep(5)
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
    # print("clicked on choose file in online")
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
#the calendar. If your sub-organization has any duplicate entries within that period, they will be displayed in the Excel which is downloaded.
    driver.find_element(By.XPATH,"//button[@class='relative group block bg-primary p-1 rounded']//*[name()='svg']").click() #click on calendar drop down
    time.sleep(10)
    print("clicked on calendar drop down")
    driver.find_element(By.XPATH,"//input[@id='toDateFilter']").click() #click on to date
    time.sleep(5)
    print("clicked on to date")
    driver.find_element(By.XPATH,"//input[@id='fromDateFilter']").click() #click on from date
    time.sleep(5)
    print("clicked on from date")


    driver.find_element(By.ID, "donations-more-action").click()
    time.sleep(4)
    print("clicked on the more action")
    driver.find_element(By.ID,"download-duplicate-button").click() #download the duplicate file for                                                                                                # 2 months in the form of Excel
    time.sleep(5)
    print("clicked on download duplicate button")

#to download 10BD

    driver.find_element(By.XPATH,"//span[@class='px-1'][normalize-space()='Donations']").click()
    print("Clicked on donation button")
    time.sleep(3)

    driver.find_element(By.XPATH, "//a[normalize-space()='All Donations']").click()
    print("clicked on all donations")
    time.sleep(10)

    driver.find_element(By.XPATH, "//input[@id='toDateFilter']").click()  # click on to date
    time.sleep(5)
    print("clicked on to date")
    driver.find_element(By.XPATH, "//input[@id='fromDateFilter']").click()  # click on from date
    time.sleep(5)
    print("clicked on from date")

    driver.find_element(By.ID, "donations-more-action").click()
    time.sleep(5)
    print("clicked on the more action")

    driver.find_element(By.ID,"//li[normalize-space()='Download 10BD']").click()
    time.sleep(5)
    print("clicked on 10BD")



#GPT search button
# GPT search button
#     driver.find_element(By.ID, "donations-more-action").click()
#     time.sleep(5)
#     print("clicked on the more action")
#     driver.find_element(By.XPATH, "//li[normalize-space()='GPTSearch']").click()
#     time.sleep(5)
#     print("clicked on gpt search")
#
#     driver.find_element(By.XPATH, "//input[@placeholder='Search with our AI integrated platform']").send_keys("Show donation for march 2024")  # entered in gpt search
#     print("entered characters")
#     time.sleep(5)
#
#     driver.find_element(By.XPATH,"//button[normalize-space()='Search']").click()  # click on search once you clicked on the content
#     time.sleep(5)
#     print("clicked on search button")



# #Click on donation button
#     driver.find_element(By.XPATH, "//span[@class='px-1'][normalize-space()='Donations']").click()
#     print("Clicked on donation button")
#     time.sleep(3)
# #click on the Alldonations
#     driver.find_element(By.XPATH,"//a[normalize-space()='All Donations']").click()
#     print("clicked on all donations")
#     time.sleep(3)

#TASK
#Task drop down
    driver.find_element(By.XPATH,"//span[@class='px-1'][normalize-space()='Tasks']").click()#click on the task drop down
    print("clicked on task dropdown")
    time.sleep(10)
    driver.find_element(By.XPATH, "//a[normalize-space()='Tasks']").click()  # click on the task button
    print("clicked on tasks")
    time.sleep(10)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")#to scroll the page down
    print("Scrolled down the page")
    time.sleep(10)

#Add a new task
    driver.find_element(By.ID,"add-task").click() #click on the add new task button
    print("clicked on add new task button")
    time.sleep(10)
    driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Auto test adding task") #enter task title
    print("Entered task title")
    time.sleep(3)
    driver.find_element(By.ID,"select-employees-list").click() #enter the Assignees
    print("Click on Assignees to select employees")
    time.sleep(10)
    driver.find_element(By.XPATH,"//select[@id='priority']").click() #select the priority
    print("click on priority")
    time.sleep(3)
    driver.find_element(By.XPATH, "//div[@class='ql-editor ql-blank']").send_keys("Complete the task which have "
                                                                                 "been assigned to you") #enter the description
    print("Entered the description")
    time.sleep(3)


    driver.find_element(By.ID, "add-task").click()  #click on add button#click on add button
    print("Click on add button")
    time.sleep(3)

    driver.execute_script("window.scrollTo(0, 0);")  # Scroll to the top
    print("Scrolled up to the top of the page")
    time.sleep(5)

#CAMPAIGN
    # campaigns button header
    driver.find_element(By.XPATH, "//span[@class='px-1'][normalize-space()='Campaigns']").click()  # click on campaign
    print("Clicked on the campaign page")
    time.sleep(5)
    driver.find_element(By.XPATH, "//a[normalize-space()='All Campaigns']").click()  # click on all campaign
    print("clicked on all campaign")
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[normalize-space()='Add Campaign']").click()  # click on add campaign
    print("clicked on add campaign")
    time.sleep(10)
    # driver.find_element(By.ID,"edit-campaign-header").click()#clicked on edit button for header
    # print("clicked on edit button for the header")
    # time.sleep(10)
    # driver.find_element(By.ID,"edit-campaign-description").click()#clicked on enter text
    # print("entered the edit-campaign-description")
    # time.sleep(10)
    # driver.find_element(By.ID, "edit-close-text").click()
    # print("click on x button")
    # time.sleep(10)
    # #driver.find_element(By.XPATH,"//button[@class='absolute top-4 text-gray-400 outline-none hover:text-gray-800 "
    #                              #"ltr:right-4 rtl:left-4 dark:hover:text-gray-600']//*[name()='svg']") #click on x button
    # #To generate AI content for header section
    # driver.find_element(By.ID, "header-edit").click()  #clicked on edit button for header#click on edit button for header
    # time.sleep(10)
    # print("click on edit button for the header")
    # driver.find_element(By.ID,"generate-text").click()#click on the generate text for AI
    # time.sleep(10)
    # print("clicked on generate text for the AI")
    # driver.find_element(By.XPATH,"//button[normalize-space()='Click to generate AI content']").click()#click on generate AI content
    # time.sleep(10)
    # print("click to generate AI content")
    # driver.find_element(By.XPATH,"//button[normalize-space()='Use this text']").click()#click on use this text button
    # time.sleep(10)
    # print("click on use this text")

    # save button

    driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
    print("clicked on save button")
    time.sleep(5)

    # Locate the input field  for category and clear existing text
    category_input = driver.find_element(By.XPATH, "//input[@value='MEDICAL']")
    category_input.clear()  # Clears the existing text "MEDICAL"
    time.sleep(2)
    # Enter new text which we want
    category_input.send_keys("test campaign")
    print("Cleared existing category and entered new category: test campaign")
    time.sleep(3)

    # locate the input field for campaign name and clear existing text
    campaign_name_input = driver.find_element(By.XPATH, "//input[@value='Campaign Name']")
    campaign_name_input.clear()
    time.sleep(2)

    # enter new text which we want
    campaign_name_input.send_keys("test")
    print("Cleared exiting campaign name and entered new campaign name: test")
    time.sleep(3)

    # locate the input field for goal amount
    goal_amount = driver.find_element(By.XPATH, "//input[@value='1000']")
    goal_amount.clear()
    time.sleep(2)
    # enter new text which we want
    goal_amount.send_keys("10000")
    print("cleared existing goal amount and entered new goal amount")

    # driver.find_element(By.XPATH,"//input[@value='MEDICAL']").send_keys("test campaign")#entered category
    # print("entered category")
    # time.sleep(6)
    #
    # driver.find_element(By.XPATH,"//input[@value='Campaign Name']").send_keys("test")#entered campaign name
    # print("entered campaign name")
    # time.sleep(5)
    # driver.find_element(By.XPATH,"//input[@value='1000']").send_keys("10000")#entered goal amount
    # print("entered goal amount")
    # time.sleep(5)
    driver.find_element(By.XPATH, "//input[@placeholder='Donation Url']").send_keys( "www.eleanorcare.ai")  # entered donation url
    print("entered donation url")
    time.sleep(5)

    driver.find_element(By.ID, "campaign-save").click()
    print("clicked on save button")
    time.sleep(10)
    #final step when we create campaign at last we will save it
    #driver.find_element(By.ID,"//button[normalize-space()='Cancel']").click()
    #print("clicked on cancel button")
    #time.sleep(5)

#EMPLOYEE
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
    random_email = f"zibra{random.randint(10000, 99999)}@gmail.com"  #random.randint(1000, 9999)
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

    driver.find_element(By.ID, "select-employee-roles").click()
    print("clicked on select roles")
    time.sleep(5)

    driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("1234569874")
    print("entered phone number")
    time.sleep(3)

    driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
    print("clicked on add button")
    time.sleep(3)
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
    driver.find_element(By.XPATH,"//button[normalize-space()='Update']").click()#clicked on update button
    print("clicked on update button")
    time.sleep(5)

#volunteers
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


#TEAM

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

#EXPENSE

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
    time.sleep(5)
    driver.find_element(By.ID,"Select-tags").click()
    print("clicked on select tags")
    time.sleep(5)

    driver.find_element(By.XPATH,"//button[normalize-space()='Add Line Item']").click()#clicked on add line item
    print("clicked on add line item")
    time.sleep(5)
    driver.find_element(By.XPATH,"//input[@id='lineItemName']").send_keys("Pencil")#entered item name
    print("entered lineitemname")
    time.sleep(5)
    driver.find_element(By.XPATH,"//textarea[@id='lineItemDescription']").send_keys("purchased the pencil")#entered line item description
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

#settings
    driver.find_element(By.XPATH,"//span[@class='px-1'][normalize-space()='Settings']").click()#clicked on settings
    print("clicked on settings")
    time.sleep(3)
    driver.find_element(By.XPATH,"//a[normalize-space()='Organization']").click()#clicked on organization
    print("clicked on organization")
    time.sleep(3)
    driver.find_element(By.ID,"setting-main").click()#clicked on main 
    print("clicked on main")
    time.sleep(3)
    driver.find_element(By.XPATH,"//button[normalize-space()='Sub Organizations']").click()#clicked on suborganization
    print("clicked on sub organization")
    time.sleep(3)
    driver.find_element(By.ID,"preferences-setting").click()
    print("clicked on preferences")
    time.sleep(10)
    driver.find_element(By.ID,"setting-razorpay-account").click()
    print("click on razorpay-account")
    time.sleep(5)
    driver.find_element(By.XPATH,"//img[@alt='userProfile']").click()#click on user profile
    print("clicked on user profile to logout")
    time.sleep(3)
    driver.find_element(By.XPATH,"//div[@class='ml-4 flex cursor-pointer flex-row !py-3 text-danger']").click()#clicked on logout
    print("clicked on logout button")
    time.sleep(3)







# Close the browser
time.sleep(5)



# Call the function
locate_by_id_demo()