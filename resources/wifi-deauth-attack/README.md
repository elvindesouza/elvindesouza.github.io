![Maintenance](https://img.shields.io/maintenance/no/2020)
[![GitHub issues](https://img.shields.io/github/issues/veerendra2/wifi-deauth-attack.svg)](https://github.com/veerendra2/wifi-deauth-attack/issues)
[![GitHub forks](https://img.shields.io/github/forks/veerendra2/wifi-deauth-attack.svg)](https://github.com/veerendra2/wifi-deauth-attack/network)
[![GitHub stars](https://img.shields.io/github/stars/veerendra2/wifi-deauth-attack.svg)](https://github.com/veerendra2/wifi-deauth-attack/stargazers)
[![GitHub license](https://img.shields.io/badge/license-Apache%202-blue.svg)](https://raw.githubusercontent.com/veerendra2/wifi-deauth-attack/master/LICENSE)
[![Twitter](https://img.shields.io/twitter/url/https/github.com/veerendra2/wifi-deauth-attack.svg?style=social)](https://twitter.com/intent/tweet?text=Wow:&url=%5Bobject%20Object%5D)
# Wifi Deauthentication Attack
Sends `deauth`(deauthentication) packets to wifi network which results network outage for connected devices. Uses `scapy` module to send `deauth` packets.
Know more about [Deauthentication Attack](https://en.wikipedia.org/wiki/Wi-Fi_deauthentication_attack)

### Dependencies
1. aircrack-ng.(I highly recommend to install latest version, from [source](https://www.aircrack-ng.org/downloads.html) to support more network drivers/cards.) 
   * `sudo apt-get install aircrack-ng -y`
2. scapy
   * `sudo apt-get install python-scapy -y`

### How to run?
We can run in 2 ways:
* `sudo python deauth.py` 
 
   It will automatically creates `mon0` with `airmon-ng start wlan0`(it wont create, if already exists) and sniffs the wifi  signal on that interface. After few seconds, it will displays the `SSID` and its `MAC` to choose.
* `sudo python deauth.py -m XX:YY:AA:XX:YY:AA` 
   
   MAC address as command line argument. In this case, there is no need to sniff wifi.

### What's new in version 3.1
* Daemonize the attack i.e performs attack in background
* Compatable to new `airmon-ng` version
* Able to detect different wireless interface name(like `wlp13s0`)
* Kill daemon option
* Now you can get wifi networks with [`iwlist`](https://linux.die.net/man/8/iwlist) tool (Relatively faster) 
### Usage
```
root@ghost:/opt/scripts#./deauth.py -h
usage: deauth.py [-h] [-d] [-c COUNT] [-m MAC] [-w] [-k] [-v]

Sends deauthentication packets to a wifi network which results network outage
for connected devices. [Coded by VEERENDRA KAKUMANU]

optional arguments:
  -h, --help  show this help message and exit
  -d          Run as daemon
  -c COUNT    Stops the monitoring after this count reachs. By default it is
              2000
  -m MAC      Sends deauth packets to this network
  -w          Uses "iwlist" to get wifi hotspots list
  -k          Kills "Deauth Daemon" if it is running
  -v          show program's version number and exit
```
![In Action](https://raw.githubusercontent.com/veerendra2/wifi-deauth-attack/master/blog-image2.jpg)

### FAQ
* ##### What is the option `-c` "COUNT"?
  
  It is a threshold value to stop the "monitoring". The access point or wifi hotspot trasmits [beacon frames](https://en.wikipedia.org/wiki/Beacon_frame) periodically to announce it's presence. The beacon frame contains all the information about the network. Now, the script looks for these beacons and makes count. If the count reachs the limit, it will stops the monitoring.
  * If you think, the monoring is taking to much time? then specify the count with less number(Default is 2000), but it may not get all wifi hotspots near to you. Because you are listening only few beacons

* ##### What is the option `-w` "Uses "iwlist" to get wifi hotspots list"?

  Script runs `iwlist wlan0 s` and gets wifi networks near to you

* ##### What is the option `-d` "Run as daemon"?
  
  Script runs in background while attacking. (Use option `-k` to kill)

### Known Issues
* For some reasons, sometimes the script is not able to find all near wifi hotspots.(Use `-w` option)
* If you try to attack on a wifi hotspot which is created by "Android" device, it won't work!.(May be it uses `802.11w`)
* Don't run the script with `-w` continously twice or more, you may get below error. If this is the case, restart `network-manager`; `sudo service network-manager restart`
  * `wlp13s0   Interface doesn't support scanning : Device or resource busy`

#### Get it!
`wget -qO deauth.py https://goo.gl/bnsV9C`

### How to avoid Deauthentication attack?
Use `802.11w` suppored routers. Know more about [802.11w](https://en.wikipedia.org/wiki/IEEE_802.11w-2009) and [read cisco document](http://www.cisco.com/c/en/us/td/docs/wireless/controller/technotes/5700/software/release/ios_xe_33/11rkw_DeploymentGuide/b_802point11rkw_deployment_guide_cisco_ios_xe_release33/b_802point11rkw_deployment_guide_cisco_ios_xe_release33_chapter_0100.pdf)

#### NOTE: 
In order to work deauthentication attack successful, you should near to the target network. The `deauth` packets should reach the connected devices of the target network(s)

#### Blog: https://veerendra2.github.io/wifi-deathentication-attack/
