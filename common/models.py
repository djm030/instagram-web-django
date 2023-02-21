from django.db import models

# Create your models here.


class CommonModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # DB에 추가 하지 않는다.
