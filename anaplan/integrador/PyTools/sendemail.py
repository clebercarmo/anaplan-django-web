import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

def sendEmail(subject="Anaplan Status Non Defined",status="Unspecified Error"):
    #receivers="paolovm@gmail.com,marcia_borges@fornodeminas.com.br"
    receivers="cleber.carmo@fornodeminas.com.br;rcleber@outlook.com.br"

    sender = 'anaplan@fornodeminas.com.br'
    password = 'Fdm1nf0rm4t1c4@2020'

    #sender = 'fdmplanning@gmail.com'
    #password = 'Fdmpla2021'
  
    port=1025
    port = 465 
    context = ssl.create_default_context()

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receivers
    msg.attach(MIMEText(status))

#    with smtplib.SMTP('localhost', port) as server:


    with smtplib.SMTP_SSL("mail.fornodeminas.com.br", port, context=context) as server:
        try:

            server.login("anaplan", password)
            server.sendmail(sender, receivers, msg.as_string())
            print(status)
            print("Successfully sent email")
        except Exception as err:
            print(err)

    


if __name__ == '__main__':
    sendEmail()

