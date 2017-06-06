#!/usr/bin/python
"""Hugo content analyser.

Usage:
  analyse flickr list
  analyse flickr shorten [--force]
  analyse images name [--dump]
  analyse (-h | --help)
  analyse --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --force       Force

"""
from docopt import docopt
import fnmatch
import os
import re
import shutil
import string
import urllib3
import yaml


ContentDir = "content"


HTTP = urllib3.PoolManager()
FlickrLongPattern = re.compile("https://www.flickr.com/[a-zA-Z0-9/_%@.-]*")
FlickrShortPattern = re.compile("flic.kr/p/[a-zA-Z0-9]*")


def list_items(directory, pattern="*.md"):
    for root, dirs, files in os.walk(directory):
        for f in files:
            if fnmatch.fnmatch(f, pattern):
                yield (f, os.path.join(root, f))


def nameof(filename):
    return os.path.splitext(filename)[0]


def extensionof(filename):
    return os.path.splitext(filename)[1]


def ensure_directory(path):
    try:
        os.makedirs(path)
    except OSError:
        pass


def read_file(path):
    with open(path, 'r') as f:
        return f.read()


def write_file(path, content):
    with open(path, 'w') as f:
        f.write(str(content))


def compute_flickr_short_url(identifier):
    table = '123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'
    encoding=''
    while identifier >= len(table):
        div,mod = divmod(identifier, len(table))
        encoding = table[mod] + encoding
        identifier = int(div)
    encoding = table[identifier] + encoding
    return "flic.kr/p/%s" % encoding


def check_flickr_short_url(url, expected_pseudo, expected_image_identifier):
    try:
        html = HTTP.request('GET', url + '/sizes/o/')
        url_sq = re.findall(r'href="/photos/([^"]*)', html.data.decode('utf-8'))[2]
        pseudo, image = url_sq.split('/')[0:2]
        return expected_pseudo == pseudo and expected_image_identifier == long(image)
    except :
        return False


def flickr_shorten(force):
    def pseudo_of(url):
        return url.split('/')[4]
    def image_identifier_of(url):
        return long(url.split('/')[5])

    for name, path in list_items(ContentDir):
        content = read_file(path)
        for url in FlickrLongPattern.findall(content):
            short = compute_flickr_short_url(image_identifier_of(url))
            if force or check_flickr_short_url(short, pseudo_of(url), image_identifier_of(url)):
                print "%-20s: %s" % (short, url)
                content = content.replace(url, short)
                write_file(path, content)
            else:
                print "Warning: check failed for %s (%s)" % (url, short)


def flickr_list():
    long_urls_count = 0
    short_urls_count = 0
    for name, path in list_items(ContentDir):
        content = read_file(path)
        long_urls = FlickrLongPattern.findall(content)
        short_urls = FlickrShortPattern.findall(content)
        if len(long_urls) > 0 or len(short_urls) > 0:
            print("\nFile %s:" % path)
            for url in long_urls:
                print("\t%s" % url)
            for url in short_urls:
                print("\t%s" % url)
        long_urls_count += len(long_urls)
        short_urls_count += len(short_urls)
    print("\nStatistics:")
    print("\tLong URL count: %d" % long_urls_count)
    print("\tShort URL count: %d" % short_urls_count)


def is_semantic_name(name):
    if sum(c.isdigit() for c in name) > 4:
        return (False, 'Too many digits')
    if sum(c.isupper() for c in name):
        return (False, 'Contains uppercase')
    return (True, 'OK')

ImageNamePattern = re.compile('name="([^"]*)"')
def images_name(dump):
    def images_names_from(content):
        names = ImageNamePattern.findall(content)
        front_matter = yaml.load_all(content).next()
        if 'illustration' in front_matter:
            names.append(front_matter['illustration']['name'])
        return names

    images = []
    for name, path in list_items(ContentDir):
        content = read_file(path)
        for name in images_names_from(content):
            status, reason = is_semantic_name(name)
            if not status:
                images.append({
                    "name": name,
                    "new_name": '',
                    "reason": reason,
                    "where": path
                })
                print "Bad  : %-30s (%s): %s" % (name, path, reason)
    if dump:
        with file('image-rename.yaml', 'w') as f:
            yaml.dump(images, f, default_flow_style=False)


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Hugo analyse 1.0')
    if arguments['flickr']:
        if arguments['list']:
            flickr_list()
        elif arguments['shorten']:
            flickr_shorten(force=arguments['--force'])
    elif arguments['images']:
        if arguments['name']:
            images_name(dump=arguments['--dump'])