from django.shortcuts import render, HttpResponse

from .models import Post

# Create your views here.
def posts(request):
    blogs = Post.objects.all()
    return render(request, 'blogs.html') 

def post(request, id):
    blog = Post.objects.get(id=id)
    contenido = f'{blog.titulo} - {blog.descripcion}'
    return render(request, 'blog.html') 
