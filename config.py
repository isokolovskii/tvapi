config = {
    'dms': 'mysql',
    'driver': 'pymysql',
    'user': 'tvapi',
    'password': 'ndfgb2017',
    'server': 'localhost',
    'database': 'tvservice',
    'charset': 'utf8',
    'host': 'tv.isokol-dev.ru',
    'port': 8085
}

DB_URI = '{dms}+{driver}://{user}:{password}@{server}/{database}?charset={charset}'.format(**config)
