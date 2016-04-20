import os, os.path
import urllib.request
import threading
from multiprocessing.dummy import Pool as ThreadPool
from time import sleep

import vendfinder
from vendfinder.scripts.configparser import ConfigParser
from vendfinder.scripts.linkfactory import LinkFactory
from vendfinder.scripts.vendcrawler import VendCrawler

class VendFinder(object):

    def __init__(self):
        self.items = {}
        self.iter = 0

    def start_async(self):
        t = threading.Thread(target=self.start)
        t.daemon = True
        t.start()

    def start(self):
        while (True):
            vf_dir = os.path.join(os.path.expanduser('~'), '.vendfinder')
            config_files = [os.path.join(vf_dir, f)
                            for f in os.listdir(vf_dir) if
                            os.path.isfile(os.path.join(vf_dir, f))]

            pool = ThreadPool(4)
            results = pool.map(self.find, config_files)

            pool.close()
            pool.join()

            self.iter += 1
            sleep(1)

    def find(self, input):
        config_parser = ConfigParser(input)
        item_tuples = config_parser.read()
        link_factory = LinkFactory()
        links = []
        for item_tuple in item_tuples:
            link_factory.keys['item_id'] = item_tuple[0]
            link_factory.keys['price'] = item_tuple[1]
            link_factory.keys['price_op'] = 'lt'
            links.append((item_tuple, link_factory.create()))

        for link_tuple in links:
            key = link_tuple[0][0] + ':' + link_tuple[0][1]
            # skip if this link has already been processed by another worker
            if key in self.items and self.items[key][0] == self.iter:
                continue

            link = link_tuple[1]
            vend_crawler = VendCrawler()
            req = urllib.request.Request(link, headers={'User-Agent': 
                                                        'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                vend_crawler.feed(response.read().decode('utf-8'))

            self.items[key] = (self.iter, vend_crawler.items)

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
