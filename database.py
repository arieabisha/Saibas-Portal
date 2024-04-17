from sqlalchemy import create_engine

db_connection_string = "mysql+pymysql://root:Mrtosso123@saibascareer.cfc6agsc2mbd.ap-southeast-2.rds.amazonaws.com/saibascareer?charset=utf8mb4"

engine = create_engine (
  db_connection_string,
  connect_args={
    "ssl": {
    "ssl_ca": "/etc/ssl/cert.pem"
    }
  })


