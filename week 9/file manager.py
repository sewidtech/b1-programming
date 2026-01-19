import os

def file_manager():
    current_dir = os.getcwd()
    print(f'current directory: {current_dir}\n')

    foldername = 'Exfile'
    os.makedirs(foldername, exist_ok=True)

    file_names = ["file1.txt", "file2.txt", "file3.txt"]
    for name in file_names:
        with open(os.path.join(foldername, name), 'w') as f:
            f.write(f"this is {name}")

    old_path = os.path.join(foldername, 'file3.txt')
    new_path = os.path.join(foldername, 'renamed.txt')
    os.rename(old_path, new_path)

    print("\nFiles after rename:")
    for file in os.listdir(foldername):
        print(file)

    for file in os.listdir(foldername):
        os.remove(os.path.join(foldername, file))

    os.rmdir(foldername)
    print("\nAll cleanup completed successfully!")

file_manager()
