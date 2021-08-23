import smtplib, getpass

#Secure Connection
smtplib_object = smtplib.SMTP('smtp.gmail.com', 587)
#Check for secure connection
smtplib_object.ehlo()
#Obtain credentails
login_email = getpass.getpass('Enter your login email')
log_email_password = getpass.getpass("Enter your login password")
#Create message body
subject = input("Enter the subject : \n")
message = input("Enter the email message : \n")
to_email = input("Enter the sender email")
msg = "Subject :" + subject + "\n" + message
#Login
smtplib_object.login(login_email,log_email_password)
# Send email
smtplib_object.sendmail(login_email,to_email,msg)
