import smtplib

var = smtplib.SMTP("smtp.gmail.com", 587)
var.ehlo()
var.starttls()
var.login("kshitijkhandelwal3009@gmail.com",)
var.sendmail("kshitijkhadelwal3009@gmail.com","kshitijkhadelwal3009@gmail.com","Subject: python \n\n Body: testing python automation \n \n - kshitij")
