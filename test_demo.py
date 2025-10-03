# FileForge Demo
# Creates sample files to test the organizer

import os

def create_test_files():
    """Create sample files for testing"""
    test_folder = "test_folder"
    
    # Create test folder
    if not os.path.exists(test_folder):
        os.makedirs(test_folder)
        print(f"📁 Created test folder: {test_folder}")
    
    # Sample files to create
    test_files = [
        "vacation_photo.jpg",
        "project_report.pdf", 
        "favorite_song.mp3",
        "funny_video.mp4",
        "homework.txt",
        "profile_pic.png",
        "presentation.zip",
        "backup.rar",
        "notes.doc",
        "music_file.wav"
    ]
    
    # Create empty test files
    for filename in test_files:
        filepath = os.path.join(test_folder, filename)
        with open(filepath, 'w') as f:
            f.write(f"# Test file: {filename}\n")
        print(f"📄 Created: {filename}")
    
    print(f"\n✅ Created {len(test_files)} test files in '{test_folder}' folder")
    print("Now run: python simple_fileforge.py")
    print(f"And organize the '{test_folder}' folder to see it work!")

if __name__ == "__main__":
    create_test_files()