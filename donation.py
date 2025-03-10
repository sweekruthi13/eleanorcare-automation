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
    time.sleep(2)

#Click on donation button
    driver.find_element(By.XPATH, "//span[@class='px-1'][normalize-space()='Donations']").click()
    print("Clicked on donation button")
    time.sleep(3)

#click on the Alldonations
    driver.find_element(By.XPATH,"//a[normalize-space()='All Donations']").click()
    print("clicked on all donations")
    time.sleep(3)

#click on Add donation to add details for cash payment
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
    #driver.find_element(By.XPATH,"//button[@id='headlessui-tabs-tab-:r8:']").click()
    #time.sleep(2)
    #print("clicked on cash")
    #driver.find_element(By.XPATH,"//button[@id='headlessui-tabs-tab-:r9:']").click()
    #time.sleep(2)
    #print("clicked on online")
    #driver.find_element(By.XPATH,"//button[@id='headlessui-tabs-tab-:ra:']").click()
    #time.sleep(2)
    #print("clicked on cheque")

#Go back to cash and enter the details
    #driver.find_element(By.XPATH, "//button[@id='headlessui-tabs-tab-:r8:']").click()
    #time.sleep(2)
    #print("clicked on cash")
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

#  click on calendar drop down to select date
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


#Sub organization drop down button for sorting date and check with cash,online,cheque,confirmed and unconfirmed
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

#more action
    driver.find_element(By.XPATH,"//button[@id='headlessui-tabs-tab-:ra:']").click()
    time.sleep(4)
    print("clicked on the more action")



#upload file button
    driver.find_element(By.XPATH,"//button[normalize-space()='Upload file']").click() #click on upload file button
    time.sleep(4)
    print("click on file upload button")


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

#GPT search button
    driver.find_element(By.XPATH,"//button[normalize-space()='GPTSearch']").click()
    time.sleep(5)
    print("clicked on gpt search")

    driver.find_element(By.XPATH,"//button[normalize-space()='Search']").click() # click on search once you clicked on the content
    time.sleep(5)
    print("clicked on search button")

    #task
#Task drop down
    driver.find_element(By.XPATH,"//a[normalize-space()='Tasks']").click()#click on the task drop down
    time.sleep(5)
    print("clicked on task dropdown")

#Add a new task
    driver.find_element(By.XPATH,"//button[@class='btn btn-primary w-full']").click() #click on the add new task button
    time.sleep(10)
    print("clicked on add new task button")

#Add task page enter details
    driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Auto test adding task") #enter task title
    time.sleep(3)
    print("Enter task title")
    driver.find_element(By.XPATH,"//div[@id='react-select-14-placeholder']").click() #enter the Assignees
    time.sleep(10)
    print("Click on Assignees")
    driver.find_element(By.XPATH,"//select[@id='priority']").click() #select the priority
    time.sleep(3)
    print("click on priority")
    driver.find_element(By.XPATH, "//div[@class='ql-editor ql-blank']").send_keys("Complete the task which have "
                                                                                 "been assigned to you") #enter the description
    time.sleep(3)
    print("Entered the description")
    driver.find_element(By.XPATH,"//button[@class='btn btn-primary ltr:ml-4 rtl:mr-4']").click()#click on add button
    time.sleep(3)
    print("Click on add button")

    #campaign

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

    #employees
# click on employees
    driver.find_element(By.XPATH, "//span[@class='px-1'][normalize-space()='Employees']").click()  # click on employees
    print("clicked on employees")
    time.sleep(5)

    # click on employees drop down
    driver.find_element(By.XPATH, "//a[normalize-space()='Employees']").click()  # clicked on drop down of employees
    print("clicked on employees from the dop down")
    time.sleep(5)
    # click on add employees
    driver.find_element(By.XPATH, "//button[normalize-space()='Add Employee']").click()  # clicked on add employees
    print("clicked on add employees")
    time.sleep(5)
    driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys("zibra")  # entered first name
    print("entered first name")
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys("black")  # entered last name
    print("entered last name")
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='email']").send_keys("zibra@gmail.com")  # entered email
    print("entered email")
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("1234")  # entered password
    print("entered password")
    time.sleep(3)
    # driver.find_element(By.XPATH,"").click()#clicked on select roles
    # print("clicked on select roles")
    # time.sleep(5)
    driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("1234569874")  # entered phone number
    print("entered phone number")
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()  # clicked on add button
    print("clicked on add button")
    time.sleep(3)

    #volunteers

# Close the browser
time.sleep(5)



# Run the function
locate_by_id_demo()