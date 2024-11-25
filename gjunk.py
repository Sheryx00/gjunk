import os
import shutil

# File extension groups
EXTENSIONS = {
    "img": [
        '.jpeg', '.jpg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.webp', '.ico', '.svg', 
        '.heif', '.heic', '.raw', '.arw', '.nef'
    ],
    "db": [
        '.sql', '.db', '.sqlite', '.sqlite3', '.mdb', '.accdb', '.dump', '.bak'
    ],
    "text": [
        '.txt', '.md', '.markdown', '.rst'
    ],
    "cloud": [
        '.json', '.yaml', '.yml', '.tf', '.cloud', '.kubeconfig', '.ini', '.cfg', '.env'
    ],
    "code": [
        '.py', '.java', '.js', '.html', '.css', '.cpp', '.c', '.sh', '.bat', '.php', '.cs', 
        '.go', '.ts', '.rb', '.rs'
    ]
}

def copy_files(src_folder, dest_folder, file_extensions=None):
    """
    Copy files matching specified extensions to the destination folder.
    If file_extensions is None, copy all files not matched to 'unknown'.
    """
    os.makedirs(dest_folder, exist_ok=True)

    for root, dirs, files in os.walk(src_folder):
        for file in files:
            # Skip files already in the gjunk folder
            if gjunk_folder in root:
                continue

            if file_extensions is None or any(file.lower().endswith(ext) for ext in file_extensions):
                src_path = os.path.join(root, file)
                dest_path = os.path.join(dest_folder, file)

                # Handle filename conflicts
                if os.path.exists(dest_path):
                    base_name, ext = os.path.splitext(file)
                    counter = 1
                    while os.path.exists(dest_path):
                        dest_path = os.path.join(dest_folder, f"{base_name}_{counter}{ext}")
                        counter += 1

                # Copy the file
                shutil.copy2(src_path, dest_path)  # copy2 preserves metadata

# Set source to the current working directory
src_folder = os.getcwd()

# Main junk folder
gjunk_folder = os.path.join(src_folder, "gjunk")
os.makedirs(gjunk_folder, exist_ok=True)

# Organize files into their respective categories
for category, extensions in EXTENSIONS.items():
    category_folder = os.path.join(gjunk_folder, category)
    copy_files(src_folder, category_folder, extensions)

# Handle files with unknown extensions
unknown_folder = os.path.join(gjunk_folder, "unknown")
copy_files(src_folder, unknown_folder)

