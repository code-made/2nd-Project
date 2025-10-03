# File Organizer 

import os
import shutil

def show_files_in_folder(folder_path):
    """Show all files in a folder"""
    print(f"\n📁 Files in '{folder_path}':")
    print("-" * 40)
    
    files = []
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):  # Only show files, not folders
            files.append(item)
    
    if not files:
        print("No files found!")
        return []
    
    for i, file in enumerate(files, 1):
        print(f"{i}. {file}")
    
    return files

def get_file_type(filename):
    """Determine what type of file it is"""
    # Get the file extension (like .jpg, .pdf, .txt)
    extension = filename.lower().split('.')[-1]
    
    # Simple rules for file types
    if extension in ['jpg', 'jpeg', 'png', 'gif']:
        return 'Images'
    elif extension in ['pdf', 'txt', 'doc', 'docx']:
        return 'Documents'
    elif extension in ['mp3', 'wav', 'flac']:
        return 'Music'
    elif extension in ['mp4', 'avi', 'mkv']:
        return 'Videos'
    elif extension in ['zip', 'rar', '7z']:
        return 'Archives'
    else:
        return 'Others'

def create_folders(folder_path):
    """Create organized folders"""
    folder_types = ['Images', 'Documents', 'Music', 'Videos', 'Archives', 'Others']
    
    created_folders = []
    for folder_type in folder_types:
        new_folder = os.path.join(folder_path, folder_type)
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
            created_folders.append(folder_type)
            print(f"✅ Created folder: {folder_type}")
    
    if created_folders:
        print(f"📁 Created {len(created_folders)} new folders!")
    else:
        print("📁 All folders already exist!")

def organize_files(folder_path):
    """Move files into organized folders"""
    print(f"\n🔄 Organizing files in '{folder_path}'...")
    
    # Get all files in the main folder (not in subfolders)
    files_to_organize = []
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            files_to_organize.append(item)
    
    if not files_to_organize:
        print("No files to organize!")
        return
    
    # Create organized folders first
    create_folders(folder_path)
    
    # Move each file to its proper folder
    files_moved = 0
    for filename in files_to_organize:
        try:
            # Figure out what type of file it is
            file_type = get_file_type(filename)
            
            # Create source and destination paths
            source = os.path.join(folder_path, filename)
            destination_folder = os.path.join(folder_path, file_type)
            destination = os.path.join(destination_folder, filename)
            
            # Move the file
            shutil.move(source, destination)
            print(f"📦 Moved: {filename} → {file_type}/")
            files_moved += 1
            
        except Exception as e:
            print(f"❌ Error moving {filename}: {e}")
    
    print(f"\n✅ Successfully organized {files_moved} files!")

def main():
    """Main program"""
    print("🗂️ SIMPLE FILE ORGANIZER")
    print("=" * 40)
    print("This program organizes your files into neat folders!")
    print("Files will be sorted into: Images, Documents, Music, Videos, Archives, Others")
    
    while True:
        print("\n" + "=" * 40)
        print("📋 MENU:")
        print("1. 👀 View files in a folder")
        print("2. 🗂️ Organize files in a folder") 
        print("3. ❓ Help - What does this do?")
        print("4. 🚪 Exit")
        print("-" * 40)
        
        choice = input("Choose option (1-4): ").strip()
        
        if choice == "1":
            folder = input("\nEnter folder path to view: ").strip()
            if folder and os.path.exists(folder):
                show_files_in_folder(folder)
            else:
                print("❌ Folder not found! Make sure the path is correct.")
        
        elif choice == "2":
            folder = input("\nEnter folder path to organize: ").strip()
            if folder and os.path.exists(folder):
                # Show what files are there first
                files = show_files_in_folder(folder)
                if files:
                    confirm = input("\n🤔 Do you want to organize these files? (y/n): ").lower()
                    if confirm == 'y':
                        organize_files(folder)
                    else:
                        print("❌ Organization cancelled.")
            else:
                print("❌ Folder not found! Make sure the path is correct.")
        
        elif choice == "3":
            print("\n❓ HELP - What does this program do?")
            print("-" * 50)
            print("📝 This program helps you organize messy folders!")
            print("\n🔍 How it works:")
            print("1. You give it a folder path (like C:\\Downloads)")
            print("2. It looks at all your files")
            print("3. It creates organized folders (Images, Documents, etc.)")
            print("4. It moves files into the right folders based on their type")
            print("\n📂 File Types:")
            print("• Images: .jpg, .png, .gif files → Images folder")
            print("• Documents: .pdf, .txt, .doc files → Documents folder") 
            print("• Music: .mp3, .wav files → Music folder")
            print("• Videos: .mp4, .avi files → Videos folder")
            print("• Archives: .zip, .rar files → Archives folder")
            print("• Others: Everything else → Others folder")
            print("\n💡 Example:")
            print("Before: folder/photo.jpg, song.mp3, document.pdf")
            print("After: folder/Images/photo.jpg, folder/Music/song.mp3, folder/Documents/document.pdf")
        
        elif choice == "4":
            print("\n👋 Thanks for using Simple File Organizer!")
            print("🎉 Keep your files organized!")
            break
        
        else:
            print("❌ Invalid choice! Please choose 1-4.")

# Run the program
if __name__ == "__main__":
    main()