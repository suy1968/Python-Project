import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("your_email_id", "your_email_password")
 
msg = "Hi_daddy"
server.sendmail("your_email_id", "reciever_email_id", msg)
server.quit()
