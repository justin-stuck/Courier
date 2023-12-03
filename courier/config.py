import os


class Config:
    @property
    def sender_email_address(self) -> str:
        return os.environ['sender_email_address']

    @property
    def sender_email_password(self) -> str:
        return os.environ['sender_email_password']
