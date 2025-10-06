import os, shutil

TYPES = {
    'Images': ['jpg','jpeg','png','gif','bmp','webp'],
    'Documents': ['pdf','txt','doc','docx','ppt','pptx','xls','xlsx','csv'],
    'Music': ['mp3','wav','flac','aac','ogg','m4a'],
    'Videos': ['mp4','avi','mkv','mov','wmv','flv'],
    'Archives': ['zip','rar','7z','tar','gz']
}

def ftype(name):
    ext = name.lower().rsplit('.',1)[-1] if '.' in name else ''
    for cat, exts in TYPES.items():
        if ext in exts: return cat
    return 'Others'

def show(folder):
    any_file = False
    print("\nFiles (recursive):")
    for root, _, fs in os.walk(folder):
        fs = [f for f in fs if os.path.isfile(os.path.join(root,f))]
        if not fs: continue
        rel = os.path.relpath(root, folder)
        print(f"\n[{'.' if rel=='.' else rel}]")
        for f in fs:
            print("-", f)
        any_file = True
    if not any_file:
        print("(none)")



def mkfolders(folder):
    for cat in list(TYPES)+['Others']:
        os.makedirs(os.path.join(folder,cat), exist_ok=True)

def organize(folder):
    if not os.path.isdir(folder):
        print("Folder not found."); return
    mkfolders(folder); moved = 0
    for f in os.listdir(folder):
        src = os.path.join(folder,f)
        if os.path.isfile(src):
            dest_dir = os.path.join(folder, ftype(f))
            shutil.move(src, os.path.join(dest_dir,f)); moved += 1
    print(f"Organized {moved} files.")

def helpmsg():
    print("\nOrganize files by type into folders (Images, Documents, Music, Videos, Archives, Others).")
    print("Provide a folder path for viewing or organizing.")

def main():
    while True:
        print("\n--- FILE ORGANIZER ---\n1) View files\n2) Organize files\n3) Help\n4) Exit")
        ch = input("Choose: ").strip()
        if ch == "1":
            d = input("Folder path: ").strip()
            if os.path.isdir(d): show(d)
            else: print("Folder not found.")
        elif ch == "2":
            d = input("Folder path: ").strip()
            organize(d)
        elif ch == "3":
            helpmsg()
        elif ch == "4":
            print("Goodbye!"); break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
