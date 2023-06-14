from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#utilities
from datetime import datetime

#creamos una variable global para la prueba

posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    }
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
        