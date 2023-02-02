import logging.config
import yaml
import logging


logger = logging.getLogger('__main__')
# linux /home/autoposting_bot/log/config.yml
# win
with open(r'./log/config.yml', 'r') as obj:
    logging.config.dictConfig(yaml.safe_load(obj))
