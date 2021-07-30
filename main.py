import read_data, send_mail

#The url of API for the shopfy store, which can be obtained from the shopify admin page Apps/Manage Private Apps
url = 'yourshopifyAPIurl'

#The sender mail credentials
smtp = 'smtp.gmail.com'
sender_email = "example@gmail.com"
password = "password"

mail_subject = "Sent from Python"

#Returns the user content in form of Pandas Dataframe
df = read_data.get_dataframe(url)

for i in range(0, len(df)+1):
#Determines the receiver of the message
    receiver = df.iloc[i]

    # Gets the body of the mail through the created template (txt file and html)
    message_html = read_data.read_html_template('template.html')
    message_text = read_data.read_text_template('template.txt')

    # Send the mail to the receiver
    send_mail.sendmail(receiver, message_html, message_text, mail_subject, smtp, sender_email, password)