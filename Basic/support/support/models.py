from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Faq(models.Model):
    CATEGORY_CHOICES=(
        ('GE','General'),
        ('AC','Account'),
        ('ET','Et cetera')
    )

    question = models.TextField(verbose_name='질문')
    category = models.CharField(verbose_name='카테고리', max_length=2,  choices=CATEGORY_CHOICES)
    reply = models.TextField(verbose_name='답변')
    creator = models.TextField(verbose_name='생성자')
    created_at = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)
    final_corr = models.TextField(verbose_name='최종 수정자')
    final_corr_at = models.DateTimeField(verbose_name='최종 수정일시', auto_now_add=True)
    