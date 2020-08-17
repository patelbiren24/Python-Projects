import smtplib  # use to sent mails
from email import encoders 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase # use for attachments
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 587) #Use smpt to find the whatever server one is using

server.starttls()  # Start the server server
me = "mailtesting624@gmail.com"
you = "bawsag@spaml.de"
#Open the file that contains the password and login using email
with open ('password.txt','r') as f:
    password = f.read()

server.login('mailtesting624@gmail.com', password)

message = MIMEMultipart() 
message['from'] = 'SampleUser' #from email
message['to'] = 'bawsag@spaml.de'
message['subject'] = 'First Email' #subject

with open ('message.txt', 'r') as f:
    message1 = f.read()

message.attach(MIMEText(message1, 'plain'))

filename = 'nature.jpeg'
attachment = open (filename, 'rb') #attach a picture to the email file

p = MIMEBase('application', 'octet-stream') #Process image data
p.set_payload(attachment.read()) #read the attachments

encoders.encode_base64(p)
p.add_header('Content-Disposition', 'attachment', filename=filename) #add the attachment
message.attach(p)

text = message.as_string()
server.sendmail(me, you, text) #send the email
