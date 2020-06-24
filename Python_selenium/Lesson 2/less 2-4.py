from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome('../ChromeDriver/chromedriver.exe')
browser.get(link)
x = int(browser.find_element_by_id('input_value').text)
x = calc(x)
input = browser.find_element_by_id('answer')
input.send_keys(str(x))
browser.find_element_by_id('robotCheckbox').click()
browser.execute_script("window.scrollBy(0, 200);")
browser.find_element_by_id('robotsRule').click()
button = browser.find_element_by_css_selector("button[type = 'submit']")

button.click()



