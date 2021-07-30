import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sendmail(receiver, message_template, message_text, mail_subject, smtp, sender_email, password):

    message = MIMEMultipart("alternative")
    message["Subject"] = mail_subject
    message["From"] = sender_email
    message["To"] = receiver["email"]

    # Turn the templates into plain/html MIMEText objects
    part1 = MIMEText(message_text, "plain")
    part2 = MIMEText(message_template, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp, 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver["email"], message.as_string()
        )

    print("\n\t[+] Email sent successfully to", receiver["email"])
