from django import forms
from .models import GuestPost

class GuestPostForm(forms.ModelForm):
    class Meta:
        model = GuestPost
        fields = ('user', 'guestbook', 'post', 'picture')
        widgets = {'user': forms.HiddenInput(), 'guestbook': forms.HiddenInput()}

class PostForm(forms.Form):
    #user = forms.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='posts')
    #trip = forms.ForeignKey(Trip, on_delete=models.CASCADE, null=True, related_name='posts')
    #photo = forms.ForeignKey(Photo, on_delete=models.SET_NULL, null=True, related_name='posts') 
    comment = forms.CharField(label='comment', max_length=300, widget=forms.Textarea)
    reaction=forms.CharField(label='reaction', ) 
    #date_created = forms.DateTimeField(auto_now_add=True)