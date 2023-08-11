from enum import Enum
from django.db import models
from django.urls import reverse
from chat.models.users.main import UserChatModel


class Sender(Enum):
    USER = 1
    BOT = 2


class ConversationChatModel(models.Model):
    id = models.AutoField(
        verbose_name="ID", primary_key=True, db_column="cc_id",
    )
    trailId = models.ForeignKey(
        "ConversationChatModel",
        verbose_name="Trail",
        db_column="cc_trail",
        on_delete=models.CASCADE,
        null=True,
        related_name="Conversation_Chat_Model_trailId",
    )
    user = models.ForeignKey(
        UserChatModel, 
        verbose_name="User", 
        db_column="cc_user",
        on_delete=models.CASCADE,
        null=True,
        related_name="Conversation_Chat_Model_user",
    )
    sender = models.CharField(
        max_length=255,
        choices=[(color.value, color.name) for color in Sender],
    )
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        data = self.name or ""
        info = (data[:75] + '..') if len(data) > 75 else data
        return f"{self.id}~{info}"

    def get_absolute_url(self):
        return reverse("AboutHCModel_detail", kwargs={"pk": self.pk})

    class Meta:
        managed = True
        db_table = 'cb_conversations'
        verbose_name = "Conversation"
        verbose_name_plural = "Conversations"

    class MetaDb:
        fields = (
            'id', 'trailId', 'user', 'sender', 'message', 'timestamp'
        )

