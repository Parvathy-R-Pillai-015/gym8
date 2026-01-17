from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.

class UserLogin(models.Model):
    """
    UserLogin model to store user registration data
    """
    name = models.CharField(max_length=255, verbose_name="Name")
    emailid = models.EmailField(unique=True, max_length=255, verbose_name="Email ID")
    password = models.CharField(max_length=255, verbose_name="Password")
    role = models.CharField(max_length=50, default='user', verbose_name="Role")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    
    class Meta:
        db_table = 'userlogin'
        verbose_name = 'User Login'
        verbose_name_plural = 'User Logins'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} ({self.emailid})"
    
    def save(self, *args, **kwargs):
        # Hash password before saving if it's not already hashed
        if self.password and not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
    
    def check_password(self, raw_password):
        """Check if the provided password matches the stored hashed password"""
        return check_password(raw_password, self.password)


class Trainer(models.Model):
    """
    Trainer model to store trainer-specific information
    """
    GOAL_CATEGORY_CHOICES = [
        ('weight_gain', 'Weight Gain'),
        ('weight_loss', 'Weight Loss'),
        ('muscle_gain', 'Muscle Gain'),
        ('others', 'Others'),
    ]
    
    user = models.OneToOneField(UserLogin, on_delete=models.CASCADE, related_name='trainer_profile')
    mobile = models.CharField(max_length=10, verbose_name="Mobile Number")
    gender = models.CharField(max_length=10, verbose_name="Gender")
    experience = models.IntegerField(verbose_name="Years of Experience")
    specialization = models.CharField(max_length=100, verbose_name="Specialization")
    certification = models.CharField(max_length=255, blank=True, null=True, verbose_name="Certification")
    goal_category = models.CharField(max_length=20, choices=GOAL_CATEGORY_CHOICES, blank=True, null=True, verbose_name="Assigned Goal Category")
    joining_period = models.CharField(max_length=50, verbose_name="Joining Period")
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    
    class Meta:
        db_table = 'trainer'
        verbose_name = 'Trainer'
        verbose_name_plural = 'Trainers'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.name} - {self.specialization}"


class UserProfile(models.Model):
    """
    UserProfile model to store user's fitness goals and personal information
    """
    GOAL_CHOICES = [
        ('weight_gain', 'Weight Gain'),
        ('weight_loss', 'Weight Loss'),
        ('muscle_gain', 'Muscle Gain'),
        ('others', 'Others'),
    ]
    
    MONTH_CHOICES = [
        (1, '1 Month'),
        (2, '2 Months'),
        (3, '3 Months'),
        (6, '6 Months'),
        (8, '8 Months'),
        (12, '1 Year'),
    ]
    
    WORKOUT_TIME_CHOICES = [
        ('morning', '4 AM to 11 AM'),
        ('evening', '4 PM to 11 PM'),
    ]
    
    DIET_CHOICES = [
        ('vegetarian', 'Vegetarian'),
        ('non_veg', 'Non-Vegetarian'),
        ('vegan', 'Vegan'),
        ('others', 'Others'),
    ]
    
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    
    user = models.OneToOneField(UserLogin, on_delete=models.CASCADE, related_name='profile')
    mobile_number = models.CharField(max_length=10, verbose_name="Mobile Number", default='0000000000')
    age = models.IntegerField(verbose_name="Age")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name="Gender")
    current_weight = models.FloatField(verbose_name="Current Weight (kg)")
    current_height = models.FloatField(verbose_name="Current Height (cm)")
    goal = models.CharField(max_length=20, choices=GOAL_CHOICES, verbose_name="Goal")
    target_weight = models.FloatField(verbose_name="Target Weight (kg)")
    target_months = models.IntegerField(choices=MONTH_CHOICES, verbose_name="Target Months")
    workout_time = models.CharField(max_length=10, choices=WORKOUT_TIME_CHOICES, verbose_name="Workout Time")
    diet_preference = models.CharField(max_length=20, choices=DIET_CHOICES, verbose_name="Diet Preference")
    food_allergies = models.TextField(blank=True, null=True, verbose_name="Food Allergies")
    health_conditions = models.TextField(blank=True, null=True, verbose_name="Health Conditions")
    payment_status = models.BooleanField(default=False, verbose_name="Payment Status")
    payment_amount = models.IntegerField(default=0, verbose_name="Payment Amount")
    payment_method = models.CharField(max_length=20, blank=True, null=True, verbose_name="Payment Method")
    assigned_trainer = models.ForeignKey('Trainer', on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_users', verbose_name="Assigned Trainer")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    
    class Meta:
        db_table = 'user_profile'
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
    
    def __str__(self):
        return f"Profile: {self.user.name}"
    
    def calculate_payment_amount(self):
        """Calculate payment amount based on target months"""
        payment_map = {
            1: 399,
            2: 499,
            3: 699,
            6: 1199,
            8: 1599,
            12: 2199,
        }
        return payment_map.get(self.target_months, 0)
