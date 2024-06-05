from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def blog(request):
    print('blog')

    context = {
        'text' : 'chave valor do blog'
    }

    return render(request,'blog/index.html',context)

def exemplo(request):
    print("acessou o exemplo")

    context = {
        'text' : 'pega esse exemplo fela',
        'title': 'parte exemplo - '
    }

    return render(request,'blog/exemplo.html',context)