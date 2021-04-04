from django import forms
from django.forms import EmailInput

from film_site.models import Page, Category, UserProfile, Film, Review
from django.contrib.auth.models import User


# class CategoryForm(forms.ModelForm):
#     name = forms.CharField(max_length=Category.NAME_MAX_LENGTH,
#                            help_text="Please enter the category name")
#     views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
#     likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
#     slug = forms.CharField(widget=forms.HiddenInput(), required=False)
#
#     class Meta:
#         model = Category
#         fields = ('name',)


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=Page.TITLE_MAX_LENGTH,
                            help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200,
                         help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page

        exclude = ('category',)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data['url'] = url

        return cleaned_data


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
