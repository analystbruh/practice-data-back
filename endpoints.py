from app import app
import funcs
import psycopg2 as pg
from flask import make_response, request
from io import StringIO
import csv

dbname='practice-data'
user = 'postgres'
password = 'postgres'
allowed_host = 'http://localhost:4200' #switch prod/dev with environment variables

@app.route('/')
def home():
    return '<h1>HEY click <a href="/api/v1/customers">here</a>!</h1>'

@app.route('/api/v1/transactions/json')
def transactions_json():
    # create response object
    output = make_response(funcs.getTransactions('json'))
    output.headers['Content-Disposition'] = 'attachment; filename=transactions.json'
    output.headers['Content-type'] = 'text/json'
    # add CORS header
    output.headers.add("Access-Control-Allow-Origin", "*")
    return output

@app.route('/api/v1/transactions/csv')
def transactions_csv():
    # allot place in memory for csv file and create file
    si = StringIO()
    csv_writer = csv.writer(si)
    csv_writer.writerows(funcs.getTransactions('csv'))
    # create respons with data for download
    output = make_response(si.getvalue())
    output.headers['Content-Disposition'] = 'attachment; filename=transactions.csv'
    output.headers['Content-type'] = 'text/csv'
    # add CORS header
    output.headers.add("Access-Control-Allow-Origin", "*")
    return output

@app.route('/api/v1/transactions/sql')
def transactions_sql():
    system = request.args.to_dict()
    #create respons with file for download
    output = make_response(funcs.getTransactionsSQL(system['system']))
    output.headers['Content-Disposition'] = f'attachment; filename=table_{system["system"]}.sql'
    output.headers['Content-type'] = 'text/plain'
    #add CORS header
    output.headers.add("Access-Control-Allow-Origin", "*")
    return output

@app.route('/api/v1/transactions/schema')
def transactions_schema():
    system = request.args.to_dict()
    print(system)
    #create respons with file for download
    output = make_response(funcs.getTransactionsSchema(system['system']))
    output.headers['Content-Disposition'] = f'attachment; filename=schema_{system["system"]}.sql'
    output.headers['Content-type'] = 'text/plain'
    #add CORS header
    output.headers.add("Access-Control-Allow-Origin", "*")
    return output
