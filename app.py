import os
import platform
from datetime import datetime

def main():
    name = os.getenv("STUDENT_NAME", "Dilnur")
    surname = os.getenv("STUDENT_SURNAME", "Satibaldiyev")
    group = os.getenv("STUDENT_GROUP", "IT2-2304")
    student_id = os.getenv("STUDENT_ID", "38036")

    print("=" * 40)
    print("DevOps Student Application")
    print("=" * 40)
    print(f"Name: {name}")
    print(f"Surname: {surname}")
    print(f"Group: {group}")
    print(f"Student ID: {student_id}")
    print(f"Operating System: {platform.system()}")
    print(f"Current Date: {datetime.now().isoformat(timespec='seconds')}")
    print("Application is running successfully!")

if __name__ == "__main__":
    main()
