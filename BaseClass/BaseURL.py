class BaseUrl:

    def setUpClass(cls):
    driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
    driver.maximize_window()
