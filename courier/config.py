import os


class Config(object):
    @property
    def sender_email_address(self):
        return os.environ['sender_email_address']

    @property
    def sender_email_password(self):
        return os.environ['sender_email_password']
