from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Forms
from posts.forms import PostForm

# Models
from posts.models import Post

# Create your views here.
from django.http import HttpResponse



# 1 Retornant pàgina sense html
#def list_posts(request):
#    """List existing posts."""
#    posts = [1,2,3]
#    return(HttpResponse(str(posts)))

# 2 Sofisticant una mica més
#def list_posts(request):
#    """List existing posts."""
#    content = []
#    for post in posts:
#        content.append("""
#        <p><strong>{name}</strong></p>
#        <p><small>{user}</small></p>
#        <p><small>{timestamp}</small></p>
#        """.format(**post))
#    return(HttpResponse('<br>'.join(content)))

# 3 template
# def list_posts(request):
#     return(render(request, 'feed.html',{'name':'ana'}))

# 4 posts
@login_required
def list_posts(request):
    """List existing posts."""
    posts = Post.objects.all().order_by('-created')
    return(render(request, 'posts/feed.html',{'posts':posts}))

@login_required
def create_post(request):
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')
    else:
        form = PostForm()

    return render(request,
                    'posts/new.html',
                    {'form':form,
                    'user':request.user,
                    'profile': request.user.profile
                    }
                )
    
        