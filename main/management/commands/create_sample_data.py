from django.core.management.base import BaseCommand
from main.models import Post


class Command(BaseCommand):
    help = 'Create sample data for testing'

    def handle(self, *args, **options):
        # Create sample posts
        sample_posts = [
            {
                'title': 'Welcome to Django Deployment Test',
                'content': 'This is a sample post to demonstrate the Django deployment test project. The application is working correctly and ready for deployment testing.'
            },
            {
                'title': 'API Testing',
                'content': 'This project includes REST API endpoints for testing API functionality. You can test the /api/status/ and /api/posts/ endpoints.'
            },
            {
                'title': 'Docker Support',
                'content': 'The project includes Docker configuration for containerized deployment. Use docker-compose up to run the application with PostgreSQL database.'
            },
            {
                'title': 'Production Ready',
                'content': 'This Django project is configured for production deployment with separate settings, security configurations, and environment variable support.'
            },
            {
                'title': 'Modern UI',
                'content': 'The application features a modern, responsive user interface built with Bootstrap 5 and Font Awesome icons for a professional look.'
            }
        ]

        created_count = 0
        for post_data in sample_posts:
            post, created = Post.objects.get_or_create(
                title=post_data['title'],
                defaults={'content': post_data['content']}
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created post: {post.title}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Post already exists: {post.title}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} new posts')
        )
