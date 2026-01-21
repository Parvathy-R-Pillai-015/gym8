import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_backend.settings')
django.setup()

from users.models import WorkoutVideo, Trainer

"""
BULK VIDEO UPLOAD SCRIPT

Instructions:
1. Place your video files in a folder (e.g., C:\Videos\)
2. Update the VIDEO_FOLDER path below
3. Update the VIDEO_METADATA list with your video information
4. Run: python bulk_upload_videos.py

Video Naming Convention (if you want automatic detection):
- Format: goaltype_difficulty_title.mp4
- Example: weight_gain_beginner_basic_exercises.mp4
"""

# =============================================================================
# CONFIGURATION - UPDATE THESE VALUES
# =============================================================================

# Path to folder containing your videos
VIDEO_FOLDER = r"C:\Videos\Gym"

# Trainer ID who is uploading these videos (get from database)
TRAINER_ID = 3  # sooraj - weight_gain trainer

# =============================================================================
# VIDEO METADATA - Define your 10 videos here
# =============================================================================

VIDEO_METADATA = [
    # Beginner videos (0-10kg weight difference) - 7 videos
    {
        'filename': 'WhatsApp Video 2026-01-19 at 11.05.27 AM.mp4',
        'title': 'Beginner Weight Loss - Cardio Basics',
        'description': 'Start your weight loss journey with basic cardio exercises.',
        'goal_type': 'weight_loss',
        'difficulty_level': 'beginner',
        'duration': 600,
    },
    {
        'filename': 'WhatsApp Video 2026-01-19 at 11.11.34 AM.mp4',
        'title': 'Beginner Fat Burning Workout',
        'description': 'Easy fat burning exercises for beginners.',
        'goal_type': 'weight_loss',
        'difficulty_level': 'beginner',
        'duration': 720,
    },
    {
        'filename': 'WhatsApp Video 2026-01-19 at 11.41.08 AM.mp4',
        'title': 'Low Impact Weight Loss',
        'description': 'Gentle exercises perfect for weight loss beginners.',
        'goal_type': 'weight_loss',
        'difficulty_level': 'beginner',
        'duration': 660,
    },
    {
        'filename': 'WhatsApp Video 2026-01-19 at 11.41.53 AM.mp4',
        'title': 'Walking & Light Exercises',
        'description': 'Walking-based workout to kickstart weight loss.',
        'goal_type': 'weight_loss',
        'difficulty_level': 'beginner',
        'duration': 540,
    },
    {
        'filename': 'WhatsApp Video 2026-01-21 at 11.08.40 AM.mp4',
        'title': 'Beginner Toning Exercises',
        'description': 'Basic toning exercises while losing weight.',
        'goal_type': 'weight_loss',
        'difficulty_level': 'beginner',
        'duration': 600,
    },
    {
        'filename': 'WhatsApp Video 2026-01-21 at 11.15.46 AM.mp4',
        'title': 'Simple Fat Burning Routine',
        'description': 'Simple and effective fat burning for beginners.',
        'goal_type': 'weight_loss',
        'difficulty_level': 'beginner',
        'duration': 900,
    },
    {
        'filename': 'WhatsApp Video 2026-01-21 at 11.16.48 AM.mp4',
        'title': 'Beginner Weight Loss - Full Body',
        'description': 'Complete full body workout for weight loss beginners.',
        'goal_type': 'weight_loss',
        'difficulty_level': 'beginner',
        'duration': 840,
    },
    
    # Advanced videos (11-30kg weight difference) - 3 videos
    {
        'filename': 'WhatsApp Video 2026-01-21 at 11.17.34 AM.mp4',
        'title': 'Advanced Fat Burn - High Intensity',
        'description': 'High intensity workout for significant weight loss (11kg+).',
        'goal_type': 'weight_loss',
        'difficulty_level': 'advanced',
        'duration': 780,
    },
    {
        'filename': 'WhatsApp Video 2026-01-21 at 11.21.36 AM.mp4',
        'title': 'HIIT Weight Loss - Advanced',
        'description': 'Advanced HIIT training for maximum fat burn.',
        'goal_type': 'weight_loss',
        'difficulty_level': 'advanced',
        'duration': 960,
    },
    {
        'filename': 'WhatsApp Video 2026-01-21 at 11.25.15 AM.mp4',
        'title': 'Complete Weight Loss Masterclass',
        'description': 'Comprehensive advanced weight loss workout program.',
        'goal_type': 'weight_loss',
        'difficulty_level': 'advanced',
        'duration': 900,
    },
]

# =============================================================================
# UPLOAD SCRIPT - DON'T MODIFY BELOW UNLESS YOU KNOW WHAT YOU'RE DOING
# =============================================================================

def upload_videos():
    """
    Upload videos to the database
    """
    print("="*80)
    print("BULK VIDEO UPLOAD SCRIPT")
    print("="*80)
    
    # Check if trainer exists
    try:
        trainer = Trainer.objects.get(id=TRAINER_ID)
        print(f"✓ Trainer found: {trainer.user.name}")
    except Trainer.DoesNotExist:
        print(f"✗ ERROR: Trainer with ID {TRAINER_ID} not found!")
        print("  Available trainers:")
        for t in Trainer.objects.all():
            print(f"    ID {t.id}: {t.user.name}")
        return
    
    # Check if video folder exists
    if not os.path.exists(VIDEO_FOLDER):
        print(f"✗ ERROR: Video folder not found: {VIDEO_FOLDER}")
        print("  Please create the folder and place your videos inside.")
        return
    
    print(f"✓ Video folder found: {VIDEO_FOLDER}")
    print(f"\nUploading {len(VIDEO_METADATA)} videos...\n")
    
    uploaded_count = 0
    skipped_count = 0
    error_count = 0
    
    for idx, video_info in enumerate(VIDEO_METADATA, 1):
        filename = video_info['filename']
        video_path = os.path.join(VIDEO_FOLDER, filename)
        
        print(f"[{idx}/{len(VIDEO_METADATA)}] Processing: {filename}")
        
        # Check if file exists
        if not os.path.exists(video_path):
            print(f"  ⚠ SKIPPED - File not found: {video_path}")
            skipped_count += 1
            continue
        
        # Check if already uploaded
        existing = WorkoutVideo.objects.filter(
            title=video_info['title'],
            uploaded_by=trainer
        ).first()
        
        if existing:
            print(f"  ⚠ SKIPPED - Already exists: {video_info['title']}")
            skipped_count += 1
            continue
        
        try:
            # Set weight difference based on difficulty
            if video_info['difficulty_level'] == 'beginner':
                min_weight_diff = 0
                max_weight_diff = 10
            else:  # advanced
                min_weight_diff = 11
                max_weight_diff = 30
            
            # Open and read video file
            with open(video_path, 'rb') as video_file:
                from django.core.files.base import ContentFile
                video_content = ContentFile(video_file.read(), name=filename)
                
                # Create video record
                video = WorkoutVideo.objects.create(
                    title=video_info['title'],
                    description=video_info['description'],
                    video_file=video_content,
                    goal_type=video_info['goal_type'],
                    difficulty_level=video_info['difficulty_level'],
                    min_weight_difference=min_weight_diff,
                    max_weight_difference=max_weight_diff,
                    duration=video_info.get('duration'),
                    uploaded_by=trainer
                )
                
                print(f"  ✓ UPLOADED: {video.title}")
                print(f"    - Goal: {video.goal_type}")
                print(f"    - Difficulty: {video.difficulty_level}")
                print(f"    - Weight Range: {min_weight_diff}-{max_weight_diff}kg")
                uploaded_count += 1
                
        except Exception as e:
            print(f"  ✗ ERROR uploading {filename}: {str(e)}")
            error_count += 1
    
    print("\n" + "="*80)
    print("UPLOAD SUMMARY")
    print("="*80)
    print(f"✓ Uploaded: {uploaded_count}")
    print(f"⚠ Skipped:  {skipped_count}")
    print(f"✗ Errors:   {error_count}")
    print(f"Total:      {len(VIDEO_METADATA)}")
    print("\n✅ Upload process complete!")
    
    # Show all videos in database
    all_videos = WorkoutVideo.objects.filter(uploaded_by=trainer, is_active=True).order_by('goal_type', 'difficulty_level')
    print(f"\nTotal videos in database for {trainer.user.name}: {all_videos.count()}")
    print("\nCurrent videos by category:")
    
    for goal in ['weight_gain', 'weight_loss', 'muscle_gain', 'muscle_building', 'others']:
        goal_videos = all_videos.filter(goal_type=goal)
        if goal_videos.exists():
            print(f"\n{goal.upper().replace('_', ' ')}:")
            for v in goal_videos:
                print(f"  - [{v.difficulty_level}] {v.title}")


if __name__ == '__main__':
    print("\n⚠ IMPORTANT: Make sure you have:")
    print("  1. Created the video folder and placed your videos inside")
    print("  2. Updated VIDEO_FOLDER path in this script")
    print("  3. Updated TRAINER_ID in this script")
    print("  4. Updated VIDEO_METADATA with your video information")
    print("\nPress Enter to continue or Ctrl+C to cancel...")
    
    try:
        input()
        upload_videos()
    except KeyboardInterrupt:
        print("\n\n✗ Upload cancelled by user.")
        sys.exit(0)
