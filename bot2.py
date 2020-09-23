config.cfg
[bot]
token = '1385808594:AAF0pVNLQiJvfC69DCdXlGTgO0pRarSLIpQ'
import configparser

conf = configparser.RawConfigParser()
conf.read(config.cfg)
token = conf.get('bot','token')
print(token)