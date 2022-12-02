from endpoints import app
from flask import jsonify

@app.route('/api/v1/test')
def test():
    return jsonify(dict(test=True))
