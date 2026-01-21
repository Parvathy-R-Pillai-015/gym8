import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import DietPlanTemplate

print("=" * 80)
print("CREATING 'OTHERS' GOAL DIET TEMPLATES (General Fitness Maintenance)")
print("=" * 80)
print("\nFor users who want general fitness without weight change")
print("Plans organized by weight ranges with balanced nutrition\n")

# =============================================================================
# 30-40 KG WEIGHT RANGE (1200-1500 calories)
# =============================================================================

DietPlanTemplate.objects.create(
    name="General Fitness - Vegan (30-40kg)",
    goal_type="others",
    calorie_min=1200,
    calorie_max=1500,
    description="7-day balanced vegan maintenance plan for 30-40kg users",
    meals_data={
        "monday": {
            "breakfast": [{"food": "Oats", "quantity": "50g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "10g"}],
            "lunch": [{"food": "Rice (brown, cooked)", "quantity": "80g"}, {"food": "Lentils (cooked)", "quantity": "100g"}, {"food": "Spinach", "quantity": "80g"}],
            "dinner": [{"food": "Quinoa", "quantity": "60g"}, {"food": "Chickpeas (cooked)", "quantity": "80g"}, {"food": "Broccoli", "quantity": "80g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "8g"}]
        },
        "tuesday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Tofu", "quantity": "80g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "80g"}, {"food": "Black beans", "quantity": "80g"}, {"food": "Carrot", "quantity": "60g"}],
            "snacks": [{"food": "Banana", "quantity": "1 small"}, {"food": "Peanuts", "quantity": "10g"}]
        },
        "wednesday": {
            "breakfast": [{"food": "Oats", "quantity": "45g"}, {"food": "Mango", "quantity": "70g"}, {"food": "Cashews", "quantity": "8g"}],
            "lunch": [{"food": "Quinoa", "quantity": "70g"}, {"food": "Lentils (cooked)", "quantity": "90g"}, {"food": "Spinach", "quantity": "80g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Chickpeas (cooked)", "quantity": "90g"}, {"food": "Broccoli", "quantity": "80g"}],
            "snacks": [{"food": "Orange", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "8g"}]
        },
        "thursday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Banana", "quantity": "1 medium"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "80g"}, {"food": "Tofu", "quantity": "80g"}, {"food": "Carrot", "quantity": "70g"}],
            "dinner": [{"food": "Quinoa", "quantity": "60g"}, {"food": "Black beans", "quantity": "80g"}, {"food": "Mixed vegetables", "quantity": "90g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "8g"}]
        },
        "friday": {
            "breakfast": [{"food": "Oats", "quantity": "50g"}, {"food": "Orange", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "10g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Lentils (cooked)", "quantity": "100g"}, {"food": "Spinach", "quantity": "80g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "80g"}, {"food": "Chickpeas (cooked)", "quantity": "90g"}, {"food": "Broccoli", "quantity": "80g"}],
            "snacks": [{"food": "Banana", "quantity": "1 small"}, {"food": "Cashews", "quantity": "8g"}]
        },
        "saturday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Mango", "quantity": "70g"}],
            "lunch": [{"food": "Quinoa", "quantity": "70g"}, {"food": "Tofu", "quantity": "80g"}, {"food": "Mixed vegetables", "quantity": "100g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Black beans", "quantity": "80g"}, {"food": "Carrot", "quantity": "70g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "8g"}]
        },
        "sunday": {
            "breakfast": [{"food": "Oats", "quantity": "45g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "8g"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "80g"}, {"food": "Lentils (cooked)", "quantity": "100g"}, {"food": "Spinach", "quantity": "80g"}],
            "dinner": [{"food": "Quinoa", "quantity": "60g"}, {"food": "Chickpeas (cooked)", "quantity": "90g"}, {"food": "Broccoli", "quantity": "80g"}],
            "snacks": [{"food": "Orange", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "10g"}]
        }
    }
)
print("✓ Created: General Fitness - Vegan (30-40kg, 1200-1500 cal)")

DietPlanTemplate.objects.create(
    name="General Fitness - Vegetarian (30-40kg)",
    goal_type="others",
    calorie_min=1200,
    calorie_max=1500,
    description="7-day balanced vegetarian maintenance plan for 30-40kg users",
    meals_data={
        "monday": {
            "breakfast": [{"food": "Oats", "quantity": "45g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Milk (whole)", "quantity": "150ml"}],
            "lunch": [{"food": "Rice (brown, cooked)", "quantity": "80g"}, {"food": "Paneer", "quantity": "60g"}, {"food": "Spinach", "quantity": "80g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Lentils (cooked)", "quantity": "90g"}, {"food": "Broccoli", "quantity": "80g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "1 piece"}]
        },
        "tuesday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Eggs (scrambled)", "quantity": "1 piece"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Quinoa", "quantity": "70g"}, {"food": "Chickpeas (cooked)", "quantity": "80g"}, {"food": "Carrot", "quantity": "70g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "80g"}, {"food": "Paneer", "quantity": "60g"}, {"food": "Mixed vegetables", "quantity": "90g"}],
            "snacks": [{"food": "Milk (whole)", "quantity": "150ml"}, {"food": "Almonds", "quantity": "8g"}]
        },
        "wednesday": {
            "breakfast": [{"food": "Oats", "quantity": "50g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "8g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Lentils (cooked)", "quantity": "90g"}, {"food": "Spinach", "quantity": "80g"}],
            "dinner": [{"food": "Quinoa", "quantity": "60g"}, {"food": "Paneer", "quantity": "60g"}, {"food": "Broccoli", "quantity": "80g"}],
            "snacks": [{"food": "Orange", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "1 piece"}]
        },
        "thursday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Milk (whole)", "quantity": "150ml"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "80g"}, {"food": "Chickpeas (cooked)", "quantity": "80g"}, {"food": "Carrot", "quantity": "70g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Paneer", "quantity": "60g"}, {"food": "Mixed vegetables", "quantity": "90g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "8g"}]
        },
        "friday": {
            "breakfast": [{"food": "Oats", "quantity": "45g"}, {"food": "Orange", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "1 piece"}],
            "lunch": [{"food": "Quinoa", "quantity": "70g"}, {"food": "Lentils (cooked)", "quantity": "90g"}, {"food": "Spinach", "quantity": "80g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "80g"}, {"food": "Paneer", "quantity": "60g"}, {"food": "Broccoli", "quantity": "80g"}],
            "snacks": [{"food": "Banana", "quantity": "1 medium"}, {"food": "Milk (whole)", "quantity": "100ml"}]
        },
        "saturday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Eggs (scrambled)", "quantity": "1 piece"}, {"food": "Mango", "quantity": "60g"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Chickpeas (cooked)", "quantity": "80g"}, {"food": "Mixed vegetables", "quantity": "90g"}],
            "dinner": [{"food": "Quinoa", "quantity": "60g"}, {"food": "Paneer", "quantity": "60g"}, {"food": "Carrot", "quantity": "70g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "8g"}]
        },
        "sunday": {
            "breakfast": [{"food": "Oats", "quantity": "50g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "8g"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "80g"}, {"food": "Lentils (cooked)", "quantity": "90g"}, {"food": "Spinach", "quantity": "80g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Paneer", "quantity": "60g"}, {"food": "Broccoli", "quantity": "80g"}],
            "snacks": [{"food": "Orange", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "1 piece"}]
        }
    }
)
print("✓ Created: General Fitness - Vegetarian (30-40kg, 1200-1500 cal)")

DietPlanTemplate.objects.create(
    name="General Fitness - Non-Veg (30-40kg)",
    goal_type="others",
    calorie_min=1200,
    calorie_max=1500,
    description="7-day balanced non-veg maintenance plan for 30-40kg users",
    meals_data={
        "monday": {
            "breakfast": [{"food": "Oats", "quantity": "40g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}],
            "lunch": [{"food": "Rice (brown, cooked)", "quantity": "80g"}, {"food": "Chicken breast", "quantity": "70g"}, {"food": "Broccoli", "quantity": "80g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Lentils (cooked)", "quantity": "80g"}, {"food": "Spinach", "quantity": "80g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Orange", "quantity": "1 medium"}]
        },
        "tuesday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Eggs (scrambled)", "quantity": "2 pieces"}],
            "lunch": [{"food": "Quinoa", "quantity": "70g"}, {"food": "Chicken thigh", "quantity": "60g"}, {"food": "Mixed vegetables", "quantity": "90g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "80g"}, {"food": "Chickpeas (cooked)", "quantity": "70g"}, {"food": "Carrot", "quantity": "70g"}],
            "snacks": [{"food": "Banana", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "8g"}]
        },
        "wednesday": {
            "breakfast": [{"food": "Oats", "quantity": "45g"}, {"food": "Orange", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Mutton", "quantity": "60g"}, {"food": "Potato", "quantity": "70g"}],
            "dinner": [{"food": "Quinoa", "quantity": "60g"}, {"food": "Lentils (cooked)", "quantity": "70g"}, {"food": "Broccoli", "quantity": "80g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "8g"}]
        },
        "thursday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Eggs (scrambled)", "quantity": "2 pieces"}, {"food": "Mango", "quantity": "50g"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "80g"}, {"food": "Chicken breast", "quantity": "70g"}, {"food": "Spinach", "quantity": "80g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Chickpeas (cooked)", "quantity": "70g"}, {"food": "Mixed vegetables", "quantity": "90g"}],
            "snacks": [{"food": "Orange", "quantity": "1 medium"}, {"food": "Peanuts", "quantity": "10g"}]
        },
        "friday": {
            "breakfast": [{"food": "Oats", "quantity": "40g"}, {"food": "Banana", "quantity": "1 medium"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}],
            "lunch": [{"food": "Quinoa", "quantity": "70g"}, {"food": "Chicken thigh", "quantity": "60g"}, {"food": "Broccoli", "quantity": "80g"}],
            "dinner": [{"food": "Rice (brown, cooked)", "quantity": "80g"}, {"food": "Lentils (cooked)", "quantity": "70g"}, {"food": "Carrot", "quantity": "70g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Cashews", "quantity": "8g"}]
        },
        "saturday": {
            "breakfast": [{"food": "Bread (whole wheat)", "quantity": "2 slices"}, {"food": "Eggs (scrambled)", "quantity": "2 pieces"}, {"food": "Orange", "quantity": "1 medium"}],
            "lunch": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Mutton", "quantity": "60g"}, {"food": "Mixed vegetables", "quantity": "90g"}],
            "dinner": [{"food": "Quinoa", "quantity": "60g"}, {"food": "Chickpeas (cooked)", "quantity": "70g"}, {"food": "Spinach", "quantity": "80g"}],
            "snacks": [{"food": "Banana", "quantity": "1 medium"}, {"food": "Almonds", "quantity": "8g"}]
        },
        "sunday": {
            "breakfast": [{"food": "Oats", "quantity": "45g"}, {"food": "Mango", "quantity": "60g"}, {"food": "Eggs (boiled)", "quantity": "2 pieces"}],
            "lunch": [{"food": "Rice (white, cooked)", "quantity": "80g"}, {"food": "Chicken breast", "quantity": "70g"}, {"food": "Broccoli", "quantity": "80g"}],
            "dinner": [{"food": "Roti (wheat)", "quantity": "2 pieces"}, {"food": "Lentils (cooked)", "quantity": "70g"}, {"food": "Carrot", "quantity": "70g"}],
            "snacks": [{"food": "Apple", "quantity": "1 medium"}, {"food": "Walnuts", "quantity": "8g"}]
        }
    }
)
print("✓ Created: General Fitness - Non-Veg (30-40kg, 1200-1500 cal)")

print("\n" + "=" * 80)
print("SUMMARY:")
print("=" * 80)
templates = DietPlanTemplate.objects.filter(goal_type='others').order_by('calorie_min', 'name')
for t in templates:
    print(f"  {t.calorie_min:4d}-{t.calorie_max:4d} cal | {t.name}")

print(f"\nTotal 'others' goal templates: {templates.count()}")
print("\n✅ Templates ready for general fitness users!")
print("=" * 80)
