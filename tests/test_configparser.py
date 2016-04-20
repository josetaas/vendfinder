import os
import unittest

from vendfinder.scripts.configparser import ConfigParser

class TestConfigParserMethods(unittest.TestCase):

    def test_parse(self):
        f = open('test_config.txt', 'w')
        f.write('# asdfas\n')
        f.write('\n')
        f.write('1234:5678\n')
        f.write('1432:3298\n')
        f.close()

        config_parser = ConfigParser('test_config.txt')
        item_tuples = config_parser.read()
        self.assertEqual(item_tuples[0][0], '1234')
        self.assertEqual(item_tuples[0][1], '5678')
        self.assertEqual(item_tuples[1][0], '1432')
        self.assertEqual(item_tuples[1][1], '3298')

if __name__ == '__main__':
    unittest.main()
