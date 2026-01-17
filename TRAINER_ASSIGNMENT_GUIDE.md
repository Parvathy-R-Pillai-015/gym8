# Trainer Assignment System - Implementation Guide

## Overview
Admin can assign maximum 2 trainers per goal category. Users can select a trainer based on their chosen fitness goal.

## Goal Categories
1. **Weight Gain** (weight_gain)
2. **Weight Loss** (weight_loss)
3. **Muscle Gain** (muscle_gain)
4. **Others** (others)

## Backend Implementation

### Models (users/models.py)

#### Trainer Model
```python
GOAL_CATEGORY_CHOICES = [
    ('weight_gain', 'Weight Gain'),
    ('weight_loss', 'Weight Loss'),
    ('muscle_gain', 'Muscle Gain'),
    ('others', 'Others'),
]

goal_category = models.CharField(max_length=20, choices=GOAL_CATEGORY_CHOICES, null=True, blank=True)
certification = models.CharField(max_length=200, blank=True)
is_active = models.BooleanField(default=True)
```

#### UserProfile Model
```python
assigned_trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_users')
```

### API Endpoints (users/admin_views.py)

#### 1. Get All Trainers
- **URL**: `/api/admin/trainers/`
- **Method**: GET
- **Response**:
```json
{
  "success": true,
  "trainers": [
    {
      "id": 1,
      "name": "John Doe",
      "experience": 5,
      "specialization": "Weight Training",
      "goal_category": "weight_gain",
      "certification": "ACE Certified",
      "is_active": true,
      "assigned_users_count": 3
    }
  ]
}
```

#### 2. Get Trainers by Goal Category
- **URL**: `/api/admin/trainers/<goal>/`
- **Method**: GET
- **Example**: `/api/admin/trainers/weight_gain/`
- **Returns**: Max 2 active trainers for that category
- **Response**:
```json
{
  "success": true,
  "trainers": [
    {
      "id": 1,
      "name": "John Doe",
      "experience": 5,
      "specialization": "Weight Training"
    }
  ]
}
```

#### 3. Assign Trainer to Goal Category
- **URL**: `/api/admin/trainers/assign/`
- **Method**: POST
- **Body**:
```json
{
  "trainer_id": 1,
  "goal_category": "weight_gain"
}
```
- **Validation**: Maximum 2 trainers per category
- **Response**:
```json
{
  "success": true,
  "message": "Trainer assigned to Weight Gain category"
}
```
Or if limit exceeded:
```json
{
  "success": false,
  "message": "Maximum 2 trainers already assigned to Weight Gain category"
}
```

#### 4. Remove Trainer from Goal Category
- **URL**: `/api/admin/trainers/remove/`
- **Method**: POST
- **Body**:
```json
{
  "trainer_id": 1
}
```
- **Response**:
```json
{
  "success": true,
  "message": "Trainer removed from category"
}
```

### User Profile API (users/views.py)

#### Create/Update Profile with Trainer
- **URL**: `/api/profile/create/`
- **Method**: POST
- **Body includes**:
```json
{
  "user_id": 1,
  "fitness_goal": "weight_gain",
  "trainer_id": 5,
  ...other fields
}
```
- **Backend Logic**: Automatically assigns the trainer to user's profile

## Frontend Implementation

### 1. Admin Dashboard (admin_dashboard_new.dart)
- Added 4th tab: **Trainers**
- Uses TabController with length: 4
- Tabs:
  1. All Users
  2. Paid Users
  3. Unpaid Users
  4. **Trainers** (NEW)

### 2. Trainer Management Tab (trainer_management_tab.dart)

#### Features:
1. **Summary Card** - Shows assignment status for all categories
2. **Goal Category Cards** - Expandable tiles for each goal category
3. **Trainer Assignment** - Assign/Reassign trainers to categories
4. **Capacity Indicator** - Shows X/2 trainers assigned
5. **Unassigned Trainers** - List of trainers not yet assigned

#### UI Components:
```dart
- Summary: Total trainers, assignments per category
- Expandable Cards per Goal Category
- Trainer Tiles with:
  * Avatar with active status (green/grey)
  * Name, experience, specialization
  * Assigned users count
  * Action buttons:
    - Remove from category (red icon)
    - Assign/Reassign to category (blue icon)
```

#### Dialog for Assignment:
- Shows all 4 goal categories
- Current category highlighted with checkmark
- Select new category to reassign
- Validates max 2 trainers per category on backend

### 3. User Profile Form (user_profile_screen.dart)

#### Features:
1. **Dynamic Trainer Loading**: When user selects fitness goal, automatically loads available trainers for that category
2. **Trainer Dropdown**: Shows trainer details (name, experience, specialization)
3. **Auto-Assignment**: Selected trainer is sent with profile submission

#### Code Flow:
```dart
1. User selects fitness goal from dropdown
2. _loadTrainersForGoal(selectedGoal) is called
3. Fetches trainers: GET /api/admin/trainers/{goal}/
4. Populates _availableTrainers list
5. Shows trainer dropdown with trainer details
6. On submit, sends trainer_id with profile data
```

### 4. Home Screen (home_screen.dart)
- Displays assigned trainer information
- Shows trainer name in profile details

## Usage Flow

### Admin Workflow:
1. Login as admin
2. Navigate to **Trainers** tab in Admin Dashboard
3. View summary of trainer assignments
4. For each category:
   - See currently assigned trainers (max 2)
   - Click blue icon to assign/reassign trainers
   - Select goal category from dialog
   - System validates max 2 per category
   - Click red icon to remove trainer from category
5. View unassigned trainers section
6. Assign trainers to categories as needed

### User Workflow:
1. Login/Register
2. Fill profile form
3. Select fitness goal (Weight Gain/Loss/Muscle Gain/Others)
4. **Trainer dropdown automatically appears** with available trainers
5. Select preferred trainer (optional)
6. Submit profile
7. View assigned trainer on home screen

## Database Migrations
- Migration 0007: Added goal_category, certification, is_active to Trainer model
- Applied successfully: `python manage.py migrate`

## Key Features
✅ Maximum 2 trainers per goal category (enforced)
✅ Dynamic trainer loading based on user's goal
✅ Visual capacity indicators (X/2)
✅ Admin can reassign trainers between categories
✅ Shows assigned users count per trainer
✅ Active/Inactive trainer status
✅ User can see assigned trainer details

## API Security Notes
- All admin endpoints should be protected with authentication
- Currently open for development, should add @admin_required decorator in production

## Testing Checklist
- [ ] Admin assigns trainer to category
- [ ] Verify max 2 trainers limit works
- [ ] Admin removes trainer from category
- [ ] Admin reassigns trainer to different category
- [ ] User selects goal, sees available trainers
- [ ] User selects trainer, submits profile
- [ ] Verify trainer assignment shows on home screen
- [ ] Verify trainer info shows in admin paid users view
- [ ] Check unassigned trainers section
- [ ] Test with all 4 goal categories
