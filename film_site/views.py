from django.db.models import Avg
from django.shortcuts import render
from django.utils import timezone

from film_site.models import Category, Film, Review, UserProfile
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from film_site.forms import UserForm, UserProfileForm, ReviewForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime


def index(request):
    film_list = Film.objects.order_by('-name')[:5]
    toprated = Film.objects.order_by('-rating')[:10]

    context_dict = {}




    context_dict['films'] = film_list
    context_dict['toprated'] = toprated
    context_dict['boldmessage'] = 'High rated films'

    visitor_cookie_handler(request)
    response = render(request, 'film_site/index.html', context=context_dict)
    return response


def show_film(request, film_name_slug):
    context_dict = {}
    try:
        film = Film.objects.get(slug=film_name_slug)
        samecategory = Film.objects.filter(category=film.category)
        curfilmreviews = Review.objects.filter(film=film)
        avgrating = Review.objects.filter(film=film).aggregate(Avg('rating'))
        film.views = film.views + 1
        if avgrating['rating__avg'] != None:
            film.rating = float(avgrating['rating__avg'])
        film.save()

        context_dict['film'] = film
        context_dict['avgrating'] = avgrating
        context_dict['reviews'] = curfilmreviews
        context_dict['similar_films'] = samecategory
    except Film.DoesNotExist:
        context_dict['avgrating'] = None
        context_dict['film'] = None
        context_dict['reviews'] = None
        context_dict['similar_films'] = None
    return render(request, 'film_site/film.html', context=context_dict)


def show_film_genre(request, choice):
    context_dict = {}
    try:
        category = Category.objects.get(category=choice)
        catname = category.get_category_display
        catFilms = Film.objects.filter(category=category.category)
        catFilms = catFilms.order_by('name')
        topFilms = catFilms.order_by('-views')[:5]

        context_dict['category'] = category
        context_dict['catFilms'] = catFilms
        context_dict['catname'] = catname
        context_dict['topFilms'] = topFilms
    except Film.DoesNotExist:
        context_dict['category'] = None
        context_dict['catFilms'] = None
        context_dict['catname'] = None
    return render(request, 'film_site/Genre.html', context=context_dict)


def show_trending(request):
    context_dict = {}
    try:

        recentreviews = Review.objects.order_by('-review_time')[:5]
        trendingfilms = Film.objects.filter(id__in=recentreviews.values_list('film__id', flat=True))[::-1]

        context_dict['recentreviews'] = recentreviews
        context_dict['trendingfilms'] = trendingfilms

    except Film.DoesNotExist:
        context_dict['recentreviews'] = None
        context_dict['trendingfilms'] = None

    return render(request, 'film_site/Trending.html', context=context_dict)


def add_review(request, film_name_slug):
    try:
        film = Film.objects.get(slug=film_name_slug)


    except film.DoesNotExist:
        film = None
        # You cannot add a page to a Category that does not exist...
    if film is None:
        return redirect(reverse('filmsite:index'))
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            if film:
                review = form.save(commit=False)
                review.film = film
                review.reviewer = request.user

                review.save()
                film.reviews = film.reviews + 1

                film.save()
                return redirect(reverse('film_site:show_film',
                                        kwargs={'film_name_slug':
                                                    film_name_slug}))
    else:
        print(form.errors)

    context_dict = {'form': form, 'film': film}
    return render(request, 'film_site/add_review.html', context=context_dict)


def register(request):
    registered = False
    if request.method == 'POST':

        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.email = user.email
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()

        profile_form = UserProfileForm()

    return render(request, 'film_site/register.html', context={'user_form': user_form,
                                                               'profile_form': profile_form,
                                                               'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('film_site:index'))
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print(f"Invalid login details: {username},{password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'film_site/login.html')


@login_required
def Account(request):
    context_dict = {}
    currentuser = UserProfile.objects.get(user=request.user)
    useremail = currentuser.email
    userpic = currentuser.picture
    Accountreviews=Review.objects.filter(reviewer=request.user)

    context_dict['currentuser'] = currentuser
    context_dict['useremail'] = useremail
    context_dict['userpic'] = userpic
    context_dict['Accountreviews'] = Accountreviews
    return render(request, 'film_site/Account.html', context=context_dict)


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('film_site:index'))


def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val


def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],
                                        '%Y-%m-%d %H:%M:%S')
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:

        request.session['last_visit'] = last_visit_cookie
    request.session['visits'] = visits


def contact_us(request):
    visitor_cookie_handler(request)
    response = render(request, 'film_site/contact_us.html')
    return response
