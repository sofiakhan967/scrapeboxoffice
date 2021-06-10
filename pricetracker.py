import requests
from bs4 import BeautifulSoup
import smtplib
def check_price():
    url = "https://www.amazon.in/ASUS-VivoBook-i3-1005G1-Integrated-X415JA-EK092TS/dp/B08JMR2GXG/ref=sr_1_2?dchild=1&qid=1623089426&refinements=p_89%3AASUS&rnid=3837712031&s=computers&sr=1-2"
    headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
    page=requests.get(url , headers=headers)
    soup= BeautifulSoup(page.content , 'html.parser')
    title=soup.find(id="productTitle").get_text() # grab product title 
    price=soup.find(id="priceblock_ourprice").get_text() # grab product price
    converted_price=price[1:8]# grab price exclude rupee symbol 


    #print(converted_price)
    #print(title.strip())
    if converted_price < '30,000': # both argument should be string 
        send_mail()
#send email when price drop 
def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('your email id','your pswd')
    subject="hURRAAYYYY buy new ASUS  "
    body="Check this amazon link ASUS price DROP!!!! \n https://www.amazon.in/ASUS-VivoBook-i3-1005G1-Integrated-X415JA-EK092TS/dp/B08JMR2GXG/ref=sr_1_2?dchild=1&qid=1623089426&refinements=p_89%3AASUS&rnid=3837712031&s=computers&sr=1-2 "
    msg=f"subject : {subject} \n\n {body} "
    server.sendmail('your email id' , 'recievers email id ' , msg)

    print("EMAIL HAS BEEN SENT....")
    server.quit()

check_price()        