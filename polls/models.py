import datetime

from django.db import models
from django.utils import timezone

#２つのモデルは，いずれもdjango.db.models.Modelのサブクラス
#どちらも複数のクラス変数を持ち，個々のクラス変数はモデルのデータベースフィールドを表現している．
#各フィールドはFieldクラスのインスタンスとして表現されている．

#question_textと，pub_dateという列をもつ，Questionというモデル
#第1引数で，名前を付けることができる．
#以下ではpub_dateに，date publishedという名前を付けている．
#CharFieldは，max_lengthという入力が必須の引数がある．
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

#ForeignKeyで，Questionとの関係を定義
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
