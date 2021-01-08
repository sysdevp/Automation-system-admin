# libraries to be imported 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import os
from datetime import datetime



def mail():

    fromaddr = "sysadmin@mazenetsolution.com"
    toaddr = "logeshs@fss.co.in,shinye@fss.co.in"
    #cc_add = 'uideveloper@mazenetsolution.com'
    rcpt = toaddr.split(",")

    # instance of MIMEMultipart 
    msg = MIMEMultipart() 

    # storing the senders email address 
    msg['From'] = fromaddr 

    # storing the receivers email address 
    msg['To'] = toaddr 

    #msg['Cc'] = cc_add

    # storing the subject 
    msg['Subject'] = "AWS IP details"

    # string to store the body of the mail 
    body = "Today IP details"

    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain'))

    date = datetime.now()

    today = date.strftime('%d%m%Y%H')

    filename = "{}.txt".format(today)
    print(filename)
    root = os.getcwd()

    a = []
    for filename in os.listdir(root):

        #print(filename)
        if filename.endswith('.txt'):
            #print(filename)

            if filename == "{}.txt".format(today):

                print(filename)
                a.append(filename)
    
    text_file = a[0]

    # open the file to be sent 
    attachment = open(r'C:\Users\USER\Desktop\system admin\{}'.format(text_file), "rb") 

    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 

    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 

    # encode into base64 
    encoders.encode_base64(p) 

    p.add_header('Content-Disposition', "attachment; filename= %s" % text_file) 

    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 

    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 

    # start TLS for security 
    s.starttls() 

    # Authentication 
    s.login(fromaddr, "Maze_solution@123") 

    # Converts the Multipart msg into a string 
    text = msg.as_string() 

    # sending the mail 
    s.sendmail(fromaddr, rcpt, text) 

    # terminating the session 
    s.quit() 