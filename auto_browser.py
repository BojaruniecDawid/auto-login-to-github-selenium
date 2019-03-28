# automatization process to  sign in to github .

from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://github.com")

signin_link =  browser.find_element_by_link_text("Sign in")
signin_link.click()

username_box = browser.find_element_by_id("login_field")
username_box.send_keys("LoginHere")

password_box = browser.find_element_by_id("password")
password_box.send_keys("PasswordHere")
password_box.submit()


# first way to check if that user is signed in .
# assert "LoginHere" in browser.page_source

# second way / more specific.
profile_link = browser.find_element_by_class_name("user-profile-link")
link_label = profile_link.get_attribute("innerHTML")
assert "LoginHere" in link_label
