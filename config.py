import web

db_host = 'localhost'
db_name = 'pythonistas2017'
db_user = 'zero'
db_pw = 'tulancingo2017'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )