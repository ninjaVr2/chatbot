from django.db import models
from django.urls import reverse


class UserChatModel(models.Model):
    id = models.AutoField(
        verbose_name="ID", primary_key=True, db_column="uc_id",
    )
    name = models.TextField(verbose_name="User Name", db_column="uc_name")

    def __str__(self):
        data = self.name or ""
        info = (data[:75] + '..') if len(data) > 75 else data
        return f"{self.id}~{info}"

    def get_absolute_url(self):
        return reverse("AboutHCModel_detail", kwargs={"pk": self.pk})

    class Meta:
        managed = True
        db_table = 'cb_user'
        verbose_name = "User"
        verbose_name_plural = "Users"

    class MetaDb:
        fields = (
            'id', 'name'
        )
