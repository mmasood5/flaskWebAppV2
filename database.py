from sqlalchemy import create_engine, text
import os

db_connection_stng = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_stng, 
                      connect_args = {
                        "ssl": {
                        "ssl_ca": "/etc/ssl/cert.pem"
                        }
                      })


def load_work_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from work"))
    work = []
    for row in result.all():
      work.append(dict(row._mapping))
    return work
