from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys


recipients = ['ykara1626@gmail.com']
emaillist = [elem.strip().split(',') for elem in recipients]
msg = MIMEMultipart()
msg['From'] = 'raspberryinf@gmail.com'
msg['Reply-to'] = 'ykara1626@gmail.com'
 
msg.preamble = 'Multipart massage.\n'
 
part = MIMEText("Merhaba, Kapınızdaki kişinin fotografi ektedir")
msg.attach(part)
 
part = MIMEApplication(open(str(sys.argv[2]),"rb").read())
part.add_header('Content-Disposition', 'attachment', filename=str())
msg.attach(part)


server = smtplib.SMTP("smtp.gmail.com:587")
server.ehlo()
server.starttls()
server.login('raspberryinf@gmail.com','5379954192')
 
server.sendmail(msg['From'], emaillist , msg.as_string())
