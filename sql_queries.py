create_table = \
'CREATE TABLE IF NOT EXISTS endpoints (' \
'id INTEGER PRIMARY KEY,' \
'verb TEXT,' \
'service TEXT,' \
'endpoint TEXT,' \
'tag TEXT UNIQUE,' \
'schema TEXT,' \
'payload TEXT)'

select_all = 'SELECT * FROM endpoints'

select_one = 'SELECT * FROM endpoints WHERE id=?'

select_query = 'SELECT * FROM endpoints WHERE endpoint=?, tag=?, schema=?'

insert = 'INSERT INTO endpoints VALUES (?,?,?,?,?,?)'

update = \
'UPDATE endpoints SET ' \
'verb=?, service=?, endpoint=?, tag=?, schema=?, payload=? ' \
'WHERE id=?' 

delete_all = 'DELETE FROM endpoints'

delete_one = 'DELETE FROM endpoints WHERE id=?'
