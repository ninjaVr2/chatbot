from enum import Enum
from django.db import models

from chatbot.mchatbot.chat.models.users.main import UserChatModel

class Sender(Enum, int):
    user = ("User", 1)
    bot = ("Bot", 2)
    
class ConversationChatModel(models.Model):
    id = models.AutoField(verbose_name="User ID", db_column="cc_id")
    user = models.ForeignKey(UserChatModel, verbose_name="User", db_column="cc_user")
    sender = models.CharField(
        max_length=255,
        choices=[(color.value, color.name) for color in Sender],
    )
    message = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
