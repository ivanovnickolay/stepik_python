from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome('../ChromeDriver/chromedriver.exe')
browser.get(link)
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
browser.find_element_by_id('book').click()
browser.execute_script("window.scrollBy(0, 500);")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x = int(browser.find_element_by_id('input_value').text)
x = calc(x)
input = browser.find_element_by_id('answer')
input.send_keys(str(x))
browser.find_element_by_css_selector("button[type = 'submit']").click()


