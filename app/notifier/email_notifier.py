import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailNotifier:
    def __init__(self):
        self.sender_email = "educai.hackathon@gmail.com"

        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        self.smtp_username = "educai.hackathon@gmail.com"
        self.smtp_password = "cjawvvqlmltkkcft"

    def notify(self, receiver_email: str, subject: str, message: str):
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.smtp_username, self.smtp_password)
            server.sendmail(self.sender_email, receiver_email,
                            msg.as_string())

            print("Email sent successfully")
        except Exception as e:
            print("Error sending email:", str(e))
        finally:
            server.quit()
