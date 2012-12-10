import ConfigParser, os

def get_config():
    try:
        config_reader = ConfigParser.ConfigParser()
        config_reader.read(os.path.abspath(os.path.join(os.path.dirname(__file__), 'config.ini')))
        return config_reader
    except:
        raise Exception('Please check the config.ini exists, or its content is correct or not.')