import vendfinder

class ConfigParser(object):

    def __init__(self, config_file):
        with open(config_file, 'r') as f:
            self.data = f.read()
            self.lines = str(self.data).replace(' ', '').split()

    def read(self):
        item_tuples = []
        for line in self.lines:
            if (line.isspace() or line[0] == '#'):
                continue

            values = line.split(':')
            try:
                item_tuples.append((values[0], values[1], values[2]))
            except IndexError:
                item_tuples.append((values[0], values[1]))
        return item_tuples

    def read_raw(self):
        return self.data
