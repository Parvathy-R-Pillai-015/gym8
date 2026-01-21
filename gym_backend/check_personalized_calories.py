import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import UserProfile, UserLogin

print("=" * 80)
print("CHECKING PERSONALIZED CALORIE CALCULATIONS")
print("=" * 80)

profiles = UserProfile.objects.all()

print("\nCurrent System:")
print("  ❌ Uses FIXED formula (weight × 24 ± 500)")
print("  ❌ Same calorie deficit/surplus for everyone")
print("\nShould Use:")
print("  ✓ Calculate based on target_weight and target_months")
print("  ✓ Personalized deficit/surplus per user")

print("\n" + "=" * 80)
print("USER GOALS & CORRECT CALCULATIONS:")
print("=" * 80)

for profile in profiles:
    user = profile.user
    current_weight = profile.current_weight
    target_weight = profile.target_weight
    target_months = profile.target_months
    goal = profile.goal
    
    # Calculate weight difference
    weight_diff = target_weight - current_weight
    
    # Calculate weekly change needed
    weeks = target_months * 4
    weekly_change = weight_diff / weeks if weeks > 0 else 0
    
    # 1kg weight change = 7700 calories
    # Daily calorie adjustment = (weekly_change × 7700) / 7
    daily_adjustment = (weekly_change * 7700) / 7
    
    # BMR (Base Metabolic Rate)
    bmr = current_weight * 24
    
    # Correct personalized target
    personalized_target = bmr + daily_adjustment
    
    # Current system target
    if goal == 'weight_loss':
        current_target = current_weight * 24 - 500
    elif goal == 'weight_gain':
        current_target = current_weight * 24 + 500
    elif goal in ['muscle_gain', 'muscle_building']:
        current_target = current_weight * 30
    else:
        current_target = 0
    
    print(f"\n{user.name}")
    print(f"  Current: {current_weight}kg → Target: {target_weight}kg")
    print(f"  Change needed: {weight_diff:+.1f}kg in {target_months} months")
    print(f"  Weekly change: {weekly_change:+.2f}kg/week")
    print(f"  BMR: {bmr:.0f} cal/day")
    print(f"  Adjustment: {daily_adjustment:+.0f} cal/day")
    print(f"  ✓ CORRECT Target: {personalized_target:.0f} cal/day")
    print(f"  ❌ Current System: {current_target:.0f} cal/day")
    
    difference = abs(personalized_target - current_target)
    if difference > 100:
        print(f"  ⚠️  ERROR: {difference:.0f} cal/day difference!")

print("\n" + "=" * 80)
print("RECOMMENDATION:")
print("=" * 80)
print("Update calorie calculation to use:")
print("  BMR = current_weight × 24")
print("  weight_change = (target_weight - current_weight)")
print("  weeks = target_months × 4")
print("  daily_adjustment = (weight_change × 7700) / (weeks × 7)")
print("  target_calories = BMR + daily_adjustment")
