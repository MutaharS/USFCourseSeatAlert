import requests, time
from bs4 import BeautifulSoup
import smtplib, ssl

port = 465  # For SSL
password = "password"
print("This version works for Summer 2021 Classes")
crn = raw_input("Please enter the course's CRN#")
my_email = raw_input("Please enter your email: ")

message = """\
Subject: COURSE SEAT UPDATE

SEAT AVAILABLE!"""


URL = 'https://usfonline.admin.usf.edu/pls/prod/bwckschd.p_disp_detail_sched?term_in=202105&crn_in='+ crn
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

flag = 0
while(flag == 0):
    table_elems = soup.find('table', class_='datadisplaytable')
    table_data = table_elems.find_all('td', class_='dddefault')
    numSeatsAvailable = str(table_data[3])
    numSeatsAvailable = numSeatsAvailable[22:23]
    numSeatsAvailable = int(numSeatsAvailable)
    if(numSeatsAvailable > 0):
        print("THERE IS SEAT AVAILABLE!")
        # Create a secure SSL context
        context = ssl.create_default_context()
        server = smtplib.SMTP_SSL("smtp.gmail.com", port, context=context)
        server.login("courseSeatAvailable@gmail.com", password)
        server.sendmail("courseSeatAvailable@gmail.com", my_email, message)
        flag = 1
        break
    time.sleep(1)
