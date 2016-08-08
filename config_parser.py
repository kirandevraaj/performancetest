import ConfigParser
Config = ConfigParser.ConfigParser()
Config.read("nccm_config.ini")
print Config.get('NCCM URL','token_url')