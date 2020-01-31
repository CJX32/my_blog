from django.shortcuts import render,redirect
from blog.models import Post
from blog.models import Comment,Post
from django.core.mail import EmailMessage
# Create your views here.

def main(request):
    state = 'blog'
    blogs = Post.objects.all()
    return render(request,'index.html',locals())

def contact(request):
    state = 'contact'
    if request.method == 'POST':
        try:
            visitor_name = request.POST['nickname']
            comment = request.POST['comment']
            try:
                post = Comment.objects.get(nickname=visitor_name,comment=comment)
                if post:
                    repeat = 'repeat'
            except:
                post = Comment.objects.create(nickname=visitor_name, comment=comment)
                mail_body = u'''
                昵称：{}
                留言：{}
                '''.format(visitor_name,comment)
                email = EmailMessage('网站留言',mail_body,'meteorskysun@gmail.com',['meteorskysun@outlook.com'])
                email.send()
                if visitor_name != None:
                    send = 'send'
        except:
            pass
    return render(request,'contact.html',locals())

def post(request,url):
    disable = 'able'
    if request.method == 'POST':
        try:
            like = request.POST['like']
        except:
            if 'like' in request.session:
                like = request.session['like']
                disable = 'disable'
    else:
        if 'like' in request.session:
            like = request.session['like']
            disable = 'disable'
    try:
        request.session['like'] = like
    except:
        pass
    try:
        p = Post.objects.get(url = url)
        if like == 'like' and disable != 'disable':
            p.like = p.like + 1
            p.save()
        elif like == 'unlike' and disable != 'disable':
            p.like = p.like - 1
            p.save()
    except:
        pass
    try:
        p = Post.objects.get(url = url)
        print("blog"+str(p.pk)+".html")
        return render(request,"blog"+str(p.pk)+".html",locals())
    except:
        return redirect('/main')
