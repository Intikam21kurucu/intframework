#!/usr/bin/env python3
import time
from flask import Flask, render_template
from flask import request
import json
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Flask is started using yarn start-api (name of script in package.json)

@app.route('/time', methods=['GET', 'POST'])
def get_current_time():
    if request.method == 'GET':
        return {'time': time.time()}
    elif request.method == 'POST':
        data = str(request.data)
        print(type(data))
        li = data.split(',')
        print(li[0])
        return {'time': li[1]}

def conversion(lst):
    n_li = []

    for url in lst:
        try:
            n_li.append(url['url'])
        except TypeError:
            pass

    return n_li

@app.route('/file', methods=['GET', 'POST'])
def post_file():
    print('FILE METHOD')
    data = request.headers.get('Content-Type')
    if request.method == 'POST':
        data = request.get_json('url')
        convert_li = conversion(data)
        crawl = Crawler()
        emails = crawl.search(convert_li)
        print('FINAL RETURNING EMAILS: ', emails)
    return emails

@app.route('/testpl', methods=['GET', 'POST'])
def flaks():
    return render_template('index.html')

class Crawler:

    def extractEmail(self, req, emails):
        EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
        for re_match in re.finditer(EMAIL_REGEX, req):
            if re_match.group() not in emails:
                emails.append(re_match.group())

        return emails

    def extractAnchors(self, req):

        soup = BeautifulSoup(req, 'html.parser')
        anchors = soup.findAll('a')
        return anchors

    def createHref(self, input_url, href):

        href = urljoin(input_url, href)
        href_parsed = urlparse(href)
        href = href_parsed.scheme
        href += "://"
        href += href_parsed.netloc
        href += href_parsed.path
        final_parsed_href = urlparse(href)
        is_valid = bool(final_parsed_href.scheme) and bool(
            final_parsed_href.netloc)
        if is_valid:
            return href

    #Function to create HrefURLs from the anchors.
    #Returns a list of internal urls of the site
    def createHrefURLS(self, input_url, anchors, links_intern):

        for anchor in anchors:
            href = anchor.attrs.get("href")
            if href != "" or href != None:

                try:
                    if re.search('contact', href):
                        href = self.createHref(input_url, href)

                        input_url_netloc = urlparse(input_url).netloc
                        href_netloc = urlparse(href).netloc
                        if input_url_netloc == href_netloc:
                            links_intern.add(href)
                except TypeError:
                    pass
        return

    #Function that extracts: Email from url, anchors
    def level_crawler(self, input_url, emails):

        links_intern = set()

        try:
            source = requests.get(input_url).text

            self.extractEmail(source, emails) #Email Extraction

            anchors = self.extractAnchors(source) #Anchro Extraction

            self.createHrefURLS(input_url, anchors, links_intern)

            for link in links_intern:
                source = requests.get(link).text
                self.extractEmail(source, emails)
            return emails

        except Exception as e:
            return emails


    #The search function implements the level crawler and should use a list of URLs that are parsed
    #to the self.level_crawler(url, emails) file.

    def search(self, urls):

        emails = []
        count = 0
        for address in urls:
            self.level_crawler(address, emails)
            count+=1

        return emails

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)