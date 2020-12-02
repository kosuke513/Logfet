class SystemConfig:
  DEBUG = True

  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:@{host}/{db_name}?charset=utf8'.format(**{
      'user': 'root',
      'host': '127.0.0.1',
      'db_name': 'logfet'
  })

Config = SystemConfig