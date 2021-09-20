from email.mime.text import MIMEText
import smtplib

def send_email(email, height, height_averge, count):
    from_email = "trinh3027@gmail.com"
    from_password = "******"
    to_email = email

    subject = "Height data"
    mess = "Hey there, your height is <b>%s</b>. Height average is <b>%s</b> from <b>%s</b> peple." %(height, height_averge, count)

    msg = MIMEText(mess, "html")
    msg["Subject"] = subject
    msg["To"] = to_email
    msg["From"] = from_email

    try:
        gmail = smtplib.SMTP("smtp.gmail.com", 587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login(from_email, from_password)
        gmail.send_message(msg)
        print("Send message successfully")
    except Exception as e:
        print("Error while sending email: ", e)