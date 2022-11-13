#!/usr/bin/env python
# coding: utf-8

# In[1]:


import smtplib
from email.message import EmailMessage

def sendMail(receiver, subject, message):
    print ("Your Email is composing. Please wait..")

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo() #Authentication
    server.starttls() #Authentication
    server.ehlo() #Authentication

    server.login("...............@gmail.com"," please enter use App password 16 digit code")
   #server.login("###########@gmail.com","password")
    
    mail=EmailMessage()
    mail["From"]="pererasn93@gmail.com"
    mail["To"]=receiver
    mail["Subject"]=subject
    mail.set_content(message)

    server.send_message(mail)
    server.close()
    print("Email sent successfully to ",receiver,"\n")

#sendMail("","testing message 1","This is a testing")
sendMail("vihangakaushan1122@gmail.com","testing message 1","This is a testing")


# In[ ]:




