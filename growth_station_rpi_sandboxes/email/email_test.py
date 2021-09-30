import smtplib

sender = 'indoor_farm@line-explorer.com'
receivers = ['giovanni.vincenti@gmail.com']

message = """From: From Person <indoor_farm@line.explorer.com>
To: To Person <giovanni.vincenti@gmail.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""

try:
    email_server = smtplib.SMTP('mail.line-explorer.com', 26)
    email_server.login('indoor_farm@line-explorer.com', 'learningCommons001')
    email_server.sendmail(sender, receivers, message)
except smtplib.SMTPException as ex:
    print("Error sending email")
    print(ex)
