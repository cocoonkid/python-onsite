'''
a cool ting is that you can switch databases depending on one line of code (database URI)

you can run a query over multiple tables
'''
import sqlalchemy as sqa
from pprint import pprint
username = 'cocoonkid'

DATABASE_URI = f'postgres+psycopg2://{username}@localhost:5432/dvdrental'

engine = sqa.create_engine(DATABASE_URI)
connection = engine.connect()
metadata = sqa.MetaData()

actor = sqa.Table('actor’, metadata, autoload=True, autoload_with=engine)
#query = sqa.select([actor])
query = sqa.select([actor]).where(actor.columns.first_name == 'Penelope')
film = sqa.Table('film', metadata, autoload=True, autoload_with=engine)


result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
#result_set = result_proxy.fetchmany(10)

print(actor.columns.keys())
pprint(result_set)%