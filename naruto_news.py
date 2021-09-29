from selenium import webdriver
import time
import smtplib

my_email = ENTER YOUR EMAIL HERE 
my_password = ENTER YOUR PASSWORD HERE
to_address = ENTER A VALID EMAIL HERTE TO SEND MAIL TO

CHROME_DRIVER=("C://Users/Carlo/desktop/Development/chromedriver.exe")
driver = webdriver.Chrome(CHROME_DRIVER)
driver.maximize_window()

driver.get('https://www.reddit.com/')
insert_text = driver.find_element_by_id("header-search-bar")
time.sleep(2)
insert_text.send_keys("naruto")
time.sleep(3)
# find_community = driver.find_element_by_xpath('//*[@id="SearchDropdownContent"]/a[1]')
time.sleep(2)
submit_form = driver.find_element_by_class_name("_1DeR7_QiQnu2UK0e2dDfYD")
time.sleep(3)
submit_form.submit()

time.sleep(3)
naruto_community_link = driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div/div[2]/div[1]/div/a')
naruto_community_link.click()

time.sleep(2)
newest_status = driver.find_element_by_tag_name("h3").text

print(newest_status)

time.sleep(2)
driver.close()

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr = my_email,
                    to_addrs = to_address, 
                    msg = "Subject:Reddit Naruto Community\n\n"
                    f"Hey Carlos, the Naruto community is now talking about '{newest_status}'.")

