from PIL import Image
import os
import hashlib
from colorama import Fore, Style, init

init(autoreset=True)

def get_hash(file):
    with open(file, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

print(Fore.CYAN + "=" * 55)
print(Fore.YELLOW + "- DUPLICATE IMAGE CLEANER TOOL")
print(Fore.GREEN + "- Created by: ABHIRAM")
print(Fore.MAGENTA + "- Instagram: themabhiram (https://www.instagram.com/themabhiram/)")
print(Fore.CYAN + "=" * 55)

print(Fore.RED + "\n WARNING: This tool can delete files permanently!\n")

folder = input(Fore.WHITE + "Enter folder path: ")

hashes = {}
duplicates = []

for file in os.listdir(folder):
    path = os.path.join(folder, file)

    if os.path.isfile(path) and file.lower().endswith((".png", ".jpg", ".jpeg")):
        file_hash = get_hash(path)

        if file_hash in hashes:
            duplicates.append((file, path))
        else:
            hashes[file_hash] = path

# Show only names
if not duplicates:
    print(Fore.GREEN + "\nNo duplicate images found ")
else:
    print(Fore.YELLOW + "\nDuplicate files found:")
    for name, _ in duplicates:
        print(Fore.RED + name)

    choice = input(Fore.WHITE + "\nDo you want to delete duplicates? (yes/no): ").lower()

    if choice == "yes":
        for name, path in duplicates:
            try:
                os.remove(path)
                print(Fore.GREEN + f"Deleted: {name}")
            except:
                print(Fore.RED + f"Failed: {name}")
        print(Fore.CYAN + "\nDone cleaning duplicates ")
    else:
        print(Fore.YELLOW + "\nNo files were deleted ")

input(Fore.MAGENTA + "\nThanks for using! Follow @themabhiram (https://www.instagram.com/themabhiram/)\nPress Enter to exit...")