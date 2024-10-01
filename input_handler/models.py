# input_handler/models.py

from django.db import models

class LogEntry(models.Model):
    client_ip = models.GenericIPAddressField()
    user_input = models.TextField()
    is_sql_injection = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_ip} - {self.user_input} - {'SQL Injection' if self.is_sql_injection else 'Safe'}"
