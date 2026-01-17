import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import UserProfile

# Check all profiles
print("All user profiles:")
for profile in UserProfile.objects.all():
    print(f"\nUser ID: {profile.user.id}")
    print(f"Name: {profile.user.name}")
    print(f"Mobile: {profile.mobile_number}")
    print(f"Age: {profile.age}")
    print(f"Payment Status: {profile.payment_status}")
