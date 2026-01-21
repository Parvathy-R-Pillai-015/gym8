import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import DietPlanTemplate

print("=" * 80)
print("CREATING LOW CALORIE WEIGHT LOSS TEMPLATES (1200-1500)")
print("=" * 80)

# 1200-1500 VEGAN
DietPlanTemplate.objects.create(
    name="Weight Loss - Vegan Light (1200-1500)",
    goal_type="weight_loss",
    calorie_min=1200,
    calorie_max=1500,
    description="7-day low calorie vegan weight loss plan",
    meals_data={
        "monday": {
            "breakfast": [{"food": "Oats", "quantity": "50g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "10g"}],
            "lunch": [{"food": "Rice (brown, cooked)", "quantity": "80g"}, {"food": "Lentils (cooked)", "quantity": "100g"}, {"food": "Spinach", "quantity": "100g"}],
            "dinner": [{"food": "Quinoa", "quantity": "70g"}, {"food": "Chickpeas (cooked)", "quantity": "80g"}, {"food": "Broccoli", "quantity": "100g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Orange", "quantity": "1 medium"}]
        },
        "tuesday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Banana", "quantity": "1 medium"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Lentils (cooked)", "quantity": "100g"}, {"food": "Carrot", "quantity": "80g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "80g"}, {"food": "Tofu", "quantity": "80g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "snacks": [{"food": "Orange", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "8g"}]
        },
        "wednesday": {
            "breakfast": [{"food": "Oats", "quantity": "55g"}, {"food": "Mango", "quantity": "80g"}, {"food": "Peanuts", "quantity": "10g"}],
            "lunch": [{"food": "Quinoa", "quantity": "70g"}, {"food": "Black beans", "quantity": "90g"}, {"food": "Spinach", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Chickpeas (cooked)", "quantity": "100g"}, {"food": "Broccoli", "quantity": "100g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Banana", "quantity": "1 small"}]
        },
        "thursday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "80g"}, {"food": "Lentils (cooked)", "quantity": "100g"}, {"food": "Mixed vegetables", "quantity": "90g"}],
            "dinner": [{"food": "Quinoa", "quantity": "70g"}, {"food": "Tofu", "quantity": "80g"}, {"food": "Carrot", "quantity": "80g"}],
            "snacks": [{"food": "Mango", "quantity": "70g"}, {"food": "Cashews", "quantity": "8g"}]
        },
        "friday": {
            "breakfast": [{"food": "Oats", "quantity": "50g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "10g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Black beans", "quantity": "90g"}, {"food": "Spinach", "quantity": "100g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "80g"}, {"food": "Chickpeas (cooked)", "quantity": "100g"}, {"food": "Broccoli", "quantity": "100g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "8g"}]
        },
        "saturday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Mango", "quantity": "80g"}],
            "lunch": [{"food": "Quinoa", "quantity": "70g"}, {"food": "Lentils (cooked)", "quantity": "100g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Tofu", "quantity": "80g"}, {"food": "Carrot", "quantity": "80g"}],
            "snacks": [{"food": "Orange", "quantity": "1 medium"}, {"food": "Banana", "quantity": "1 small"}]
        },
        "sunday": {
            "breakfast": [{"food": "Oats", "quantity": "55g"}, {"food": "Orange", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "10g"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "80g"}, {"food": "Chickpeas (cooked)", "quantity": "100g"}, {"food": "Spinach", "quantity": "100g"}],
            "dinner": [{"food": "Quinoa", "quantity": "70g"}, {"food": "Black beans", "quantity": "90g"}, {"food": "Broccoli", "quantity": "100g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "8g"}]
        }
    }
)
print("✓ Created: Weight Loss - Vegan Light (1200-1500)")

# 1200-1500 VEGETARIAN
DietPlanTemplate.objects.create(
    name="Weight Loss - Vegetarian Light (1200-1500)",
    goal_type="weight_loss",
    calorie_min=1200,
    calorie_max=1500,
    description="7-day low calorie vegetarian weight loss plan",
    meals_data={
        "monday": {
            "breakfast": [{"food": "Oats", "quantity": "45g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Milk (whole)", "quantity": "150ml"}],
            "lunch": [{"food": "Rice (brown, cooked)", "quantity": "80g"}, {"food": "Paneer", "quantity": "60g"}, {"food": "Spinach", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Lentils (cooked)", "quantity": "90g"}, {"food": "Broccoli", "quantity": "100g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "1 piece"}]
        },
        "tuesday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Eggs (scrambled)", "quantity": "1 piece"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Quinoa", "quantity": "70g"}, {"food": "Chickpeas (cooked)", "quantity": "90g"}, {"food": "Carrot", "quantity": "80g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "80g"}, {"food": "Paneer", "quantity": "60g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "150ml"}, {"food": "Almonds", "quantity": "8g"}]
        },
        "wednesday": {
            "breakfast": [{"food": "Oats", "quantity": "50g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "8g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Lentils (cooked)", "quantity": "90g"}, {"food": "Spinach", "quantity": "100g"}],
            "dinner": [{"food": "Quinoa", "quantity": "70g"}, {"food": "Paneer", "quantity": "60g"}, {"food": "Broccoli", "quantity": "100g"}],
            "snacks": [{"food": "Orange", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "1 piece"}]
        },
        "thursday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Milk (whole)", "quantity": "150ml"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "80g"}, {"food": "Chickpeas (cooked)", "quantity": "90g"}, {"food": "Carrot", "quantity": "80g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Paneer", "quantity": "60g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "8g"}]
        },
        "friday": {
            "breakfast": [{"food": "Oats", "quantity": "45g"}, {"food": "Orange", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "1 piece"}],
            "lunch": [{"food": "Quinoa", "quantity": "70g"}, {"food": "Lentils (cooked)", "quantity": "90g"}, {"food": "Spinach", "quantity": "100g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "80g"}, {"food": "Paneer", "quantity": "60g"}, {"food": "Broccoli", "quantity": "100g"}],
            "snacks": [{"food": "Banana", "quantity": "1 medium"}, {"food": "Milk (whole)", "quantity": "100ml"}]
        },
        "saturday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Eggs (scrambled)", "quantity": "1 piece"}, {"food": "Mango", "quantity": "70g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Chickpeas (cooked)", "quantity": "90g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Quinoa", "quantity": "70g"}, {"food": "Paneer", "quantity": "60g"}, {"food": "Carrot", "quantity": "80g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "8g"}]
        },
        "sunday": {
            "breakfast": [{"food": "Oats", "quantity": "50g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "8g"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "80g"}, {"food": "Lentils (cooked)", "quantity": "90g"}, {"food": "Spinach", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Paneer", "quantity": "60g"}, {"food": "Broccoli", "quantity": "100g"}],
            "snacks": [{"food": "Orange", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "1 piece"}]
        }
    }
)
print("✓ Created: Weight Loss - Vegetarian Light (1200-1500)")

# 1200-1500 NON-VEG
DietPlanTemplate.objects.create(
    name="Weight Loss - Non-Veg Light (1200-1500)",
    goal_type="weight_loss",
    calorie_min=1200,
    calorie_max=1500,
    description="7-day low calorie non-veg weight loss plan",
    meals_data={
        "monday": {
            "breakfast": [{"food": "Oats", "quantity": "40g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}],
            "lunch": [{"food": "Rice (brown, cooked)", "quantity": "80g"}, {"food": "Chicken breast", "quantity": "80g"}, {"food": "Broccoli", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Lentils (cooked)", "quantity": "80g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Orange", "quantity": "1 medium"}]
        },
        "tuesday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Eggs (scrambled)", "quantity": "2 pieces"}],
            "lunch": [{"food": "Quinoa", "quantity": "70g"}, {"food": "Chicken thigh", "quantity": "70g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "80g"}, {"food": "Chickpeas (cooked)", "quantity": "80g"}, {"food": "Carrot", "quantity": "80g"}],
            "snacks": [{"food": "Banana", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "8g"}]
        },
        "wednesday": {
            "breakfast": [{"food": "Oats", "quantity": "45g"}, {"food": "Orange", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Mutton", "quantity": "70g"}, {"food": "Potato", "quantity": "80g"}],
            "dinner": [{"food": "Quinoa", "quantity": "70g"}, {"food": "Lentils (cooked)", "quantity": "80g"}, {"food": "Broccoli", "quantity": "100g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "8g"}]
        },
        "thursday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Eggs (scrambled)", "quantity": "2 pieces"}, {"food": "Mango", "quantity": "60g"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "80g"}, {"food": "Chicken breast", "quantity": "80g"}, {"food": "Spinach", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Chickpeas (cooked)", "quantity": "80g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "snacks": [{"food": "Orange", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "10g"}]
        },
        "friday": {
            "breakfast": [{"food": "Oats", "quantity": "40g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}],
            "lunch": [{"food": "Quinoa", "quantity": "70g"}, {"food": "Chicken thigh", "quantity": "70g"}, {"food": "Broccoli", "quantity": "100g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "80g"}, {"food": "Lentils (cooked)", "quantity": "80g"}, {"food": "Carrot", "quantity": "80g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "8g"}]
        },
        "saturday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Eggs (scrambled)", "quantity": "2 pieces"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Mutton", "quantity": "70g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Quinoa", "quantity": "70g"}, {"food": "Chickpeas (cooked)", "quantity": "80g"}, {"food": "Spinach", "quantity": "100g"}],
            "snacks": [{"food": "Banana", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "8g"}]
        },
        "sunday": {
            "breakfast": [{"food": "Oats", "quantity": "45g"}, {"food": "Mango", "quantity": "70g"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "80g"}, {"food": "Chicken breast", "quantity": "80g"}, {"food": "Broccoli", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Lentils (cooked)", "quantity": "80g"}, {"food": "Carrot", "quantity": "80g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "8g"}]
        }
    }
)
print("✓ Created: Weight Loss - Non-Veg Light (1200-1500)")

print("\n" + "=" * 80)
print("ALL WEIGHT_LOSS TEMPLATES:")
print("=" * 80)
templates = DietPlanTemplate.objects.filter(goal_type='weight_loss').order_by('calorie_min', 'name')
for t in templates:
    print(f"  {t.calorie_min:4d}-{t.calorie_max:4d} cal | {t.name}")

print(f"\nTotal weight_loss templates: {templates.count()}")
print("\nCalorie Coverage:")
print("  1200-1500 cal → Users weighing 50-70kg (NEW)")
print("  1500-2000 cal → Users weighing 71-87kg")
print("  2000-2500 cal → Users weighing 88-104kg")
