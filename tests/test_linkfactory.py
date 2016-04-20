import unittest

from vendfinder.scripts.linkfactory import LinkFactory

class TestLinkFactoryMethods(unittest.TestCase):

    def test_create(self):
        link_factory = LinkFactory()
        link_factory.keys['item_id'] = 8700
        link = link_factory.create()
        self.assertEqual(link, 'https://sarahserver.net/?module=vendor&' \
                               'action=index&item_id=8700&name=&refine_op=eq&' \
                               'refine=&vendor=&shop=&price_op=eq&price=&map=')

if __name__ == '__main__':
    unittest.main()
