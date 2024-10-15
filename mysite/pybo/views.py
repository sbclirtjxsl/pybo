from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse  # 삭제
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer


# def index(request):
#     question_list = Question.objects.order_by('-create_date')
#     context = {'question_list': question_list}
#     return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    answer.save()

    # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail', question_id=question.id)




def a01index(request):
        return render(request, 'pybo/a01index.html')
def a02data(request):
        return render(request, 'pybo/a02data.html')
def a03notice(request):
        return render(request, 'pybo/a03notice.html')
def a04CF(request):
        return render(request, 'pybo/a04CF.html')
def a05intro(request):
        return render(request, 'pybo/a05intro.html')
def a06law(request):
        return render(request, 'pybo/a06law.html')
def a07search(request):
        return render(request, 'pybo/a07search.html')
def a08login(request):
        return render(request, 'pybo/a08login.html')


# def index(request):
#     return render(request, 'pybo/index.html')

# def data_page(request):
#     return render(request, 'pybo/data.html')

# def introduction_page(request):
#     return render(request, 'pybo/introduction.html')

# def notice_page(request):
#     return render(request, 'pybo/notice.html')

# def search_page(request):
#     return render(request, 'pybo/search.html')

# def uhreff_page(request):
#     return render(request, 'pybo/uhreff.html')

# def login_page(request):
#     return render(request, 'pybo/login.html')


