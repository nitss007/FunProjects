#PRICE ALERT FOR AMAZON and SENDING MAIL and PUSH NOTIFICATION
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import requests,time,smtplib
from bs4 import  BeautifulSoup
from notify_run import Notify
from datetime import datetime
#USER INPUT-----------but I make it comment because I want to be specific to this product.
'''
url = input("Enter your URL here : ")
dp = int(input("Enter your desired price : "))
'''
#-----------------------------------------------
url = "https://www.amazon.in/gp/product/B077GYR3XD?pf_rd_p=649eac15-05ce-45c0-86ac-3e413b8ba3d4&pf_rd_r=S36SQNZYXB84HCV3C9EX"
dp = 2949
URL = url
pnmsg = "Below Rs. "+str(dp)+" you can get your Phillips Trimmmer."
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
 
def check_price():
 
  page = requests.get(URL, headers=headers)
  soup= BeautifulSoup(page.content,'html.parser')
  #----------------------------------------------------- TO CHECK WHETHER soup IS WORKING OR NOT
  #'''
  m=open('soupw.txt',"wb")
  m.write(soup.prettify().encode("utf-8"))
  m.close
  #'''
  #--------------------------------------------------------------------------------------
  title = soup.find(id="productTitle").get_text()
  price = soup.find(id="priceblock_ourprice").get_text()
  main_price = price[2:]
  #LETS MAKE IT AN INTEGER---------------------------------------------------------------
  l = len(main_price)
  if l<=6 :
      main_price = price[2:5]
  else:
      p1 =  price[2]
      p2 =  price[4:7]
      pf = str(p1)+str(p2)
      main_price = int(pf)
     
  price_now = int(main_price)
  #VARIABLES FOR SENDING MAIL AND PUSH NOTIFICATION---------------------------------------
  title1=str(title.strip())
  main_price1 = main_price
  print("NAME : "+ title1)
  print("CURRENT PRICE : "+ str(main_price1))
  print("DESIRED PRICE : "+ str(dp))
  #-----------------------------------------------Temporary fixed for values under Rs.  9,999
  #FUNCTION TO CHECK THE PRICE-------------------------------------------------------
 
  count = 0
  if(price_now <= dp):
     send_mail()
     push_notification()
  else:
     count = count+1
  print("Rechecking... Last checked at "+str(datetime.now()))
 
#Lets send the mail-----------------------------------------------------------------
def send_mail():
#  server = smtplib.SMTP('smtp.gmail.com',587)
#  server.ehlo()
#  server.starttls()
#  server.ehlo()
#  server.login('nitss007@gmail.com','fzanpwfvxnldiycv')
#  subject = "Price of Phillips Trimmer has fallen down below Rs. "+str(dp)
#  msg = f"Subject: {subject} \n\n {body} "
#  server.sendmail(
#  'nitss007@gmail.com',
#  '28sharmanitish@gmail.com',
#  msg
#  )


    gmail_user = 'nitss007@gmail.com'
    gmail_password = 'whukouaezfqnjcee'

    sent_from = gmail_user
    to = ['28sharmanitish@gmail.com', 'sans1337@yahoo.com']
    subject = "Price of Phillips Trimmer has fallen down below Rs. "+str(dp)
    body = "Hey Nitish! \n The price of Phillips trimmer on AMAZON has fallen down below Rs."+str(dp)+".\n So, hurry up & check the amazon link right now : "+url
   # email_text = """From: hello@hello.com
   # To: nitss007@gmail.com\n
   # Subject: <Subject goes here>\n
   # Here's my message!\nIt is lovely!
   # """
    email_text = 'Subject: {}\n\n{}'.format(subject, body)
   #email_text = """\
   # From: %s 
   # To: %s 
   # Subject: %s \n
   # %s
   # """ % (sent_from, ", ".join(to), subject, body)
    
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
    except:
        print('Something went wrong...')

    print("HEY Bro, EMAIL HAS BEEN SENT SUCCESSFULLY.")
 
    server.quit()
#Now lets send the push notification-------------------------------------------------
def push_notification():
  notify = Notify()
  notify.send(pnmsg)
  print("HEY Bro, PUSH NOTIFICATION HAS BEEN SENT SUCCESSFULLY.")
 
  print("Check again after an hour.")
#Now lets check the price after 1 min ----------------------------------------------- 
count = 0
while(True):
  count += 1
  print("Count : "+str(count))
  check_price()
  time.sleep(3600)
#but demonstration purpose I entered 5 instead of 3600 in line no 111
