from collections import OrderedDict

from html.parser import HTMLParser
import re

import vendfinder

class VendCrawler(HTMLParser):

    def __init__(self):
        super(VendCrawler, self).__init__()
        self.in_table = False
        self.row = 0
        self.col = 0
        self.get_data = False
        self.items = []
        self.reset_current()

    def handle_starttag(self, tag, attrs):
        if (not self.in_table and tag == 'table'):
            for attr in attrs:
                if (attr[0] == 'class' and attr[1] == 'horizontal-table'):
                    self.in_table = True
        elif (self.in_table):
            if (tag == 'tr'):
                self.row += 1
            elif (tag == 'td'):
                self.col += 1
                self.get_data = True

    def handle_endtag(self, tag):
        if (self.in_table):
            if (tag == 'table'):
                self.in_table = False
                self.get_data = False
            elif (tag == 'tr'):
                self.col = 0
                if (self.row > 1):
                    self.items.append(self.current)
                    self.reset_current()

    def handle_data(self, data):
        if (self.get_data):
            if (data.isspace()):
                return

            data = data.replace('\r', '').replace('\t', '').replace('\n', '')

            if (self.col == 2):
                self.current['item'] = data
            elif (self.col == 3):
                self.current['amount'] = data
            elif (self.col == 4):
                self.current['price'] = data
            elif (self.col == 6):
                self.current['shop'] = data
            elif (self.col == 7):
                self.current['map'] = data

    def reset_current(self):
        self.current = OrderedDict()
        self.current['item'] = ''
        self.current['amount'] = ''
        self.current['price'] = ''
        self.current['shop'] = ''
        self.current['map'] = ''
