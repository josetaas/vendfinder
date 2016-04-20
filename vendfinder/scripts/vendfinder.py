import os, os.path

import urllib.request

from vendfinder.scripts.configparser import ConfigParser
from vendfinder.scripts.linkfactory import LinkFactory
from vendfinder.scripts.vendcrawler import VendCrawler
import vendfinder

class VendFinder(object):

    def find(self, input):
        config_parser = ConfigParser(input)
        item_tuples = config_parser.read()
        link_factory = LinkFactory()
        links = []
        for item_tuple in item_tuples:
            link_factory.keys['item_id'] = item_tuple[0]
            link_factory.keys['price'] = item_tuple[1]
            link_factory.keys['price_op'] = 'lt'
            links.append(link_factory.create())

        items = []
        for link in links:
            vend_crawler = VendCrawler()
            req = urllib.request.Request(link, headers={'User-Agent': 
                                                        'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                vend_crawler.feed(response.read().decode('utf-8'))
                items = items + vend_crawler.items

        return items

    def get_user_config(self, user):
        if (' ' in user or ';' in user):
            return

        vf_dir = os.path.join(os.path.expanduser('~'), '.vendfinder')
        if (not os.path.isdir(vf_dir)):
            os.mkdir(vf_dir)

        user_file = os.path.join(vf_dir, user)
        if (not os.path.isfile(user_file)):
            with open(user_file, 'w+'):
                pass

        return user_file
