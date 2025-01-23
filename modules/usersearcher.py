#!/usr/bin/env python3
import requests
import time
import argparse

def outer_func(colour):
    def inner_function(msg):
        print(f'{colour}{msg}')
    return inner_function

''' COLOUR PRINTS '''
GREEN = outer_func('\033[92m')
YELLOW = outer_func('\033[93m')
RED = outer_func('\033[91m')

''' BANNER '''
def bannerslk():
    YELLOW(r'''    
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣄⡀⠀⠀⠀⠀⢠⣤⣄⠀⣀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣴⠟⠛⠉⠁⠀⠀⠈⠉⠛⠻⣦⣄⠀⢸⡟⠙⣿⡟⣷⡀
⠀⠀⠀⠀⠀⢠⣾⠏⠁⣀⠀⠀⠀⠀⢀⣀⡈⠻⣷⣼⣧⠀⢹⡇⣹⡇
⠀⠀⠀⠀⣰⡿⠟⠛⢛⣛⣛⡿⢶⣶⣶⡶⢿⣛⣛⡛⠛⠿⢿⣿⣷⣿⣣⡿⠁
⠀⠀⠀⠀⣿⠁⢀⣼⠟⣯⣝⣻⣦⣤⣤⣾⣟⣫⣭⠻⣷⡄⠈⣿⣨⣿⠋⠀⠀
⠀⠀⣠⡾⠻⢷⣬⣛⣿⡿⠟⠋⠁⠀⠀⠈⠉⠛⢿⣿⣋⣵⡾⠛⢿⣅⠀⠀⠀
⠀⣼⠟⠀⠀⠀⠉⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⠁⠀⠀⠀⠻⣧⠀⠀
⠰⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠆⠀
⠀⢻⣦⠀⠀⠀⠀⠀⢴⣤⣤⣀⣀⠀⠀⣀⣠⣤⡾⢿⡆⠀⠀⠀⠀⣴⡟⠀⠀
⠀⠀⠙⢷⣤⣀⠀⠀⠀⠈⠉⠙⠛⠛⠛⠛⠉⠁⠀⠈⠁⠀⣀⣤⡾⠋⠀⠀⠀
⠀⠀⠀⠀⠈⠛⠷⢶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⠟⠋⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠛⢷⣤⣀⡀⠀⠀⢀⣠⣴⡾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
  ''')

def searchus(username):
    WEBSITES = [
        f'https://www.instagram.com/{username}', f'https://www.facebook.com/{username}', f'https://www.twitter.com/{username}',
        f'https://www.youtube.com/{username}', f'https://{username}.blogspot.com', f'https://plus.google.com/s/{username}/top',
        f'https://www.reddit.com/user/{username}', f'https://{username}.wordpress.com', f'https://www.pinterest.com/{username}',
        f'https://www.github.com/{username}', f'https://{username}.tumblr.com', f'https://www.flickr.com/people/{username}',
        f'https://steamcommunity.com/id/{username}', f'https://vimeo.com/{username}', f'https://soundcloud.com/{username}',
        f'https://disqus.com/by/{username}', f'https://medium.com/@{username}', f'https://{username}.deviantart.com',
        f'https://vk.com/{username}', f'https://about.me/{username}', f'https://imgur.com/user/{username}',
        f'https://flipboard.com/@{username}', f'https://slideshare.net/{username}', f'https://fotolog.com/{username}',
        f'https://open.spotify.com/user/{username}', f'https://www.mixcloud.com/{username}', f'https://www.scribd.com/{username}',
        f'https://www.badoo.com/en/{username}', f'https://www.patreon.com/{username}', f'https://bitbucket.org/{username}',
        f'https://www.dailymotion.com/{username}', f'https://www.etsy.com/shop/{username}', f'https://cash.me/{username}',
        f'https://www.behance.net/{username}', f'https://www.goodreads.com/{username}', f'https://www.instructables.com/member/{username}',
        f'https://keybase.io/{username}', f'https://kongregate.com/accounts/{username}', f'https://{username}.livejournal.com',
        f'https://angel.co/{username}', f'https://last.fm/user/{username}', f'https://dribbble.com/{username}',
        f'https://www.codecademy.com/{username}', f'https://en.gravatar.com/{username}', f'https://pastebin.com/u/{username}',
        f'https://foursquare.com/{username}', f'https://www.roblox.com/user.aspx?username={username}', f'https://www.gumroad.com/{username}',
        f'https://{username}.newgrounds.com', f'https://www.wattpad.com/user/{username}', f'https://www.canva.com/{username}',
        f'https://creativemarket.com/{username}', f'https://www.trakt.tv/users/{username}', f'https://500px.com/{username}',
        f'https://buzzfeed.com/{username}', f'https://tripadvisor.com/members/{username}', f'https://{username}.hubpages.com',
        f'https://{username}.contently.com', f'https://houzz.com/user/{username}', f'https://blip.fm/{username}',
        f'https://www.wikipedia.org/wiki/User:{username}', f'https://news.ycombinator.com/user?id={username}', f'https://www.reverbnation.com/{username}',
        f'https://www.designspiration.net/{username}', f'https://www.bandcamp.com/{username}', f'https://www.colourlovers.com/love/{username}',
        f'https://www.ifttt.com/p/{username}', f'https://www.ebay.com/usr/{username}', f'https://{username}.slack.com',
        f'https://www.okcupid.com/profile/{username}', f'https://www.trip.skyscanner.com/user/{username}', f'https://ello.co/{username}',
        f'https://tracky.com/user/~{username}', f'https://{username}.basecamphq.com/login', f'https://www.linkedin.com/in/{username}'
    ]

    GREEN(f'[+] Searching for username: {username}')
    time.sleep(0.5)
    print('.......')
    time.sleep(0.5)
    print('.......\n')
    time.sleep(0.5)

    GREEN(f'[+] codassassin\'s UserSearch is working...\n')
    time.sleep(0.5)
    print('.......')
    time.sleep(0.5)
    print('.......\n')
    time.sleep(0.5)

    time.sleep(1)

    count = 0
    match = True
    for url in WEBSITES:
        r = requests.get(url)

        if r.status_code == 200:
            if match:
                GREEN('[+] FOUND MATCHES')
                match = False
            YELLOW(f'\n{url} - {r.status_code} - OK')
            if username in r.text:
                GREEN(f'POSITIVE MATCH: Username:{username} - text has been detected in url.')
            else:
                GREEN(f'POSITIVE MATCH: Username:{username} - \033[91mtext has NOT been detected in url, could be a FALSE POSITIVE.')
        count += 1

    total = len(WEBSITES)
    GREEN(f'FINISHED: A total of {count} MATCHES found out of {total} websites.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Search for a username across multiple websites")
    parser.add_argument('username', type=str, help='Username to search for')
    args = parser.parse_args()

    bannerslk()
    searchus(args.username)