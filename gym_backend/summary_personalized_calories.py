import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import UserProfile, UserLogin

print("=" * 80)
print("✅ CALORIE SYSTEM UPGRADED TO PERSONALIZED CALCULATION")
print("=" * 80)

print("\n📊 SUMMARY OF CHANGES:")
print("  1. Added calculate_target_calories() method to UserProfile model")
print("  2. Personalized calculation based on:")
print("     - Current weight → Target weight")
print("     - Target timeline (months)")
print("     - Gender (for min safe calories)")
print("  3. Safety checks implemented:")
print("     - Max weight change: ±1kg/week")
print("     - Min safe calories: 1200 (female) / 1500 (male)")
print("     - Max safe calories: 4000 cal/day")
print("  4. Warnings generated for unrealistic goals")
print("  5. API endpoint updated: /api/diet/calculate/<user_id>/")

print("\n" + "=" * 80)
print("SAMPLE CALCULATIONS (First 5 Users):")
print("=" * 80)

profiles = UserProfile.objects.all()[:5]

for profile in profiles:
    user = profile.user
    calc = profile.calculate_target_calories()
    
    print(f"\n{user.name}")
    print(f"  {profile.current_weight}kg → {profile.target_weight}kg ({profile.target_months} months)")
    print(f"  🎯 Personalized: {calc['target_calories']} cal/day")
    print(f"  📈 Weekly change: {calc['weekly_change']:+.2f}kg/week")
    print(f"  {'✅ Safe goal' if calc['is_safe'] else '⚠️  ' + ', '.join(calc['warnings'][:1])}")

print("\n" + "=" * 80)
print("NEXT STEPS:")
print("=" * 80)
print("1. Backend automatically uses new personalized calculation")
print("2. Frontend will receive warnings in API response")
print("3. Trainers can see if user goals are realistic")
print("4. Diet plan templates still match by calorie range")
print("\n✅ System is ready to use!")
