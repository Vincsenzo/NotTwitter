from django.db import models


class Message(models.Model):
    message_content = models.CharField(max_length=500)
    time_sent = models.DateTimeField(auto_now_add=True)
    sender_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.message_content)
