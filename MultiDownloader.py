import requests,re,datetime,json
class Downloader:
    def __init__(self, Username, Link, Password, Private):
        self.Username =self.Link=self.Password=""
        self.Private = False
    class InstaWeb:
        def __init__(self):
            None
        #web = https://www.instagram.com/p/CGXmUGDjA3V/
        #mobile = https://www.instagram.com/p/CGXmUGDjA3V/?igshid=r1020202020
        def GetData(self,Link,Private=False):
            if not Link.endswith("/"):
                str(Link) + "/"
            url = str(Link)+"?__a=1"
            if Private == False:
                r = requests.get(url)
            elif Private == True:
                r = requests.get(url, headers={"Cookie": InstaLogin(input("Username => "), input("Password => "))})
            content = json.loads(r.content)
            r.close()
            return content
        def Download(self, Filename, Data):
            content = Data['graphql']['shortcode_media']
            if content['__typename'] == "GraphImage":
                r = requests.get(content['display_url'])
                with open(Filename + ".png", "wb") as f:
                    f.write(r.content)
            elif content['__typename'] == "GraphVideo":
                r = requests.get(content['video_url'])
                with open(Filename + ".mp4", "wb") as f:
                    f.write(r.content)
            elif content['__typename'] == "GraphSidecar":
                for index,x in enumerate(content['edge_sidecar_to_children']['edges'], start=1):
                    if x['node']['__typename'] == "GraphVideo":
                        # print(x)
                        # exit()
                        r = requests.get(x['node']['video_url'])
                        with open(str(index) + "-" + Filename + ".mp4", "wb") as f:
                            f.write(r.content)
                    elif x['node']['__typename'] == "GraphImage":
                        r = requests.get(x['node']['display_url'])
                        with open(str(index) + "-" + Filename + ".png", "wb") as f:
                            f.write(r.content)
            r.close()
        def GetUrl(self, Data):
            content = Data['graphql']['shortcode_media']
            if content['__typename'] == "GraphImage":
                return content['display_url']
            elif content['__typename'] == "GraphVideo":
                return content['video_url']
            elif content['__typename'] == "GraphSidecar":
                urls = []
                for x in content['edge_sidecar_to_children']['edges']:
                    urls.append(x)
                return urls
    class InstaMobile:
        def __init__(self):
            None
        def GetData(self, Link, Private=False):
            url = str(Link.split("?")[0])
            url += "?__a=1"
            if Private == False:
                r = requests.get(url)
            elif Private == True:
                r = requests.get(url, headers={"Cookie": InstaLogin(input("Username => "), input("Password => "))})
            content = json.loads(r.content)
            r.close()
            return content
        def Download(self, Filename, Data):
            content = Data['graphql']['shortcode_media']
            if content['__typename'] == "GraphImage":
                r = requests.get(content['display_url'])
                with open(Filename + ".png", "wb") as f:
                    f.write(r.content)
            elif content['__typename'] == "GraphVideo":
                r = requests.get(content['video_url'])
                with open(Filename + ".mp4", "wb") as f:
                    f.write(r.content)
            elif content['__typename'] == "GraphSidecar":
                for x in content['edge_sidecar_to_children']['edges']:
                    if x['node']['__typename'] == "GraphVideo":
                        r = requests.get(x['video_url'])
                        with open(Filename, "wb") as f:
                            f.write(r.content)
                    elif x['node']['__typename'] == "GraphImage":
                        r = requests.get(x['display_url'])
                        with open(Filename + ".png", "wb") as f:
                            f.write(r.content)
            r.close()
        def GetUrl(self, Data):
            content = Data['graphql']['shortcode_media']
            if content['__typename'] == "GraphImage":
                return content['display_url']
            elif content['__typename'] == "GraphVideo":
                return content['video_url']
            elif content['__typename'] == "GraphSidecar":
                urls = []
                for x in content['edge_sidecar_to_children']['edges']:
                    urls.append(x)
                return urls
    class Snapchat:
        def __init__(self):
            None
        def GetData(self, Username):
            rHeaders = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0",
                "Referer": "http://play.snapchat.com/" + Username + "?upnext=1&loop=true"
            }
            r = requests.get("https://storysharing.snapchat.com/v1/fetch/" + Username, headers=rHeaders)
            content = json.loads(r.content)
            return content
        def Download(self, Filename, Data):
            content = Data
            for index,x in enumerate(content['story']['snaps'], start=1):
                with open(str(index) + "-" + Filename + ".mp4" if x['media']['type'] == "VIDEO" else ".png", "wb") as f:
                    r = requests.get(x['media']['mediaUrl'])
                    f.write(r.content)
        def GetUrl(self, Data):
            urls = []
            content = Data
            for url in content['story']['snaps']:
                urls.append(url)
            return urls
    class Twitter:
        def __init__(self):
            None
        def GetData(self, Link):
            code = Link.split("/")[-1]
            rHeaders = {
                "Accept": "*/*",
                "Accept-Languange": "ar,en-US;q=0.7,en;q=0.3",
                "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs=1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
                "Cookie": "_ga=GA1.2.1054613344.1468150257; des_opt_in=Y; dnt=1; kdt=js8OFucP58RCdgvum1EqZvKP3WjteBM5XCtpC3qU; remember_checked_on=1; csrf_same_site_set=1; csrf_same_site=1; night_mode=1; lang=en; personalization_id="+ "\"v1_PJpsqN6fGbfikDq1JmDJew==\"; guest_id=v1:160287544378302956; gt=1317181195881500673; ct0=ff2ad58fa62dc6328ed7d76a7ee6c7a4; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo",
                "Host": "twitter.com",
                "Referer": Link,
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0",
                "x-csrf-token": "ff2ad58fa62dc6328ed7d76a7ee6c7a4",
                "x-guest-token": "1317181195881500673",
                "x-twitter-active-user": "yes",
                "x-twitter-client-language": "ar"
            }
            r = requests.get("https://twitter.com/i/api/2/timeline/conversation/" + code+ ".json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_quote_count=true&include_reply_count=1&tweet_mode=extended&include_entities=true&include_user_entities=true&include_ext_media_color=true&include_ext_media_availability=true&send_error_codes=true&simple_quoted_tweet=true&referrer=app&controller_data=DAACDAAFDAABDAABDAABCgABAAAAAAAAAEAAAAwAAgoAAQAAAAAAAAAICgACAK1%2B4wDZaqILAAMAAAAZItmI2YTZitivINi52KjYr9in2YTZhNmHIgwABAwAAQsAAQAAABfZiNmE2YrYryDYudio2K%2FYp9mE2YTZhwsAAgAAACQwODY0OTFhYi0wMDMxLTQ3OTEtODk3Ny1lZmRhYjJlYjEwMTgAAAAAAAAA&count=20&include_ext_has_birdwatch_notes=false&ext=mediaStats%2ChighlightedLabel", headers=rHeaders, verify=False)
            # print(json.loads(r.content))
            content = json.loads(r.content)
            return [content, code]
        def Download(self, Filename, Data):
            for index,x in enumerate(Data[0]['globalObjects']['tweets'][Data[1]]['extended_entities']['media'], start=1):
                if x['type'] == "video":
                    for z in x['video_info']['variants']:
                        with open(str(index) + "-"+ Filename + ".mp4", "wb") as f:
                            f.write(requests.get(z['url']).content)
                        break
                elif x['type'] == "photo":
                    with open(str(index) + "-" + Filename + ".png", "wb") as f:
                        f.write(requests.get(x['media_url']).content)
        def GetUrl(self, Data):
            urls = []
            for x in Data[0]['globalObjects']['tweets'][Data[1]]['extended_entities']['media']:
                if x['type'] == "video":
                    for z in x['video_info']['variants']:
                        urls.append(z['url'])
                        break
                elif x['type'] == "photo":
                    urls.append(x['media_url'])
            return urls
def Unix():
    dt = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)
    timestamp = dt.replace(tzinfo=datetime.timezone.utc).timestamp()
    # print(timestamp)
    return timestamp
def InstaLogin(user, password):
    rHeaders= {"Accept": "*/*" , "Accept-Language": "ar,en-US;q=0.7,en;q=0.3" , "Content-Type": "application/x-www-form-urlencoded", "Cookie": "Y1z1n" , "Host": "www.instagram.com" , "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0" , "X-CSRFToken": "Y1z1n", "X-IG-App-ID": "936619743392459" , "X-Instagram-AJAX": "Y1z1n", "X-Requested-With": "XMLHttpRequest"}
    rData = {"username": user, "enc_password": "#PWD_INSTAGRAM_BROWSER:0:" + str(Unix())[:-4]+ ":"+password, "queryParams": "{}" , "optIntoOneTap": "false"}
    r = requests.post("https://www.instagram.com/accounts/login/ajax/" ,  headers=rHeaders , data=rData, verify=False)
    res = r.json()
    if "userId" in res:
        #print("Done login :)")
        csrf = str(r.headers)
        full_cookies = "".join(re.findall(r'csrftoken=.*?;', csrf)) +   "".join(re.findall(r'ds_user_id=.*?;', csrf)) + "".join(re.findall(r'ig_did=.*?;', csrf))  + "".join(re.findall(r'mid=.*?;', csrf)) + "".join(re.findall(r'rur=.*?;', csrf)) + "".join(re.findall(r'sessionid=.*?;', csrf)) + "".join(re.findall(r'shbid=.*?;', csrf)) + "".join(re.findall(r'shbts=.*?;', csrf))
        return full_cookies
    else:
        print("Wrong username or password, or a banned account")
        return False