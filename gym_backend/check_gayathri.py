import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import UserProfile, UserLogin, DietPlanTemplate

print("=" * 80)
print("CHECKING GAYATHRI")
print("=" * 80)

# Find GAYATHRI user
user = UserLogin.objects.filter(emailid='gayathri@gmail.com').first()
if not user:
    print("❌ User not found with email: gayathri@gmail.com")
    print("\nAll users with 'gayathri' in name:")
    users = UserLogin.objects.filter(name__icontains='gayathri')
    for u in users:
        print(f"  - {u.name} ({u.emailid})")
else:
    gayathri = UserProfile.objects.filter(user=user).first()
    print(f"User: {user.name} ({user.emailid})")
    print(f"\nProfile:")
    print(f"  Goal: {gayathri.goal}")
    print(f"  Weight: {gayathri.current_weight}kg")
    print(f"  Diet Preference: {gayathri.diet_preference}")
    
    # Calculate target calories
    calc = gayathri.current_weight * 24 - 500
    print(f"  Target Calories: {calc} cal/day")
    
    print(f"\n" + "=" * 80)
    print("WEIGHT_LOSS TEMPLATES:")
    print("=" * 80)
    templates = DietPlanTemplate.objects.filter(goal_type='weight_loss').order_by('calorie_min')
    for t in templates:
        print(f"  {t.calorie_min:4d}-{t.calorie_max:4d} cal | {t.name}")
    
    print(f"\nTotal weight_loss templates: {templates.count()}")
    
    # Check matching templates
    print(f"\n" + "=" * 80)
    print(f"MATCHING TEMPLATES FOR GAYATHRI ({calc} cal):")
    print("=" * 80)
    matching = DietPlanTemplate.objects.filter(
        goal_type='weight_loss',
        calorie_min__lte=calc,
        calorie_max__gte=calc
    )
    if matching.exists():
        for t in matching:
            print(f"  ✓ {t.name} ({t.calorie_min}-{t.calorie_max})")
    else:
        print(f"  ❌ No templates match {calc} cal")
        print(f"\n  PROBLEM: {calc} cal is outside all template ranges!")
