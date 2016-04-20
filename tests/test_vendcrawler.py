import unittest

from vendfinder.scripts.vendcrawler import VendCrawler

class TestVendCrawlerMethods(unittest.TestCase):
    
    def test_extract(self):
        vend_crawler = VendCrawler()
        with open('test_vendcrawler.html', 'r') as f:
            vend_crawler.feed(f.read())
        vendor_infos = vend_crawler.items
        self.assertEqual(vendor_infos[0]['item'], 'Elven Ears')
        self.assertEqual(vendor_infos[0]['price'], '8,899,999')


if __name__ == '__main__':
    unittest.main()
