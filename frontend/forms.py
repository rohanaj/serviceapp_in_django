from django.contrib.auth.forms import AuthenticationForm
from app.models import RequestList
from django import forms


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'hi',
        }
))

class RequestListForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(RequestListForm, self).__init__(*args, **kwargs)
        self.fields.queryset = Book.objects.filter(owner=self.request.user)

    class Meta:
        model = RequestList
        fields = "__all__"
