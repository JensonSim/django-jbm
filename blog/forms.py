from django import forms
# 장고 모듈에서 폼을 불러온다 써야되니까
from .models import Post
# 그리고 저장을 위해서 모델파일안에 포스트 클래스를 불러온다.
class PostForm(forms.ModelForm):
    #PostForm 은 이미 다들 예상 하셨듯이 우리가 만들 폼의 이름이에요. 그리고 장고에 이 폼이 ModelForm이라는 것을 알려줘야해요.
    class Meta:
        #이 폼을 만들기 위해서 어떤 model이 쓰여야 하는지 장고에 알려주는 구문입니다.
        model = Post
        fields = ('title','text',)

        
