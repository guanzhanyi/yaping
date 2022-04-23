from selenium import webdriver
from selenium.webdriver.support.select import Select
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# options = ChromeOptions()
driver = webdriver.Chrome(r'E:\application\chromedriver.exe')
driver.get('https://data.eastmoney.com/gzfx/scgk.html')
total_market_value = driver.find_elements(by="xpath", value=r'//*[@id="scgz_table"]/div[2]/div[2]/table/tbody/tr/td[6]')
for mv in total_market_value:
    print(mv.text)

driver.get('https://data.eastmoney.com/cjsj/gdp.html')
total_gdp_value = driver.find_elements(by="xpath", value=r'//*[@id="cjsj_table"]/table/tbody/tr/td[2]')
for gdb in total_gdp_value:
    print(gdb.text)
driver.quit()
