from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome('../ChromeDriver/chromedriver.exe')
browser.get(link)
browser.find_element_by_css_selector("button[type = 'submit']").click()
browser.switch_to.window(browser.window_handles[1])
x = int(browser.find_element_by_id('input_value').text)
x = calc(x)
browser.find_element_by_id('answer').send_keys(str(x))
browser.find_element_by_css_selector("button[type = 'submit']").click()