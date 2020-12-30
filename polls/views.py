from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

#genericを使うことで，簡単に作れる．
#template_name='~~~'とするだけでどのhtmlをテンプレートとするか定義できる

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    #https://www.366service.com/jp/qa/3775b1b0b603e605b44e8747afbf26c5
    #context_object_nameで指定された文字列で，template内の'object_list'を置き換える
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    #ListViewへの，モデル指定方法は３つ
    #1. model = Question
    #2. queryset = Question.objects.all()
    #3. defget_queryset(self):
    #       return Question.objects.all()
    #今回は，Questionモデルの中の，日が新しい5つのクエリセットのみを取り出す
    #1だと，Questionの全てをクエリセットに入れてしまう
    #2だと，Viewが最初に呼び出された際の状態を維持してしまう．
    #3ならば動的に，表示可能
    #なので3の方法を使っている．
    #以下に，ListViewについて詳しく書いてある．
    #https://hombre-nuevo.com/python/python0057/



class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        #https://stackoverflow.com/questions/2048777/what-is-choice-set-in-this-django-app-tutorial
        #↑ choice_setがどこから来たのかの説明
        #request.POSTは，送信したデータを取ってくる操作
        #name="choice"のデータを取ってきて，その値（id）を取ってくる
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # selected_choiceのvotesを1インクリメントして，polls:resultsが示すurlに飛ばす
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))