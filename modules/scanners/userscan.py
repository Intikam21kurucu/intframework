# usr/bin/env python3
# userscan.py
import argparse
from requests import get

services = [
    ['github.com/{}', 'github'],
    ['api.github.com/users/{}/events/public', 'github'],
    ['api.github.com/users/{}', 'github'],
    ['facebook.com/{}', 'facebook'],
    ['twitter.com/{}', 'twitter'],
    ['twitch.com/{}', 'twitch'],
    ['reddit.com/user/{}', 'reddit'],
    ['producthunt.com/@{}', 'producthunt'],
    ['steamcommunity.com/id/{}', 'steam'],
    ['myspace.com/{}', 'myspace'],
    ['deviantart.com/{}', 'deviantart'],
    ['last.fm/user/{}', 'last'],
    ['slideshare.net/{}', 'slideshare'],
    ['vk.com/{}', 'vk'],
    ['roblox.com/users/profile?username={}', 'roblox'],
    ['skyscanner.com/trip/user/{}', 'skyscanner'],
    ['pastebin.com/u/{}', 'pastebin'],
    ['en.wikipedia.org/w/api.php?action=query&format=json&list=allusers&auprefix={}&aulimit=10', 'wikipedia'],
    ['codementor.io/{}', 'codementor'],
    ['news.ycombinator.com/user?id={}', 'ycombinator'],
    ['500px.com/{}', '500px'],
    ['open.spotify.com/user/{}', 'spotify'],
    ['scribd.com/{}', 'scribd'],
    ['wattpad.com/user/{}', 'wattpad'],
    ['badoo.com/en/profile/{}', 'badoo'],
    ['mixcloud.com/{}', 'mixcloud'],
    ['telegram.me/{}', 'telegram'],
    ['t.me/{}', 'telegram'],
    ['medium.com/@{}', 'medium'],
    ['soundcloud.com/{}', 'soundcloud'],
    ['imgur.com/user/{}', 'imgur'],
    ['flipboard.com/@{}', 'flipboard'],
    ['ok.ru/{}', 'ok'],
    ['reverbnation.com/{}', 'reverbnation'],
    ['wix.com/{}', 'wix'],
    ['about.me/{}', 'about.me'],
    ['angellist.com/{}', 'angellist'],
    ['disqus.com/by/{}', 'disqus'],
    ['ellp.co/@{}', 'ello'],
    ['keybase.io/{}', 'keybase'],
    ['kongregate.com/accounts/{}', 'kongregate'],
    ['livejournal.com/profile?userid={}', 'livejournal'],
    ['medium.com/@{}', 'medium'],
    ['meetup.com/members/{}', 'meetup'],
    ['pinterest.com/{}', 'pinterest'],
    ['plurk.com/{}', 'plurk'],
    ['rottentomatoes.com/user/id/{}', 'rottentomatoes'],
    ['slideshare.net/{}', 'slideshare'],
    ['tripadvisor.com/members/{}', 'tripadvisor'],
    ['vimeo.com/{}', 'vimeo'],
    ['yelp.com/user_details?userid={}', 'yelp'],
    ['zomato.com/{}', 'zomato']
]

class NameCheck:
    def __init__(self, services, language):
        self.services = services
        self.language = language

    def get_url(self, uri, username):
        return ('https://{}'.format(uri)).format(username)

    def request(self, url):
        res = get(url)
        text = res.text.lower()
        if self.language == 'tr':
            return res.status_code // 100 == 2 and text.find('bulunamadı') == -1 and text.find('hata') == -1 and text.find('no such user.') == -1
        else:
            return res.status_code // 100 == 2 and text.find('not found') == -1 and text.find('error') == -1 and text.find('bulunamadı') == -1 and text.find('no such user.') == -1

    def search(self, username):
        index = 0
        for uri, service in self.services:
            if self.request(self.get_url(uri, username)):
                if self.language == 'tr':
                    print('[+] Kullanıcı adı bulundu: {}'.format(service))
                    print('[+] Profil URL: {}'.format(self.get_url(uri, username)))
                else:
                    print('[+] Username found on: {}'.format(service))
                    print('[+] Profile URL: {}'.format(self.get_url(uri, username)))
                print('-' * 75)
                index += 1
        if index:
            if self.language == 'tr':
                print('[+] Tüm profiller bulundu [+]')
            else:
                print('[+] All profiles are found [+]')
        else:
            if self.language == 'tr':
                print('[+] Bu kullanıcı adında kullanıcı bulunamadı [+]')
            else:
                print('[+] No such users with this username [+]')

def main():
    parser = argparse.ArgumentParser(prog="userscan", description='userscan')
    parser.add_argument('username', type=str, help='The username to search for / Aranacak kullanıcı adı')
    parser.add_argument('--lang', type=str, choices=['en', 'tr'], default='en', help='Language (en or tr) / Dil (en veya tr)')
    args = parser.parse_args()

    if args.lang == 'tr':
        print('[+] Kullanıcı Adı ile Profil Bul [+]')
    else:
        print('[+] Find Profile by Username [+]')
    
    name_check = NameCheck(services, args.lang)
    name_check.search(args.username)

if __name__ == '__main__':
    main()