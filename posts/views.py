from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#utilities
from datetime import datetime

#creamos una variable global para la prueba

posts = [
    {
        'name': 'Mont Blanc',
        'user': 'Yésica Cortés',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture':'picture'
    },
    {
        'name': 'BUAAAA Blanc',
        'user': 'Yésica Cortés',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture':'picture'
    },
    {
        'name': 'MERDAAAA Blanc',
        'user': 'Yésica Cortés',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture':'picture'
    },
  ]

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
    return(render(request, 'posts/feed.html',{'posts':posts}))
        