import subprocess

logs = subprocess.getoutput("docker logs selfheal-container")

if "ModuleNotFoundError" in logs:
    print("Root Cause: Missing dependency")
    subprocess.call("docker build -t selfheal-app app/", shell=True)

elif "Address already in use" in logs:
    print("Root Cause: Port conflict")
    subprocess.call("docker restart selfheal-container", shell=True)

else:
    print("Unknown issue, manual check needed")
