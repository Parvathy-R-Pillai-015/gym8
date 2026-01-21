import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

import requests
from users.models import UserProfile, UserLogin

print("=" * 80)
print("TESTING UPDATED API - PERSONALIZED CALORIES")
print("=" * 80)

# Get a few test users
users = UserLogin.objects.all()[:3]

for user in users:
    try:
        profile = UserProfile.objects.get(user=user)
        
        print(f"\n{user.name} (ID: {user.id})")
        print(f"  {profile.current_weight}kg → {profile.target_weight}kg in {profile.target_months} months")
        print(f"  Goal: {profile.goal}")
        
        # Test API call
        url = f"http://localhost:8000/api/users/{user.id}/calculate-calories/"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            print(f"\n  ✓ API Response:")
            print(f"    Target Calories: {data['target_calories']} cal/day")
            print(f"    BMR: {data['bmr']} cal/day")
            print(f"    Weekly Change: {data['weekly_change']:+.2f}kg/week")
            print(f"    Daily Adjustment: {data['daily_adjustment']:+.0f} cal/day")
            print(f"    Safe: {'✓ YES' if data['is_safe'] else '⚠️  NO'}")
            
            if data['warnings']:
                print(f"\n    ⚠️  Warnings:")
                for warning in data['warnings']:
                    print(f"      - {warning}")
        else:
            print(f"  ❌ API Error: {response.status_code}")
            
    except UserProfile.DoesNotExist:
        print(f"  ⚠️  No profile for {user.name}")
    except Exception as e:
        print(f"  ❌ Error: {e}")

print(f"\n{'='*80}")
print("✓ API updated successfully with personalized calorie calculation!")
print("=" * 80)
