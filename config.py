import web

db_host = 'dyud5fa2qycz1o3v.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'gwaq594jewqemud3'
db_user = 'z2k0axmt1cgw31up'
db_pw = 'ksxb0pv9407muyw8'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )
