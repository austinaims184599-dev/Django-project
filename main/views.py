from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Post


def home(request):
    """Home page view"""
    posts = Post.objects.all()[:5]  # Get latest 5 posts
    context = {
        'posts': posts,
        'total_posts': Post.objects.count(),
    }
    return render(request, 'main/home.html', context)


def about(request):
    """About page view"""
    return render(request, 'main/about.html')


def api_status(request):
    """Simple API endpoint for testing deployment"""
    return JsonResponse({
        'status': 'success',
        'message': 'Django deployment test is working!',
        'version': '1.0.0'
    })


@csrf_exempt
def api_posts(request):
    """API endpoint for posts"""
    if request.method == 'GET':
        posts = Post.objects.all()
        posts_data = [
            {
                'id': post.id,
                'title': post.title,
                'content': post.content,
                'created_at': post.created_at.isoformat(),
            }
            for post in posts
        ]
        return JsonResponse({'posts': posts_data})
    
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            post = Post.objects.create(
                title=data.get('title', ''),
                content=data.get('content', '')
            )
            return JsonResponse({
                'id': post.id,
                'title': post.title,
                'content': post.content,
                'created_at': post.created_at.isoformat(),
            }, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)
