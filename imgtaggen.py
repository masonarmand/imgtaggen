"""
file: imgtaggen.py
author: Mason Armand

This is a super simple script that creates a text file containing html
<img> tags for all files in a directory.
"""
import os

# text file containing tags
TAGS_FILE = '_tags.txt'

# tuple containing file types/extensions
IMAGE_TYPES = (
    '.png', '.gif', '.jpeg', '.jpg', '.webp', '.jfif'
)


def main():
    """ Append html <img> tags to TAGS_FILE """

    for _, _, files in os.walk(r'.'):
        for file in files:
            if not file.lower().endswith(IMAGE_TYPES):
                continue

            print(f'Adding {file} to {TAGS_FILE}...')

            # open file "tags.txt" for writing and add the <img> tag to it
            with open(TAGS_FILE, "a", encoding="utf-8") as text_file:
                text_file.write(f'<img src="{file}">\n')
                text_file.close()


if __name__ == "__main__":
    main()
