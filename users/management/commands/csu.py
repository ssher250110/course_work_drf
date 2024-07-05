from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Команда для создания суперпользователя"""
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@admin.com',
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )
        user.set_password('12345')
        user.save()
