import smtplib
from .config import Config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class Message(object):
    def __init__(self, from_address: str, 
                       to_address: str, 
                       subject: str,
                       body: str,
                       attachment_file_path=None):
        self.msg = MIMEMultipart()
        self.msg['From'] = from_address  
        self.msg['To'] = to_address
        self.msg['Subject'] = subject
        self.msg.attach(MIMEText(body, 'plain'))
        if attachment_file_path:
            with open(attachment_file_path, 'rb') as attachment:
                base = MIMEBase('application', 'octet-stream')
                base.set_payload((attachment).read())
                encoders.encode_base64(base)
                base.add_header('Content-Disposition', "attachment; filename= {}".format(attachment_file_path))
                self.msg.attach(base)

    @property
    def text(self):
        return self.msg.as_string()

class Courier(object):
    def __init__(self, connect=False):
        self._config = Config()
        self._email = self._config.sender_email_address
        self._password = self._config.sender_email_password
        # TODO add logging

    def connect(self):
        # start smtp session
        self._smtp_conn = smtplib.SMTP('smtp.gmail.com', 587)
        
        # secure connection with tls
        self._smtp_conn.starttls()
        
        # Authenticate smtp server connection 
        self._smtp_conn.login(self._email, self._password) 

    def disconnect(self):
        # quit smtp session if connection exists
        if self._smtp_conn:
            self._smtp_conn.quit()

    def send_email(self, to_address: str, 
                         subject: str,
                         body: str,
                         attachment_file_path=None):
        #TODO gracefully handle and log connection issues
        self.connect()
        try:
            message = Message(self._email,
                            to_address,
                            subject,
                            body,
                            attachment_file_path).text
            self._smtp_conn.sendmail(self._email, to_address, message)
        except Exception as e:
            RuntimeError("Failed to send email. Exception message: {}".format(str(e)))
        finally:
            self.disconnect()

