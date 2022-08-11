import os

try:
    os.system("pip freeze > requirements.txt")
    print("-> Successully updated requirements.txt")
except Exception as e:
    print(f"! Failed to update requirements.txt: {e}")