import random
import smtplib

server=smtplib.SMTP('smtp.gmail.com',587)
#adding TLS security 
server.starttls()
server.login("reachylimited@gmail.com","okqtubxhisupwlew")
#generate OTP using random.randint() function
otp=''.join([str(random.randint(0,9)) for i in range(6)])
msg='Hello, Your OTP is '+str(otp)
sender='reachylimited@gmail.com'  #write email id of sender
receiver='kvsharsha.2000@gmail.com' #write email of receiver
#sending
server.sendmail(sender,receiver,msg)
server.quit()