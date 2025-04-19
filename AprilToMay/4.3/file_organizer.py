import os


def create_directories():

    if not os.path.exists('MyFiles'):
        os.makedirs('MyFiles')
        print("Directory 'MyFiles' created.")
    else:
        print("Directory 'MyFiles' already exists.")
        
    subdirectories = ['Docs', 'Images', 'Videos', ]
    
    for subdir in subdirectories:
        sub_path = os.path.join('MyFiles', subdir)
        if not os.path.exists(sub_path):
            os.makedirs(sub_path)
            print(f"Subdirectory '{subdir}' created.")
        else:
            print(f"Subdirectory '{subdir}' already exists.")

if __name__ == "__main__":
    create_directories()