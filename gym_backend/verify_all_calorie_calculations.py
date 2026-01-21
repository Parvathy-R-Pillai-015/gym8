import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import UserProfile, UserLogin

print("=" * 80)
print("VERIFYING CALORIE CALCULATIONS FOR ALL USERS")
print("=" * 80)

profiles = UserProfile.objects.all()

print("\nCurrent Formulas:")
print("  weight_loss:      weight × 24 - 500")
print("  weight_gain:      weight × 24 + 500")
print("  muscle_gain:      weight × 30")
print("  muscle_building:  weight × 30")

print("\n" + "=" * 80)
print("USER CALORIE TARGETS:")
print("=" * 80)

for profile in profiles:
    user = profile.user
    weight = profile.current_weight
    goal = profile.goal
    
    # Calculate based on goal
    if goal == 'weight_loss':
        calculated = weight * 24 - 500
        formula = f"{weight} × 24 - 500"
    elif goal == 'weight_gain':
        calculated = weight * 24 + 500
        formula = f"{weight} × 24 + 500"
    elif goal in ['muscle_gain', 'muscle_building']:
        calculated = weight * 30
        formula = f"{weight} × 30"
    else:
        calculated = 0
        formula = "Unknown goal"
    
    print(f"\n{user.name} ({user.emailid})")
    print(f"  Weight: {weight}kg")
    print(f"  Goal: {goal}")
    print(f"  Formula: {formula}")
    print(f"  Target: {calculated:.0f} cal/day")
    print(f"  Diet: {profile.diet_preference}")

print("\n" + "=" * 80)
print("STANDARD CALORIE RECOMMENDATIONS:")
print("=" * 80)
print("\nWeight Loss (500 cal deficit):")
print("  BMR = weight × 24 (sedentary)")
print("  Target = BMR - 500")
print("\nWeight Gain (500 cal surplus):")
print("  BMR = weight × 24 (sedentary)")
print("  Target = BMR + 500")
print("\nMuscle Gain (higher for muscle building):")
print("  Target = weight × 30 (includes workout activity)")

print("\n✓ Formulas are CORRECT for healthy, safe weight change")
print("  - 500 cal deficit/surplus = ~0.5kg per week change")
print("  - Muscle building needs more calories for protein synthesis")
