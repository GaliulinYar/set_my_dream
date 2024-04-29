from django.core.management import BaseCommand
from django.db.utils import IntegrityError
from users.models import User


class Command(BaseCommand):
    """Комманда для создания супер юзера -python manage.py csu- """

    def handle(self, *args, **options):
        """Добавляем админа"""
        try:
            user = User.objects.create(
                email='yaroslav66@list.ru',
                first_name='Admin',
                last_name='тут фамилия наверное',
                is_staff=True,
                is_superuser=True,
            )

            user.set_password('qwerty')
            user.save()
            print('Super User complete')

        except IntegrityError as e:
            print('Такой пользователь уже есть')

