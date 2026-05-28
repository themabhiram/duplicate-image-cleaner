# duplicate-image-cleaner
A Python tool to find and delete duplicate images instantly.

# Duplicate Image Cleaner

A simple Python tool to find and delete duplicate images instantly.

## Features

* Detect duplicate images
* Delete duplicate files
* Supports JPG, JPEG, PNG
* Fast and simple

## Warning

This tool can permanently delete duplicate files.

Please review files carefully before deleting.

## Installation

Install requirements:

```bash
pip install -r requirements.txt
```

## Run Tool

```bash
python main.py
```

## Build EXE

```bash
pyinstaller --onefile --console --name Duplicate_Image_Cleaner main.py
```

## How To Use

1. Open the tool
2. Enter folder path

Example:

```text
C:\Users\YourName\Pictures
```

3. Wait for scan to complete
4. Review duplicate images
5. Type:

```text
yes
```

to delete duplicates

or

```text
no
```

to cancel.

## Notes

* Only exact duplicate images are detected
* Original image is not deleted
* Internet is not required

## Requirements

```text
colorama
pillow
```

Created by ABHIRAM

Instagram: @themabhiram

