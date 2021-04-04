from django import forms
from django.forms import EmailInput

from film_site.models import Category, UserProfile, Film, Review
from django.contrib.auth.models import User



class ReviewForm(forms.ModelForm):

    rating = forms.IntegerField(max_value=5, min_value=0, help_text="Please enter a score between 0 and 5",required=True)
    reviewtext = forms.CharField(max_length=500, help_text="Enter your Review",)

    class Meta:
        model = Review

        exclude = ('reviewer', 'film')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),required=True)
    email = forms.EmailField(widget=forms.EmailInput(),required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)
