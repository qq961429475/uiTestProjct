import configparser

config = configparser.ConfigParser()
config.read('../common/db.ini')
aa = config['TEST_DB']['host']
print(aa)
