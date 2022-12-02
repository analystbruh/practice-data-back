from venv import create
import psycopg2 as pg
from create_statements import create_statements
from schema_codes import ansi, mssqlserver, mysql_mariadb, oracle, postgres, sqlite

#db info
dbname='practice-data'
user = 'postgres'
password = 'postgres'

transactions_query = """
select
    t.id as transaction_id,
    c.first_name as customer_first_name,
    c.last_name as customer_last_name,
    c.city as customer_city,
    c.state as customer_state,
    c.country as customer_country,
	pc.product_category,
    p.brand,
    p.product_name,
    p.price,
    e.first_name as employee_first_name,
    e.last_name as employee_last_name,
    e.city as employee_city,
    e.state as employee_state,
    e.country as employee_country,
    e.hire_date,
    e.termination_date,
    e.job_title,
    t.timestamp,
    t.transaction_type
from transactions t
left join customers c on c.id = t.customer_id
left join products p on p.id = t.product_id
left join product_categories pc on pc.id = p.category_id
left join employees e on e.id = t.employee_id
order by t.id;
"""

def getData(query: str):
    # connect to db and get data
    conn = pg.connect(dbname=dbname, user=user, password=password) # use environment variable here
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    col_names = tuple(cols[0] for cols in cursor.description)
    cursor.close()
    conn.close()
    return (col_names, data)

def getInserts(table: str, cols: tuple, data: list[tuple]):
    fmt = "{}"
    insert_statement=f"insert into {table} values ({', '.join([fmt]*len(cols))});"
    insert_list = []
    quotes=("'","''")
    for row in data:
        lrow = list(row)
        for i, v in enumerate(row):
            if v == None:
                lrow[i] = 'Null'
            elif type(v) == str:
                lrow[i] = f"'{v.replace(quotes[0],quotes[1])}'"
            elif type(v) not in [int, float]:
                lrow[i] = f"'{v}'"
        insert_list.append(insert_statement.format(*lrow))
    insert_statements = '\n'.join(insert_list)
    return insert_statements

def getTransactions(type: str):
    transactions = {
        'csv': lambda cnms, dta: [cnms] + dta,
        'json': lambda cnms, dta: [dict(zip(cnms, row)) for row in dta]
    }
    col_names, data = getData(transactions_query)
    return transactions[type](col_names, data)

def getTransactionsSQL(system: str):
    # set up functions
    db_systems = ['ansi', 'sql server', 'mysql', 'mariadb','oracle','postgresql','sqlite']
    col_names, data = getData(transactions_query)
    insert_statements = getInserts('store_transactions', col_names, data)
    table_sql = dict(zip(db_systems, create_statements))[system] + insert_statements
    return table_sql.replace('        ','')

def getTransactionsSchema(system: str):
    db_systems = ['ansi', 'sql server', 'mysql', 'mariadb','oracle','postgresql','sqlite']
    create_statements = [
        ansi.create_statements,
        mssqlserver.create_statements,
        mysql_mariadb.create_statements,
        mysql_mariadb.create_statements,
        oracle.create_statements,
        postgres.create_statements,
        sqlite.create_statements
    ]
    system_create_statements = dict(zip(db_systems, create_statements))
    tables = ['customers', 'employees', 'product_categories', 'products', 'transactions']
    all_inserts = []
    for table in tables:
        col_names, data = getData(f'select * from {table};')
        insert_statements = getInserts(table, col_names, data)
        all_inserts.append(insert_statements)
    inserts = '\n\n'.join(all_inserts)
    return system_create_statements[system] + inserts

if __name__=='__main__':
    # getTransactionsSQL('ansi')
    print(getTransactionsSchema('postgresql'))