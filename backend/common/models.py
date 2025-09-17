from django.db import models

class CommonModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, help_text='생성 일시')
    updated_at = models.DateTimeField(auto_now=True, help_text='수정 일시')

    class Meta:
        abstract = True