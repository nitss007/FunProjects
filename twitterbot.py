from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd

chromedriver_path = '/home/nisharma/Downloads/chromedriver_linux64(1)/chromedriver' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://twitter.com/login')
sleep(10)

username = webdriver.find_element_by_name('session[username_or_email]')
username.send_keys('youemailid')
password = webdriver.find_element_by_name('session[password]')
password.send_keys('your password')


button_login = webdriver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/form/div/div[3]/div")
#button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(3) > button')
sleep(3)
button_login.click()
sleep(3)


#prev_user_list = list(prev_user_list[0])

new_followed = []
tag = -1
followed = 0
likes = 0
comments = 0
hashtag_list = [str(randint(10000000,90000000))]  #'75279282',
prev_user_list = []
pHolderList = ["", "[1]"]
for hashtag in hashtag_list:
    tag += 1
    webdriver.get('https://twitter.com/i/connect_people?user_id='+hashtag)

    for pHolder in pHolderList:
        try:
            for x in range(4, 33):
                try:
                    follow = "/html/body/div/div/div/div[2]/main/div/div/div/div"+str(pHolder)+"/div/div[2]/section/div/div/div/div["+ str(x)+ ']/div/div/div/div[2]/div[1]/div[2]/div/div/span/span'
                    # If we already follow, do not unfollow
                    sleep(6)
                    if webdriver.find_element_by_xpath(follow).text == 'Follow':
                        webdriver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div"+str(pHolder)+"/div/div[2]/section/div/div/div/div["+ str(x)+ "]/div/div/div/div[2]/div[1]/div[2]/div").click()

                        new_followed.append(username)
                        followed += 1
                except Exception as e:
                    print(str(e))

# some hashtag stops refreshing photos (it may happen sometimes), it continues to the next
        except Exception as e:
           print(str(e))

for n in range(0,len(new_followed)):
    prev_user_list.append(new_followed[n])
    
#updated_user_df = pd.DataFrame(prev_user_list)
#updated_user_df.to_csv('{}_users_followed_list.csv'.format(strftime("%Y%m%d-%H%M%S")))
print('Followed {} new people.'.format(followed))
