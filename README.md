# piwifi
Python module to manage wpa_supplicant wifi networks on Raspberry Pi  

Original repo: https://github.com/jeffleary00/piwifi/
## Fork
The edits and setup from this fork got it working for me.  Tested on Pi 3B+
#
## Setup

Overwrite file:  /etc/wpa_supplicant/wpa_supplicant.conf  

File should have these lines only (needed to use wpa_cli):

```bash
ctrl_interface=/run/wpa_supplicant
update_config=1
```



File:  /etc/network/interfaces  

depends on system, but on raspberry pi 3B+ I believe this is the default (worked for me):

```bash
source-directory /etc/network/interfaces.d

auto lo
iface lo inet loopback

auto eth0
iface eth0 inet manual

allow-hotplug wlan0
iface wlan0 inet manual
    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf

allow-hotplug wlan1
iface wlan1 inet manual
    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
```


Edit the piwifi_test.py with your configuration and run it
```bash
python3 piwifi_test.py
```