from django.db import models


class UserChatModel(models.Model):
    id = models.AutoField(verbose_name="User ID", db_column="uc_id")
    name = models.TextField(verbose_name="User Name", db_column="uc_name")
