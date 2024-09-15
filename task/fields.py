from typing import Any
from cryptography.fernet import Fernet

from django.db import models
from django.conf import settings

class EncryptedTextField(models.TextField):
    def __init__(self, *args, **kwargs):
        self.fernet = Fernet(settings.FERNET_KEY)
        super().__init__(*args, **kwargs)
    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        try:
            return self.fernet.decrypt(value.encode()).decode()
        except Exception:
            return value
    def get_prep_value(self, value):
        if value is None:
            return value
        try:
            return self.fernet.encrypt(value.encode()).decode()
        except Exception:
            return value