import datetime

from django.db import models
from django.utils import timezone

#�Q�̃��f���́C�������django.db.models.Model�̃T�u�N���X
#�ǂ���������̃N���X�ϐ��������C�X�̃N���X�ϐ��̓��f���̃f�[�^�x�[�X�t�B�[���h��\�����Ă���D
#�e�t�B�[���h��Field�N���X�̃C���X�^���X�Ƃ��ĕ\������Ă���D

#question_text�ƁCpub_date�Ƃ���������CQuestion�Ƃ������f��
#��1�����ŁC���O��t���邱�Ƃ��ł���D
#�ȉ��ł�pub_date�ɁCdate published�Ƃ������O��t���Ă���D
#CharField�́Cmax_length�Ƃ������͂��K�{�̈���������D
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= now - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

#ForeignKey�ŁCQuestion�Ƃ̊֌W���`
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
