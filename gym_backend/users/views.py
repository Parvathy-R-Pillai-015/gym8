from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import UserLogin, Trainer, UserProfile

# Create your views here.

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            emailid = data.get('emailid')
            password = data.get('password')
            
            if not name or not emailid or not password:
                return JsonResponse({
                    'success': False,
                    'message': 'All fields (name, emailid, password) are required'
                }, status=400)
            
            # Check if user with this email already exists
            if UserLogin.objects.filter(emailid=emailid).exists():
                return JsonResponse({
                    'success': False,
                    'message': 'User with this email already exists'
                }, status=400)
            
            # Create new user
            user = UserLogin.objects.create(
                name=name,
                emailid=emailid,
                password=password  # Password will be hashed in the model's save method
            )
            
            return JsonResponse({
                'success': True,
                'message': 'User registered successfully',
                'user': {
                    'id': user.id,
                    'name': user.name,
                    'emailid': user.emailid
                }
            }, status=201)
            
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'message': 'Invalid JSON data'
            }, status=400)
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            }, status=500)
    
    return JsonResponse({
        'success': False,
        'message': 'Only POST method is allowed'
    }, status=405)


@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            emailid = data.get('emailid')
            password = data.get('password')
            
            print(f"[LOGIN ATTEMPT] Email: {emailid}")  # Debug log
            
            if not emailid or not password:
                return JsonResponse({
                    'success': False,
                    'message': 'Email and password are required'
                }, status=400)
            
            # Find user by emailid
            try:
                user = UserLogin.objects.get(emailid=emailid)
                print(f"[USER FOUND] Name: {user.name}, Email: {user.emailid}")  # Debug log
            except UserLogin.DoesNotExist:
                print(f"[USER NOT FOUND] Email: {emailid} - REJECTED")  # Debug log
                return JsonResponse({
                    'success': False,
                    'message': 'User not registered. Please register first.'
                }, status=401)
            
            # Check if user is active
            if not user.is_active:
                print(f"[INACTIVE USER] Email: {emailid} - REJECTED")  # Debug log
                return JsonResponse({
                    'success': False,
                    'message': 'Account is inactive. Please contact support.'
                }, status=401)
            
            # Check password
            if user.check_password(password):
                print(f"[LOGIN SUCCESS] Email: {emailid} - Role: {user.role}")  # Debug log
                return JsonResponse({
                    'success': True,
                    'message': 'Login successful',
                    'user': {
                        'id': user.id,
                        'name': user.name,
                        'emailid': user.emailid,
                        'role': user.role
                    }
                }, status=200)
            else:
                print(f"[WRONG PASSWORD] Email: {emailid} - REJECTED")  # Debug log
                return JsonResponse({
                    'success': False,
                    'message': 'Invalid email or password'
                }, status=401)
            
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'message': 'Invalid JSON data'
            }, status=400)
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            }, status=500)
    
    return JsonResponse({
        'success': False,
        'message': 'Only POST method is allowed'
    }, status=405)


@csrf_exempt
def create_trainer(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            emailid = data.get('emailid')
            mobile = data.get('mobile')
            gender = data.get('gender')
            experience = data.get('experience')
            specialization = data.get('specialization')
            joining_period = data.get('joining_period')
            password = data.get('password')
            
            if not all([name, emailid, mobile, gender, experience, specialization, joining_period, password]):
                return JsonResponse({'success': False, 'message': 'All fields are required'}, status=400)
            
            if UserLogin.objects.filter(emailid=emailid).exists():
                return JsonResponse({'success': False, 'message': 'Email already exists'}, status=400)
            
            if len(mobile) != 10 or not mobile.isdigit():
                return JsonResponse({'success': False, 'message': 'Mobile number must be 10 digits'}, status=400)
            
            user = UserLogin.objects.create(name=name, emailid=emailid, password=password, role='trainer')
            trainer = Trainer.objects.create(user=user, mobile=mobile, gender=gender, experience=int(experience), specialization=specialization, joining_period=joining_period)
            
            return JsonResponse({'success': True, 'message': 'Trainer added successfully', 'trainer': {'id': trainer.id, 'name': user.name, 'emailid': user.emailid, 'mobile': trainer.mobile, 'specialization': trainer.specialization}}, status=201)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)
    return JsonResponse({'success': False, 'message': 'Only POST method is allowed'}, status=405)


@csrf_exempt
def create_profile(request):
    """Create or update user profile with fitness goals"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_id = data.get('user_id')
            
            # Validate user_id
            if not user_id:
                return JsonResponse({
                    'success': False,
                    'message': 'User ID is required'
                }, status=400)
            
            # Check if user exists
            try:
                user = UserLogin.objects.get(id=user_id)
            except UserLogin.DoesNotExist:
                return JsonResponse({
                    'success': False,
                    'message': 'User not found'
                }, status=404)
            
            # Get all required fields
            mobile_number = data.get('mobile_number', '')
            age = data.get('age')
            gender = data.get('gender')
            current_weight = data.get('current_weight')
            current_height = data.get('current_height')
            goal = data.get('goal')
            target_weight = data.get('target_weight')
            target_months = data.get('target_months')
            workout_time = data.get('workout_time')
            diet_preference = data.get('diet_preference')
            food_allergies = data.get('food_allergies', '')
            health_conditions = data.get('health_conditions', '')
            trainer_id = data.get('trainer_id')
            
            # Validate required fields
            if not all([age, gender, current_weight, current_height, goal, target_weight, target_months, workout_time, diet_preference]):
                return JsonResponse({
                    'success': False,
                    'message': 'All fields are required except food allergies and health conditions'
                }, status=400)
            
            # Calculate payment amount based on target months
            payment_map = {1: 399, 2: 499, 3: 699, 6: 1199, 8: 1599, 12: 2199}
            payment_amount = payment_map.get(int(target_months), 0)
            
            # Check if profile already exists and update or create
            try:
                profile = UserProfile.objects.get(user=user)
                # Update existing profile
                profile.mobile_number = mobile_number
                profile.age = int(age)
                profile.gender = gender
                profile.current_weight = float(current_weight)
                profile.current_height = float(current_height)
                profile.goal = goal
                profile.target_weight = float(target_weight)
                profile.target_months = int(target_months)
                profile.workout_time = workout_time
                profile.diet_preference = diet_preference
                profile.food_allergies = food_allergies
                profile.health_conditions = health_conditions
                profile.payment_amount = payment_amount
                
                # Assign trainer if provided
                if trainer_id:
                    try:
                        trainer = Trainer.objects.get(id=trainer_id)
                        profile.assigned_trainer = trainer
                    except Trainer.DoesNotExist:
                        pass
                
                profile.save()
            except UserProfile.DoesNotExist:
                # Get trainer if provided
                assigned_trainer = None
                if trainer_id:
                    try:
                        assigned_trainer = Trainer.objects.get(id=trainer_id)
                    except Trainer.DoesNotExist:
                        pass
                
                # Create new profile with all fields
                profile = UserProfile.objects.create(
                    user=user,
                    mobile_number=mobile_number,
                    age=int(age),
                    gender=gender,
                    current_weight=float(current_weight),
                    current_height=float(current_height),
                    goal=goal,
                    target_weight=float(target_weight),
                    target_months=int(target_months),
                    workout_time=workout_time,
                    diet_preference=diet_preference,
                    food_allergies=food_allergies,
                    health_conditions=health_conditions,
                    payment_amount=payment_amount,
                    assigned_trainer=assigned_trainer
                )
            
            return JsonResponse({
                'success': True,
                'message': 'Profile saved successfully',
                'profile': {
                    'id': profile.id,
                    'user_id': user.id,
                    'age': profile.age,
                    'gender': profile.gender,
                    'current_weight': profile.current_weight,
                    'current_height': profile.current_height,
                    'goal': profile.goal,
                    'target_weight': profile.target_weight,
                    'target_months': profile.target_months,
                    'workout_time': profile.workout_time,
                    'diet_preference': profile.diet_preference,
                    'food_allergies': profile.food_allergies,
                    'health_conditions': profile.health_conditions,
                    'payment_amount': profile.payment_amount,
                    'payment_status': profile.payment_status
                }
            }, status=200)
            
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'message': 'Invalid JSON data'
            }, status=400)
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            }, status=500)
    
    return JsonResponse({
        'success': False,
        'message': 'Only POST method is allowed'
    }, status=405)


@csrf_exempt
def get_profile(request, user_id):
    """Get user profile by user_id"""
    if request.method == 'GET':
        try:
            print(f"Getting profile for user_id: {user_id}")
            user = UserLogin.objects.get(id=user_id)
            try:
                profile = UserProfile.objects.get(user=user)
                print(f"Profile found: {profile.id}, payment_status: {profile.payment_status}")
                
                # Get trainer info if assigned
                trainer_info = None
                if profile.assigned_trainer:
                    trainer = profile.assigned_trainer
                    trainer_info = {
                        'id': trainer.id,
                        'name': trainer.user.name,
                        'email': trainer.user.emailid,
                        'mobile': trainer.mobile,
                        'experience': trainer.experience,
                        'specialization': trainer.specialization,
                        'certification': trainer.certification or 'Not Specified'
                    }
                
                response_data = {
                    'success': True,
                    'profile': {
                        'id': profile.id,
                        'user_id': user.id,
                        'mobile_number': profile.mobile_number,
                        'age': profile.age,
                        'gender': profile.gender,
                        'current_weight': profile.current_weight,
                        'current_height': profile.current_height,
                        'goal': profile.goal,
                        'target_weight': profile.target_weight,
                        'target_months': profile.target_months,
                        'workout_time': profile.workout_time,
                        'diet_preference': profile.diet_preference,
                        'food_allergies': profile.food_allergies,
                        'health_conditions': profile.health_conditions,
                        'payment_amount': profile.payment_amount,
                        'payment_status': profile.payment_status,
                        'assigned_trainer': trainer_info
                    }
                }
                print(f"Returning response: {response_data}")
                return JsonResponse(response_data, status=200)
            except UserProfile.DoesNotExist:
                print(f"Profile not found for user_id: {user_id}")
                return JsonResponse({
                    'success': False,
                    'message': 'Profile not found'
                }, status=404)
        except UserLogin.DoesNotExist:
            print(f"User not found: {user_id}")
            return JsonResponse({
                'success': False,
                'message': 'User not found'
            }, status=404)
        except Exception as e:
            print(f"Error in get_profile: {str(e)}")
            return JsonResponse({
                'success': False,
                'message': str(e)
            }, status=500)
    
    return JsonResponse({
        'success': False,
        'message': 'Only GET method is allowed'
    }, status=405)


@csrf_exempt
def update_payment_status(request):
    """Update payment status after successful payment"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_id = data.get('user_id')
            payment_status = data.get('payment_status', True)
            
            if not user_id:
                return JsonResponse({
                    'success': False,
                    'message': 'User ID is required'
                }, status=400)
            
            payment_method = data.get('payment_method', '')
            
            user = UserLogin.objects.get(id=user_id)
            profile = UserProfile.objects.get(user=user)
            profile.payment_status = payment_status
            if payment_method:
                profile.payment_method = payment_method
            profile.save()
            
            return JsonResponse({
                'success': True,
                'message': 'Payment status updated successfully',
                'payment_status': profile.payment_status
            }, status=200)
            
        except UserLogin.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'User not found'
            }, status=404)
        except UserProfile.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'Profile not found'
            }, status=404)
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            }, status=500)
    
    return JsonResponse({
        'success': False,
        'message': 'Only POST method is allowed'
    }, status=405)
