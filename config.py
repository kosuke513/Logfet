# from sqlalchemy import create_engine, engine
class LocalConfig:
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:@{host}/{db_name}?charset=utf8'.format(**{
      'user': 'root',
      'host': '127.0.0.1',
      'db_name': 'logfet'
  })
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SECRET_KEY = b'\xb9\x8dH\x1d\t\x0b\x98\xb9\x93\xe4\x15\xcd\x01%\n\x10\xcbud\xb7\xc0\xbdo\xaa'

class ProductConfig:
  DEBUG = False

  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:@/{db_name}?unix_socket=/cloudsql/{connection_name}?charset=utf8'.format(**{
      'user': 'root',
      'db_name': 'logfet',
      'connection_name': 'logfet-298314:asia-northeast1:logfet'
  })
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SECRET_KEY = b'\xb9\x8dH\x1d\t\x0b\x98\xb9\x93\xe4\x15\xcd\x01%\n\x10\xcbud\xb7\xc0\xbdo\xaa'

Local = LocalConfig
Product = ProductConfig

print(__name__)