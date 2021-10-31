from piwifi_lib import WpaManager

ssid_input = "Your wifi ssid"
ssid_password = "Your wifi password"

# Possible parameters for WpaManager():
    # sudo=False   - run command with sudo?
    # wpa_cli="path/to/wpa_cli"   - nonstandard path to wpa_cli?
    # dhcp=True   - need to run dhcp to get IP address assigned from router?
    # interface="wlan0"  - this is the default RPI wifi card
    # debug=False   - Make this true to see a bunch of print statements in the library

m = WpaManager(sudo=True)

m.add_network( {'ssid': ssid_input, 'psk': ssid_password} )

exit()

# If you like, there is also a scanner in this library which can be used like so:

from piwifi_lib import Scanner
s = Scanner(interface=wifi_interface, sudo=True)

list_of_networks = s.cells
strongest_signal = s.strongest_channel()
quietest_signal = s.quietest_channel()
