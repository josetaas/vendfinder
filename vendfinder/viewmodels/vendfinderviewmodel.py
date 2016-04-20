from hashlib import sha1
from json import dumps

from vendfinder.scripts.configparser import ConfigParser
from vendfinder.scripts.vendfinder import VendFinder
import vendfinder

class VendFinderViewModel(object):

    def __init__(self):
        self.vend_finder = VendFinder()
        self.vend_finder.start_async()

    def get_vendors(self, user):
        user_config = self.vend_finder.get_user_config(user)
        config_parser = ConfigParser(user_config)
        item_tuples = config_parser.read()

        items = []
        for item_tuple in item_tuples:
            try:
                key = item_tuple[0] + ':' + item_tuple[1]
                items += self.vend_finder.items[key][1]
            except KeyError as e:
                continue

        return dumps(items)

    def get_config(self, user):
        config = self.vend_finder.get_user_config(user)
        with open(config, 'r') as f:
            data = f.read()
        return dumps(data)

    def save_config(self, user, data):
        config = self.vend_finder.get_user_config(user)
        with open(config, 'w') as f:
            f.write(data)
