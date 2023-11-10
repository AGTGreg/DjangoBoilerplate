from django.core.management import call_command
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Creates an admin user non-interactively if it doesn't exist"

    def add_arguments(self, parser):
        parser.add_argument('--username', help="Admin's username")
        parser.add_argument('--email', help="Admin's email")
        parser.add_argument('--password', help="Admin's password")

    def handle(self, *args, **options):
        print("Starting app for the first time...")
        print("="*100)
        print("Running database migrations")
        call_command('migrate')
        print("="*100)
        print("Creating cache")
        call_command('createcachetable')
        print("="*100)
        print("Creating super user")
        User = get_user_model()

        username = options['username'] if options['username'] else 'admin'
        email = options['email'] if options['email'] else 'admin@example.com'
        password = options['password'] if options['password'] else 'admin'
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )

        print("Done!")
