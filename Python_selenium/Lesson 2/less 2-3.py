from selenium import webdriver
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome('../ChromeDriver/chromedriver.exe')
browser.get(link)
x = int(browser.find_element_by_id('num1').text)
y = int(browser.find_element_by_id('num2').text)
sel = Select(browser.find_element_by_id('dropdown'))
sel.select_by_value(str(x+y))
browser.find_element_by_css_selector("button[type = 'submit']").click()



