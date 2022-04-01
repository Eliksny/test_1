from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

        # 필드를 저렇게 정의할 수도 있지만 exclude = ('post', 'author', 'created_at', 'modified_at')으로 정의할 수도 있다.