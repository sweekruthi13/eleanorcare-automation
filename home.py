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


#click on the home button
    driver.find_element(By.XPATH,"//div[normalize-space()='Home']").click() # click on home button
    time.sleep(5)
    print("clicked on the home button")

#click on the features button in features click on several options to navigate to particular session
    driver.find_element(By.XPATH,"//a[@class='menu-link']//div[contains(text(),'Features')]").click()
                                                #clicked on features
    time.sleep(5)
    print("clicked on features")

    driver.find_element(By.XPATH,"//body/div[@id='wrapper']/header[@id='header']/div[@id='header-wrap']/div[@class='container']"
                                 "/div[@class='header-row']/nav[@class='primary-menu with-arrows primary-menu-init']/ul[@class='menu-container']"
                                 "/li[@class='menu-item mega-menu sub-menu menu-item-hover']/div[@class='mega-menu-content"
                                 " mega-menu-style-2 px-0']/div[@class='container']/div[@class='row']/a[1]/div[1]").click()
                                    #navigate to particular session called features
    time.sleep(10)
    print("clicked on features donation management")

    driver.find_element(By.XPATH,"//a[@class='menu-link']//div[contains(text(),'Features')]").click()
                                                #clicked on features
    time.sleep(5)
    print("clicked on features")

#click on the contact button
    driver.find_element(By.XPATH,"//div[normalize-space()='Contact']").click()
    time.sleep(10)
    print("click on the contact button")

#Home page to ask for the demo
    driver.find_element(By.XPATH,"//div[normalize-space()='Home']").click()
    time.sleep(5)
    print("click on home page to click on as for demo")

    driver.find_element(By.XPATH,"//input[@id='contactform-name']").send_keys("Testing")
    time.sleep(5)
    print("entered name for demo session")

    driver.find_element(By.XPATH,"//input[@id='contactform-email']").send_keys("testing@gmail.com")
    time.sleep(5)
    print("entered email for the demo session")

    driver.find_element(By.XPATH,"//input[@id='contactform-phone']").send_keys("1234561232")
    time.sleep(5)
    print("entered phone number")

#click on the Ask for the demo
    driver.find_element(By.XPATH,"//button[@id='demo-button']").click()
    time.sleep(10)
    print("clicked on i want a demo")



# Close the browser
time.sleep(5)




# Run the function
locate_by_id_demo()