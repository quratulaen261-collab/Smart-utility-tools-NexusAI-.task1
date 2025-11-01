import os
import shutil

def rename_files(folder, prefix):
    for i, name in enumerate(os.listdir(folder), 1):
        ext = os.path.splitext(name)[1]
        os.rename(os.path.join(folder, name), os.path.join(folder, f"{prefix}_{i}{ext}"))

def organize_files(folder):
    for file in os.listdir(folder):
        ext = os.path.splitext(file)[1].replace('.', '')
        if not ext: continue
        path = os.path.join(folder, ext)
        os.makedirs(path, exist_ok=True)
        shutil.move(os.path.join(folder, file), os.path.join(path, file))

