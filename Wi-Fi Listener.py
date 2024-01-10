import subprocess

def get_wifi_list():
    try:
        result = subprocess.check_output(["netsh", "wlan", "show", "network"])
        result = result.decode("ascii")
        wifi_list = result.replace("\r", "").split("\n")
        wifi_list = wifi_list[4:-2]  # Remove unnecessary lines from the output
        return wifi_list
    except subprocess.CalledProcessError:
        return []

wifi_networks = get_wifi_list()
for network in wifi_networks:
    print(network)

# Enjoy!!!
