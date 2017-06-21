create_table = \
'CREATE TABLE IF NOT EXISTS endpoints (' \
'id INTEGER PRIMARY KEY,' \
'verb TEXT,' \
'service TEXT,' \
'url TEXT,' \
'tag TEXT UNIQUE,' \
'schema TEXT,' \
'payload TEXT)'

select_all = 'SELECT * FROM endpoints'
select_one = 'SELECT * FROM endpoints WHERE id=?'
select_query = 'SELECT schema, payload FROM endpoints WHERE url=? AND tag=?'

insert = \
'INSERT INTO endpoints (verb,service,url,tag,schema,payload) ' \
'VALUES (?,?,?,?,?,?)'
update = \
'UPDATE endpoints SET ' \
'verb=?,service=?,url=?,tag=?,schema=?,payload=? ' \
'WHERE id=?' 

delete_all = 'DELETE FROM endpoints'
delete_one = 'DELETE FROM endpoints WHERE id=?'
