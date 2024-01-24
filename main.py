# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Import Service class for Selenium 4 or later
from selenium.webdriver.common.by import By
# imports current date and time so that script can look out 3 day
import datetime

current_date = datetime.date.today()  # Get current date
target_date = current_date + datetime.timedelta(days=3)  # Add 3 days
target_date_text = target_date.strftime("%b %d")  # Format as "Dec 23"

# Construct the absolute path to the driver
driver_path = r"C:\Users\matt0\PycharmProjects\Courtbot\drivers\chromedriver.exe"  # Replace with the exact path if needed

# Use Service class for Selenium 4 or later
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Navigate to the login page
driver.get("https://www.pwyc.com/login.aspx")

# Find the username and password fields
username_field = driver.find_element(By.ID, "p_lt_ContentWidgets_pageplaceholder_p_lt_zoneContent_CHO_Widget_LoginFormWithFullscreenBackground_XLarge_loginCtrl_BaseLogin_UserName")
username_field.send_keys("username") # Enter your username

password_field = driver.find_element(By.ID, "p_lt_ContentWidgets_pageplaceholder_p_lt_zoneContent_CHO_Widget_LoginFormWithFullscreenBackground_XLarge_loginCtrl_BaseLogin_Password")
password_field.send_keys("password") # Enter your password

# Find the login button and submit the form
login_button = driver.find_element(By.ID, "p_lt_ContentWidgets_pageplaceholder_p_lt_zoneContent_CHO_Widget_LoginFormWithFullscreenBackground_XLarge_loginCtrl_BaseLogin_LoginButton")
login_button.click()

# After logging in, navigate to the CourtScheduler page
court_scheduler_url = "https://www.pwyc.com/Courts/CourtScheduler"
driver.get(court_scheduler_url)

# constructs the path for the date 3 days out
#date_xpath = f"//div[@class='div date ng-binding' and text()='{target_date_text}']"
# date_xpath = //*[@id="form1"]/div[3]/div[1]/div/div/div/div[3]/div/div[2]/div/div/div/div[5]/div[2] and text()='{target_date_text}']"

# finds and clicks this date element to select the date 3 days out
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Example using Slick's API:
driver.execute_script("$('.slick-slider').slick('slickGoTo', 2);")  # Go to the 3rd slide

#wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
#date_element = wait.until(EC.element_to_be_clickable((By.XPATH, date_xpath)))
#date_element.click()

input("Press Enter to close the browser...")

