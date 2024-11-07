import os

def create_structure():
    # Define the folders and files to create
    folders = ['folder1', 'folder2', 'folder3']
    files = ['file1.txt', 'file2.txt', 'file3.txt']

    # Create folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")

    # Create files
    for file in files:
        with open(file, 'w') as f:
            f.write('')  # Create an empty file
        print(f"Created file: {file}")

if __name__ == "__main__":
    create_structure()