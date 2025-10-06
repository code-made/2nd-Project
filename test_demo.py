# FileForge Demo
# Creates sample files to test the organizer

import os

def create_test_files():
    """Create sample files for testing"""
    test = "test_folder"
    
    # Create test folder
    if not os.path.exists(test):
        os.makedirs(test)
        print(f"📁 Created test folder: {test}")
    
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
        filepath = os.path.join(test, filename)
        with open(filepath, 'w') as f:
            f.write(f"# Test file: {filename}\n")
        print(f"📄 Created: {filename}")
    
    print(f"\n✅ Created {len(test_files)} test files in '{test}' folder")
    print("Now run: python simple_fileforge.py")
    print(f"And organize the '{test}' folder to see it work!")

if __name__ == "__main__":
    create_test_files()