import smtplib
from config import Config


class Message(object):
    def __init__(self, from_address: str, 
                       to_address: str, 
                       subject: str,
                       body: str,
                       attachment_file_path: str):
        pass

class Courier(object):
    def __init__(self):
        self._config = Config()
        self._email = self._config.sender_email_address
        self._password = self._config.sender_email_password
        self._smtp_conn = smtplib.SMTP('smtp.gmail.com', 587)
        
        # secure connection with tls
        self._smtp_conn.starttls()
        
        # Authenticate smtp server connection 
        self._smtp_conn.login(self._email, self._password) 

    def send_email(self, to_address: str, 
                         subject: str,
                         body: str,
                         attachment_file_path=None):
        pass