import os
import subprocess
print("Building development environment...")
try:
    subprocess.run(["mkdir", "Titanfall2"])
    os.chdir("Titanfall2")
    with open("Titanfall2.exe", "w") as f:
        pass
    subprocess.run(["mkdir", "vpk"])
except Exception:
    print("One or more things went wrong with the build. Stop")
print("Development environment built successfully!")