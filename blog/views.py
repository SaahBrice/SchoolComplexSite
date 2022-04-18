from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from blog.models import Admission,Teacher_applications, Sitemessages, article, Schoolinfos, Form1_applications, Form2_4_applications, Lowersixth_applications, Class1_applications, Class2_6_applications, Nursery_applications
from blog.forms import PostForm,Teacher_applicationForm,  SchoolinfosForm, Form1_applicationsForm, Form2_4_applicationForm, LowerSixth_applicationForm, Class1_applicationForm, Class2_6_applicationForm, Nursery_applicationForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
# Create your views here.

def index(request):
    new_articles = article.objects.all()
    new_articles =new_articles[::-1]
    context = {
    'new_articles': new_articles,
    }
    return render(request, 'blog/index.html', context)
@login_required()
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post_item = form.save(commit=False)
            post_item.save()
            messages.success(request, "Post Added Successfully!")
            return redirect('posts')
        else:
            messages.error(request, "Unable to add post!")

    else:
        form=PostForm()
    return render(request, 'principal/add_post.html', {'form':form})

@login_required()
def schoolinfos(request):
    item = get_object_or_404(Schoolinfos, id = 1)
    form = SchoolinfosForm(request.POST or None, instance = item)
    if form.is_valid():
        form.save()
        messages.success(request, "Infos Updated Successfully")
        return redirect("schoolinfos")
    return render(request, 'principal/schoolinfos.html', {'form':form})

@login_required()
def posts(request):
    new_posts = article.objects.all()
    new_posts = new_posts[::-1]
    context ={
    'new_posts': new_posts
    }
    return render(request, 'blog/posts.html', context)

def why(request):
    return render(request, 'blog/why-ZHS.html')


def preschool(request):
    return render(request, 'blog/preschool.html')

def primaryschool(request):
    return render(request, 'blog/primaryschool.html')


def secondaryschool(request):
    return render(request, 'blog/secondaryschool.html')

def schoolprogram(request):
    return render(request, 'blog/schoolprogram.html')


def news(request):
    articles = article.objects.all()
    articles = articles[::-1]
    context = {
    'articles':articles,
    }
    return render(request, 'blog/news.html', context)
@login_required()
def view_post(request, article_id):
    S_article = article.objects.get(id = article_id)
    context = {
    'S_article': S_article,
    }
    return render(request, 'blog/view_post.html', context)

@login_required()
def delete_new_post(request, post_id):
    S_article = article.objects.get(id = post_id)
    S_article.delete()
    messages.success(request, "Post deleted successfully")
    return redirect('posts')
@login_required()
def edit_new_post(request, post_id):
    item = get_object_or_404(article, id = post_id)
    form = PostForm(request.POST or None, instance = item)
    if form.is_valid():
        form.save()
        messages.success(request, "Post Updated Successfully")
        return redirect("posts")
    return render(request, 'principal/update_post.html', {'form':form})

@login_required()
def view_message(request, sitemessage_id):
    message = Sitemessages.objects.get(id = sitemessage_id)
    message.read = True
    message.save()
    context = {
    'message': message,
    }
    return render(request, 'blog/sitemessage.html', context)


@login_required()
def all_messages(request):
    messages = Sitemessages.objects.all()
    messages = messages[::-1]
    return render(request, 'blog/all_messages.html', {'messages':messages})



def admission(request):
    return render(request, 'blog/admission.html')


def contact(request):
    return render(request, 'blog/contact.html')

def registration(request):
    return render(request, 'blog/registration.html')

def openhours(request):
    return render(request, 'blog/openhours.html')

def sitemessages(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        content = request.POST.get('content')
        new_message = Sitemessages()
        new_message.name = name
        new_message.message = content
        new_message.save()
        messages.success(request, "You message has been send successfully")
        return redirect('index')
    else:
        messages.error(request, "Your message could not be send, try again later.")


def form1_application(request):
    if request.method == 'POST':
        form = Form1_applicationsForm(request.POST, request.FILES)
        if form.is_valid():
            post_item = form.save(commit=False)
            post_item.save()
            messages.success(request, "Application submitted Successfully!")
            return redirect('thankyou')
        else:
            messages.error(request, "Unable to appy!")

    else:
        form=Form1_applicationsForm()
    return render(request, 'blog/apply.html', {'form':form})

def Form2_4_application(request):
    if request.method == 'POST':
        form = Form2_4_applicationForm(request.POST, request.FILES)
        if form.is_valid():
            post_item = form.save(commit=False)
            post_item.save()
            messages.success(request, "Application submitted Successfully!")
            return redirect('thankyou')
        else:
            messages.error(request, "Unable to appy!")

    else:
        form=Form2_4_applicationForm()
    return render(request, 'blog/apply.html', {'form':form})

def LowerSixth_application(request):
    if request.method == 'POST':
        form = LowerSixth_applicationForm(request.POST, request.FILES)
        if form.is_valid():
            post_item = form.save(commit=False)
            post_item.save()
            messages.success(request, "Application submitted Successfully!")
            return redirect('thankyou')
        else:
            messages.error(request, "Unable to appy!")

    else:
        form=LowerSixth_applicationForm()
    return render(request, 'blog/apply.html', {'form':form})

def Class1_application(request):
    if request.method == 'POST':
        form = Class1_applicationForm(request.POST, request.FILES)
        if form.is_valid():
            post_item = form.save(commit=False)
            post_item.save()
            messages.success(request, "Application submitted Successfully!")
            return redirect('thankyou')
        else:
            messages.error(request, "Unable to appy!")

    else:
        form=Class1_applicationForm()
    return render(request, 'blog/apply.html', {'form':form})

def Class2_6_application(request):
    if request.method == 'POST':
        form = Class2_6_applicationForm(request.POST, request.FILES)
        if form.is_valid():
            post_item = form.save(commit=False)
            post_item.save()
            messages.success(request, "Application submitted Successfully!")
            return redirect('thankyou')
        else:
            messages.error(request, "Unable to appy!")

    else:
        form=Class2_6_applicationForm()
    return render(request, 'blog/apply.html', {'form':form})

def Nursery_application(request):
    if request.method == 'POST':
        form = Nursery_applicationForm(request.POST, request.FILES)
        if form.is_valid():
            post_item = form.save(commit=False)
            post_item.save()
            messages.success(request, "Application submitted Successfully!")
            return redirect('thankyou')
        else:
            messages.error(request, "Unable to appy!")

    else:
        form=Nursery_applicationForm()
    return render(request, 'blog/apply.html', {'form':form})

def Teacher_application(request):
    if request.method == 'POST':
        form = Teacher_applicationForm(request.POST, request.FILES)
        if form.is_valid():
            post_item = form.save(commit=False)
            post_item.save()
            messages.success(request, "Application submitted Successfully!")
            return redirect('thankyou')
        else:
            messages.error(request, "Unable to appy!")

    else:
        form=Teacher_applicationForm()
    return render(request, 'blog/apply.html', {'form':form})



def thankyou(request):
    return render(request, 'blog/thankyou.html')

@login_required()
def view_applications(request):
    teachers = Teacher_applications.objects.all()
    teachers = teachers[::-1]
    form1s = Form1_applications.objects.all()
    form1s = form1s[::-1]
    otherforms = Form2_4_applications.objects.all()
    otherforms = otherforms[::-1]
    lowersixths = Lowersixth_applications.objects.all()
    lowersixths = lowersixths[::-1]
    class1s = Class1_applications.objects.all()
    class1s = class1s[::-1]
    otherclasses = Class2_6_applications.objects.all()
    otherclasses = otherclasses[::-1]
    nurseries = Nursery_applications.objects.all()
    nurseries = nurseries[::-1]
    context = {
    'teachers':teachers,
    'form1s':form1s,
    'otherforms':otherforms,
    'lowersixths':lowersixths,
    'class1s':class1s,
    'otherclasses':otherclasses,
    'nurseries':nurseries,
    }
    return render(request, 'principal/view_applications.html', context)

@login_required()
def l6_app_view(request, l6_id):
    l6 = Lowersixth_applications.objects.get(pk = l6_id)
    return render(request, 'principal/l6.html', {'l6':l6})

@login_required()
def l6_app_accept(request, l6_id):
    l6 = Lowersixth_applications.objects.get(pk = l6_id)
    l6.Approved = True
    l6.save()
    messages.success(request, "Accepted successfully")
    return redirect('view_applications')

@login_required()
def f1_app_view(request, f1_id):
    f1 = Form1_applications.objects.get(pk = f1_id)
    return render(request, 'principal/f1.html', {'f1':f1})

@login_required()
def f1_app_accept(request, f1_id):
    f1 = Form1_applications.objects.get(pk = f1_id)
    f1.Approved = True
    f1.save()
    messages.success(request, "Accepted successfully")
    return redirect('view_applications')

@login_required()
def f2_4_app_view(request, l6_id):
    f1 = Form2_4_applications.objects.get(pk = l6_id)
    return render(request, 'principal/f2_4.html', {'f1':f1})

@login_required()
def f2_4_app_accept(request, l6_id):
    l6 = Form2_4_applications.objects.get(pk = l6_id)
    l6.Approved = True
    l6.save()
    messages.success(request, "Accepted successfully")
    return redirect('view_applications')

@login_required()
def c2_6_app_view(request, f1_id):
    f1 = Class2_6_applications.objects.get(pk = f1_id)
    return render(request, 'principal/c2_6.html', {'f1':f1})

@login_required()
def c2_6_app_accept(request, f1_id):
    f1 = Class2_6_applications.objects.get(pk = f1_id)
    f1.Approved = True
    f1.save()
    messages.success(request, "Accepted successfully")
    return redirect('view_applications')

@login_required()
def c1_app_view(request, f1_id):
    f1 = Class1_applications.objects.get(pk = f1_id)
    return render(request, 'principal/c1.html', {'f1':f1})

@login_required()
def c1_app_accept(request, f1_id):
    f1 = Class1_applications.objects.get(pk = f1_id)
    f1.Approved = True
    f1.save()
    messages.success(request, "Accepted successfully")
    return redirect('view_applications')

@login_required()
def n_app_view(request, f1_id):
    f1 = Nursery_applications.objects.get(pk = f1_id)
    return render(request, 'principal/n.html', {'f1':f1})

@login_required()
def n_app_accept(request, f1_id):
    f1 = Nursery_applications.objects.get(pk = f1_id)
    f1.Approved = True
    f1.save()
    messages.success(request, "Accepted successfully")
    return redirect('view_applications')

@login_required()
def t_app_view(request, f1_id):
    f1 = Teacher_applications.objects.get(pk = f1_id)
    return render(request, 'principal/t.html', {'f1':f1})

@login_required()
def t_app_accept(request, f1_id):
    f1 = Teacher_applications.objects.get(pk = f1_id)
    f1.Approved = True
    f1.save()
    messages.success(request, "Accepted successfully")
    return redirect('view_applications')
