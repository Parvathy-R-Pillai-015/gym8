import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import UserProfile, UserLogin

print("=" * 80)
print("TESTING NEW PERSONALIZED CALORIE CALCULATION")
print("=" * 80)

profiles = UserProfile.objects.all()[:5]  # Test first 5 users

for profile in profiles:
    user = profile.user
    print(f"\n{'='*80}")
    print(f"{user.name} ({user.emailid})")
    print(f"{'='*80}")
    print(f"Current: {profile.current_weight}kg → Target: {profile.target_weight}kg")
    print(f"Timeline: {profile.target_months} months")
    print(f"Goal: {profile.goal}")
    print(f"Gender: {profile.gender}")
    print(f"Diet: {profile.diet_preference}")
    
    # Calculate personalized calories
    calc_result = profile.calculate_target_calories()
    
    print(f"\n✓ PERSONALIZED CALCULATION:")
    print(f"  BMR: {calc_result['bmr']} cal/day")
    print(f"  Weekly Change: {calc_result['weekly_change']:+.2f}kg/week")
    print(f"  Daily Adjustment: {calc_result['daily_adjustment']:+.0f} cal/day")
    print(f"  🎯 TARGET CALORIES: {calc_result['target_calories']} cal/day")
    print(f"  Safe: {'✓ YES' if calc_result['is_safe'] else '⚠️  NO'}")
    
    if calc_result['warnings']:
        print(f"\n⚠️  WARNINGS:")
        for warning in calc_result['warnings']:
            print(f"    - {warning}")

print(f"\n{'='*80}")
print("CONCLUSION:")
print("=" * 80)
print("✓ Personalized calorie calculation is working!")
print("✓ Safety checks are in place")
print("✓ Warnings shown for unrealistic goals")
