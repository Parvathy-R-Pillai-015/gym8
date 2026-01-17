import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import UserLogin

# Check if user exists
user = UserLogin.objects.filter(emailid='krishna@gmail.com').first()

if user:
    print(f"User found!")
    print(f"ID: {user.id}")
    print(f"Username: {user.name}")
    print(f"Email: {user.emailid}")
    print(f"Password (stored): {user.password}")
    print(f"Role: {user.role}")
else:
    print("User not found")

# List all users
print("\nAll users in database:")
for u in UserLogin.objects.all():
    print(f"  - {u.name} ({u.emailid}) - Role: {u.role}")
