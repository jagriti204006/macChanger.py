import subprocess
import optparse 

# subprocess.run("ifconfig", shell=True)

def change(interface, mac):
    subprocess.run("ifconfig "+interface+" down", shell=True)
    subprocess.run("ifconfig "+interface+" hw ether "+mac, shell=True)

    subprocess.run("ifconfig "+interface+" up", shell=True)

def getArguments():
    parser = optparse.OptionParser()
  
    parser.add_option("-i", "--interface", dest="interface", help="interface name of the target")
    parser.add_option("-m", "--mac", dest="mac", help="new mac address you want to assign to the target")
    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("Please specify the interface name ")
    if not options.mac:
        parser.error("Please specify the new mac address ")

    return options

options = getArguments()
change(options.interface, options.mac)

print("Mac address changed")
