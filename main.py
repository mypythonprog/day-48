from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)


bot = webdriver.Chrome(options=chrome_options)
bot.get("https://www.youtube.com")