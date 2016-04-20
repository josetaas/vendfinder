
import unittest

from vendfinder.scripts.vendfinder import VendFinder

class TestVendFinderMethods(unittest.TestCase):
    
    def test_get_user_config(self):
        vend_finder = VendFinder()
        config = vend_finder.get_user_config('test_vendfinder')
        with open(config, 'w') as f:
            f.write('# test_vendfinder\n')

        config = vend_finder.get_user_config('test_vendfinder')
        with open(config, 'r') as f:
            self.assertTrue('# test_vendfinder' in str(f.read()))


if __name__ == '__main__':
    unittest.main()
