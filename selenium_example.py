from selenium import webdriver


driver = webdriver.Firefox()
driver.get("https://www.hackerrank.com/raj61")
assert "Raj" in driver.title
elem = driver.find_element_by_id("hacker-contest-score")
print (elem.text)
