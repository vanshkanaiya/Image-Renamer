# RenameImage

A small Python command-line tool for batch-renaming image files in a folder.

## Downloads

A Windows executable (`.exe`) is coming soon. Until then, run the script with Python using the instructions below.

It renames supported images using a base name and number sequence, for example:

```text
holiday.jpg  -> IMG_0.jpg
photo.png    -> IMG_1.png
picture.webp -> IMG_2.webp
```

Existing numbered files are protected. If `IMG_0.jpg` through `IMG_6.jpg` already exist, the next matching image is renamed to `IMG_7.jpg` instead of overwriting a file.

## Requirements

- Python 3

No additional packages are required.

## How to run

From this project folder, run:

```bash
python rename.py
```

Then:

1. Enter the full path of the image folder.
2. Enter the base name you want to use, such as `IMG`.
3. Review the confirmation prompt and enter `y` to rename the files.

## Supported image types

- PNG
- JPG / JPEG
- GIF
- BMP
- WEBP

## Notes

- Files are processed in alphabetical order.
- Image extensions are kept and converted to lowercase.
- The script only processes files directly inside the selected folder; it does not scan subfolders.
- Make a copy of important images before batch-renaming them.
