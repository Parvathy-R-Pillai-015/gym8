import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import UserLogin, UserProfile, UserDietPlan

# Check dinju's diet plan
users = UserLogin.objects.filter(name__icontains='dinju')
print(f"Found {users.count()} users matching 'dinju'\n")

for user in users:
    print(f"USER: {user.name} (ID: {user.id}) | Email: {user.emailid}")
    
    try:
        profile = UserProfile.objects.get(user=user)
        print(f"  Goal: {profile.goal}")
        print(f"  Current: {profile.current_weight}kg -> Target: {profile.target_weight}kg")
        print(f"  Months: {profile.target_months}")
        
        # Check for diet plans
        diet_plans = UserDietPlan.objects.filter(user=user)
        print(f"  Diet Plans: {diet_plans.count()}")
        
        for plan in diet_plans:
            print(f"    - Plan ID: {plan.id}")
            print(f"      Created: {plan.created_at}")
            print(f"      Template: {plan.template.name if plan.template else 'None'}")
            print(f"      Calories: {plan.template.calorie_min}-{plan.template.calorie_max} cal" if plan.template else "")
        
    except UserProfile.DoesNotExist:
        print("  No profile found")
    
    print()
