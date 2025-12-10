import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone


class QuestionModel(models.Model):
    question_text = models.CharField(max_length=200, verbose_name="问题描述", db_comment="问题描述")
    pub_date = models.DateTimeField(verbose_name="提问时间", db_comment="提问时间")

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    class Meta:
        db_table = "polls_question"
        verbose_name = '问题表'


class ChoiceModel(models.Model):
    choice_text = models.CharField(max_length=200, verbose_name="选项描述", db_comment="选项描述")
    votes = models.IntegerField(default=0, verbose_name="当前得票数", db_comment="当前得票数")
    question = models.ForeignKey(
        to=QuestionModel,
        default=None,
        related_name='choice_to_question',
        verbose_name="选项所属问题",
        db_comment="选项所属问题",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.choice_text

    class Meta:
        db_table = "polls_choice"
        verbose_name = '选项表'
