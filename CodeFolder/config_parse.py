from ConfigParser import ConfigParser

def my_parse(file):
    parser = ConfigParser()
    parser.read(file)
    return parser.get('home','uri')
