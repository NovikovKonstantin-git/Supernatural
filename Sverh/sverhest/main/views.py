from django.shortcuts import render, Http404, HttpResponse, get_object_or_404, redirect
from .models import Creatures, Category, Nichego, Comments
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, F
from django.db.models import Q
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm, CommentForm
from django.contrib.auth import login, logout


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'main/login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')


def index(request):
    search_query = request.GET.get('search', '')

    if search_query:
        articles_creatures = Creatures.objects.filter(title__icontains=search_query)
    else:
        articles_creatures = Creatures.objects.all()

    paginator = Paginator(articles_creatures, 3)
    page = request.GET.get('page', 1)
    page_objects = paginator.get_page(page)

    context = {
        'articles_creatures': articles_creatures,
        'title': 'Сверхъестественное',
        'page_obj': page_objects,
    }

    return render(request, 'main/index.html', context, )


def get_category(request, category_id):

    articles_creatures = Creatures.objects.filter(category_id=category_id)
    # articles_creatures = Creatures.objects.filter(title='title')
    # count_artic = Creatures.objects.all()

    category = Category.objects.get(pk=category_id)
    paginator = Paginator(articles_creatures, 3)
    page = request.GET.get('page', 1)
    page_objects = paginator.get_page(page)
    return render(request, 'main/category.html', {'articles_creatures': articles_creatures,
                                                  'category': category, 'page_obj': page_objects, })


def view_articles(request, articles_id):

    # articles_item = Creatures.objects.get(pk=articles_id)
    articles_item = get_object_or_404(Creatures, pk=articles_id)
    comments = articles_item.comments_creatures.all()
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.article_id = articles_item.id

            # Save the comment to the database
            new_comment.author_id = request.user.pk
            new_comment.save()

            comment_form = CommentForm()
            return redirect(articles_item)
    else:
        comment_form = CommentForm()

    return render(request, 'main/view_articles.html', {"articles_item": articles_item, "comment_form": comment_form, "comments": comments, })


def home_page_one(request):
    return render(request, 'main/home_page_one.html', )


def photo_gallery(request):

    photo = Creatures.objects.all()

    paginator = Paginator(photo, 4)
    page = request.GET.get('page', 1)
    page_objects = paginator.get_page(page)

    context = {
        'photo': photo,
        'page_obj': page_objects,
    }
    return render(request, 'main/photo_gallery.html', context, )


