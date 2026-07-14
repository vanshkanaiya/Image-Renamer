import os

# Ask the user to input the folder path
folder_path = input("Enter the full path to your image folder: ").strip()

# Remove quotes if the user dragged and dropped the folder into the terminal
folder_path = folder_path.strip("'\"")

# Check if the path actually exists
if not os.path.exists(folder_path):
    print("Error: That folder path does not exist. Please check it and try again.")
    exit()

# Only target these image types
image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')

# Get and sort the files so they rename in order
files = sorted(os.listdir(folder_path))

# Filter the list first to count how many images will be changed
images_to_rename = [f for f in files if f.lower().endswith(image_extensions)]
total_images = len(images_to_rename)

# If no images are found, stop early
if total_images == 0:
    print("No matching image files found in that folder.")
    exit()

name = input("Enter the base name for the images (e.g., 'IMG' will result in IMG_0, IMG_1, etc.): ").strip()

# Ask the user for confirmation
print(f"\nFound {total_images} images in the folder.")
confirm = input(f"Are you sure you want to rename these using the base name '{name}'? (y/n): ").strip().lower()

if confirm != 'y':
    print("Operation cancelled. No files were renamed.")
    exit()

# Start the count at 0
count = 0
renamed_count = 0
skipped_count = 0
existing_names = set(files)

# Files that already use this naming format must never be renamed. They reserve
# their number, so a later file will move on to the next available number.
already_numbered = set()
prefix = f"{name}_"
for filename in images_to_rename:
    stem, _ = os.path.splitext(filename)
    if stem.startswith(prefix) and stem[len(prefix):].isdigit():
        already_numbered.add(filename)

for filename in images_to_rename:
    # Keep the original file extension (.jpg, .png, etc.)
    _, ext = os.path.splitext(filename)

    # Keep pre-existing names such as IMG_6.jpg unchanged.
    if filename in already_numbered:
        print(f"Skipped: {filename} already has a numbered name")
        skipped_count += 1
        continue

    while True:
        # Build the next available name: IMG_0, IMG_1, etc.
        new_name = f"{name}_{count}{ext.lower()}"

        # Do not overwrite an existing file; try the next number instead.
        if new_name in existing_names:
            print(f"Name already in use: {new_name}; trying the next number")
            count += 1
            continue

        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        existing_names.remove(filename)
        existing_names.add(new_name)
        print(f"Renamed: {filename} -> {new_name}")
        renamed_count += 1
        count += 1
        break

print(f"\nFinished! Renamed {renamed_count} images and skipped {skipped_count} already-correct names.")
