from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome('../ChromeDriver/chromedriver.exe')
browser.get(link)
browser.find_element_by_name("firstname").send_keys('Ivan')

browser.find_element_by_name("lastname").send_keys('ggg')
browser.find_element_by_name("email").send_keys('ggg@dd.yy')
browser.find_element_by_name("file").send_keys('C:\\Users\\DELL\\Documents\\PycharmProjects\\stepik\\Python_selenium\\read.me')

button = browser.find_element_by_css_selector("button[type = 'submit']")

button.click()



