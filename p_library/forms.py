from django import forms  
from p_library.models import Book, Friend
  
class FriendForm(forms.ModelForm):  
    full_name = forms.CharField(widget=forms.TextInput)
    class Meta:  
        model = Friend  
        fields = '__all__'

class BookForm(forms.ModelForm):  
    title = forms.CharField(widget=forms.TextInput)
    friends = forms.ModelChoiceField(queryset=Friend.objects.all(), label='Должник', required=False)
    class Meta:  
        model = Book  
        fields = '__all__'

class BookFriendForm(forms.ModelForm):  
    title = forms.CharField(widget=forms.TextInput, label='Название книги', max_length=100, disabled=True)
    description = forms.CharField(widget=forms.Textarea, label='Описание', required=False, disabled=True)
    friends = forms.ModelChoiceField(queryset=Friend.objects.all(), label='Должник', required=False)
    class Meta:  
        model = Book  
        fields = ['title', 'description', 'friends']