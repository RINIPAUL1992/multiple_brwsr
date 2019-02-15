from selenium import webdriver

browser='ie'
if browser=='chrome':
    driver=webdriver.Chrome()
elif browser=='ie':
    driver=webdriver.Ie(executable_path="G:\Downloads\IEDriverServer_Win32_3.14.0\IEDriverServer.exe")
elif browser=='ff':
    driver=webdriver.Firefox(executable_path="G:\Downloads\geckodriver-v0.24.0-win64\geckodriver.exe")

driver.get("https://www.facebook.com/")
driver.maximize_window()