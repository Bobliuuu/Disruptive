import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from undetected_chromedriver import Chrome, ChromeOptions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

# CHROME 114 is required

def get_company_about(company_name, linkedin_url):

    SECRETUSER = "msmirsaj@edu.uwaterloo.ca" # Put linkedin email here
    SECRETPASS = "mekqe8-bozFof-nupquq" # Put linkedin password
    ignored_exceptions=(NoSuchElementException,StaleElementReferenceException)

    debug_mode = True
    options = ChromeOptions()
    
    if not debug_mode: options.add_argument("--headless=new") # Run Chrome in headless mode without opening a browser window
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36")

    driver = Chrome(options=options)
    
    # driver.get("https://www.linkedin.com/login")
    # element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
  
    # email_elem = driver.find_element(By.ID,"username")
    # email_elem.send_keys(SECRETUSER)
  
    # password_elem = driver.find_element(By.ID,"password")
    # password_elem.send_keys(SECRETPASS)
    # password_elem.submit()
    
    # time.sleep(10) # 10 seconds to do bot test
    
    # driver.get(linkedin_url)
    # time.sleep(2)
    
    # # Get the HTML source of the page
    # html_source = driver.page_source

    # # Create a BeautifulSoup object to parse the HTML
    # soup = BeautifulSoup(html_source, 'html.parser')

    # # Find the target div and extract all the text
    # description_div = soup.find('div', class_='org-about-module__description')
    # spans = description_div.find_all('span', class_='lt-line-clamp__line')

    # # Extract and print the text content of each span
    # for span in spans:
    #     print(span.get_text())

    # # If you want to concatenate all the span text into a single string:
    # all_text = ' '.join(span.get_text() for span in spans)
    # print(all_text)
    
    # #################
    # # driver.get("https://www.linkedin.com/company/infosys/")
    # # time.sleep(2)
    # # html_source = driver.page_source

    # #  # Create a BeautifulSoup object to parse the HTML
    # # soup = BeautifulSoup(html_source, 'html.parser')

    # # # Find the target div and extract all the text
    # # description_div = soup.find('div', class_='org-about-module__description')
    # # spans = description_div.find_all('span', class_='lt-line-clamp__line')

    # # # Extract and print the text content of each span
    # # for span in spans:
    # #     print(span.get_text())

    # # # If you want to concatenate all the span text into a single string:
    # # all_text = ' '.join(span.get_text() for span in spans)
    # # print(all_text)
    
    
    
    # description = driver.find_element(By.CLASS_NAME,"org-about-module__description")
    
    # time.sleep(10)
    # WebDriverWait(driver, 10,ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.NAME, 'session_key')))

    # # Find the username and password input elements and fill in the values
    # username_element = driver.find_element(By.NAME, 'session_key')
    # password_element = driver.find_element(By.NAME, 'session_password')

    # # Replace 'your_username' and 'your_password' with the actual values
    # username_element.send_keys(SECRETUSER)
    # password_element.send_keys(SECRETPASS)
    
    # password_element.send_keys(Keys.RETURN)
    
    # driver.find_element(By.CSS_SELECTOR, 'button[class="sign-in-modal__outlet-btn cursor-pointer btn-md btn-primary"].btn-primary').click()


if __name__ == "__main__":
    url = "https://www.linkedin.com/company/facebook/"
    name = "Facebook"
    get_company_about(name, url)