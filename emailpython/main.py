import smtplib
from email.mime.text import MIMEText

msg = MIMEText('This is test mail')
msg['Subject'] = 'Test Email'
msg['From'] = 'labautomation7@gmail.com'
msg['To'] = 'abbaskashan234@gmail.com'

try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('labautomation7@gmail.com', 'zibbgfbonagebwxd')
        server.sendmail('labautomation7@gmail.com', 'abbaskashan234@gmail.com', msg.as_string())
        print("Email sent successfully!")
except Exception as e:
    print("Failed to send email:", e)