#加载固定版本ChromeDriver
browser_path=r'C:/Users/.../browser/chrome.exe'
driver_path=r'C:/.../driver/chromedriver.exe'
options = webdriver.ChromeOptions()
options.binary_location = browser_path
browser = webdriver.Chrome(driver_path, options=options)
