from django.contrib.auth.models import User

user = User.objects.get(is_superuser=True)
username = user.username