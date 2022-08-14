import os
import pyvenv.cfg

try:
    os.system("pip install -r requirements.txt")
    print("-> Successully installed requirements")
except Exception as e:
    print(f"! Failed to install requirements: {e}")
