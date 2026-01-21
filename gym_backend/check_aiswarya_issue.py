import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import UserLogin, UserProfile, DietPlanTemplate

# Check both Aiswarya users
users = UserLogin.objects.filter(name='Aiswarya')
print(f"Found {users.count()} users named 'Aiswarya'\n")

for user in users:
    print(f"USER ID: {user.id} | Email: {user.emailid}")
    try:
        profile = UserProfile.objects.get(user=user)
        print(f"  Current: {profile.current_weight}kg -> Target: {profile.target_weight}kg")
        print(f"  Goal: {profile.goal}")
        print(f"  Months: {profile.target_months}")
        
        # Calculate target calories
        calc_result = profile.calculate_target_calories()
        target_calories = calc_result['target_calories']
        print(f"  Target Calories: {target_calories}")
        
        # Check matching templates
        templates = DietPlanTemplate.objects.filter(
            goal_type=profile.goal,
            calorie_min__lte=target_calories,
            calorie_max__gte=target_calories
        )
        print(f"  Matching templates: {templates.count()}")
        for t in templates:
            print(f"    - {t.name} ({t.calorie_min}-{t.calorie_max} cal)")
        
    except UserProfile.DoesNotExist:
        print("  No profile found")
    
    print()

print("\n" + "="*60)
print("ALL WEIGHT_GAIN TEMPLATES:")
print("="*60)
templates = DietPlanTemplate.objects.filter(goal_type='weight_gain').order_by('calorie_min')
for t in templates:
    print(f"{t.calorie_min}-{t.calorie_max} cal | {t.name}")
print(f"\nTotal: {templates.count()} templates")
