from pathlib import Path
import shutil
folder=Path(r"C:\Users\Admin\OneDrive\Desktop\FileOrganizerPractice")
print("folder exists:", folder.exists())
print("items inside folder:",list(folder.iterdir()))
dry_run=True
choice=input("do you want to organize files?(yes/no):").strip().lower()
while True:
    if choice.lower() not in ["yes","no"]:
        choice=input("please enter yes or no:")
    else:
        break
if choice.lower()=="yes":
    dry_run=False
else:
    dry_run=True
for items in list(folder.iterdir()):
    if items.is_file():
        extension=items.suffix.lower()
        print(items.stem,"extension:",extension)
        if extension in [".jpg",".jpeg",".png",".gif"]:
            category="images"      
        elif extension==".mp4" or extension==".mkv":
            category="videos"
        elif extension==".pdf" or extension==".txt":
            category="documents"
        else:
            category="others"
        print(items.name, "->", category)
        destination=folder/category
        if dry_run:
            print("[DRY-RUN]=",items.name, "->", destination/items.name)
        else:
            destination.mkdir(exist_ok=True)
            target=destination/items.name
            if target.exists():
                print(f"File {target} already exists.")
            else:
                shutil.move(str(items),str(target))