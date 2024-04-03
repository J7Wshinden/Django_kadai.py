from typing import Any
from django.db import models
from django.urls import reverse

class Product(models.Model):
     name = models.CharField(max_length=200)###文字列の上限200
     price = models.PositiveIntegerField()###価格の用数（フィールド）を正の数で
     
     # 新規作成・編集完了時のリダイレクト先
     def get_absolute_url(self):
         return reverse('list')
