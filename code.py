import subprocess

# subprocess.run("ifconfig", shell=True)

subprocess.run("ifconfig wlan0 down", shell=True)
subprocess.run("ifconfig wlan0 hw ether C1:B1:23:82:67:AE", shell=True)

subprocess.run("ifconfig wlan0 up", shell=True)
