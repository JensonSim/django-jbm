#UTF-8
from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html',{'posts': posts})
# Create your views here.
#render함수에는 매개변수 request(사용자가 요청하는 모든 것)와 'blog/post_list.html' 템플릿이 있습니다. {}이 보일 텐데, 이곳에 템플릿을 사용하기 위해 매개변수를 추가할 거에요. (이 매개변수를'posts'라고 할거에요){'posts': posts}이렇게 작성할거에요. :이전에 문자열이 와야하고, 작은 따옴표''를 양쪽에 붙이는 것을 잊지 마세요.
