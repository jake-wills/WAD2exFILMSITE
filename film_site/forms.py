from django import forms
from django.forms import EmailInput

from film_site.models import Page, Category, UserProfile# Film
from django.contrib.auth.models import User



class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=Category.NAME_MAX_LENGTH,
                           help_text="Please enter the category name")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)

# class FilmForm(forms.ModelForm):
#     name = forms.CharField(max_length=Film.NAME_MAX_LENGTH,
#                            help_text="Please enter the film name")
#     bio = forms.CharField(max_length=Film.BIO_MAX_LENGTH,
#                           help_text="Please enter the film Bio" )
#     director = forms.CharField(max_length=Film.NAME_MAX_LENGTH,
#                                help_text="Please enter the director name")
#     rating = forms.IntegerField(default=0)
#     reviews = forms.IntegerField(default=0)
#     slug = forms.CharField(widget=forms.HiddenInput(), required=False)
#
#     class Meta:
#         model = Category
#         fields = ('name', 'picture', 'bio', 'director')
#
#

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


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)




class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)