from vendfinder.scripts.vendfinder import VendFinder
import vendfinder

class VendFinderViewModel(object):

    def __init__(self):
        self.vend_finder = VendFinder()

    def get_vendors(self, user):
        config = self.vend_finder.get_user_config(user)
        return self.vend_finder.find(config)

    def get_config(self, user):
        config = self.vend_finder.get_user_config(user)
        with open(config, 'r') as f:
            data = f.read()
        return data

    def save_config(self, user, data):
        config = self.vend_finder.get_user_config(user)
        with open(config, 'w') as f:
            f.write(data)
