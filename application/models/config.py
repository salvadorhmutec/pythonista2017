import web

db_host = 'kavfu5f7pido12mr.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'qu5vnrzlly7v7d86'
db_user = 'sulo7biopvlrrmok'
db_pw = 'b7hbpc0lbzebzsvm'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )