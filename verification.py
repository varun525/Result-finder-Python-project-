import smtplib
email=input("enter your email:")
sender_email="jhakvarun1999@gmail.com"
reciever_email=email
password="Varun1999"
list3=[]
list4=[]
list2=["a","e","i","o","u"]
for i in range(len(email)):
    list3.append(email[i])
for item in list3:
    if item in list2:
        list4.append(item)
sum=""
for item in list4:
    sum=sum+item
message= "Your paasword is: " + sum
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,password)
server.sendmail(sender_email,reciever_email,message)
print("paasword sent! CHECK YOUR EMAIL")