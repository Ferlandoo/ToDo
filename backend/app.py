from flask import Flask, request, jsonify, make_response, render_template, session
import jwt
from datetime import datetime, timedelta
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY']  = '479cdcf08d2b4a16b9c3ea2eba2853a7'

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'Alert': 'Token is missing!'}), 401
        try:
            payload = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'Alert': 'Token is invalid!'}), 403
        return func(*args, **kwargs)
    return decorated

@app.route ('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return 'Logged in currently'

@app.route ('/public')
def public():
    return 'For Public'

@app.route ('/auth')
@token_required
def auth():
    return 'Token is valid!'

@app.route('/login', methods=['POST'])
def login():
    if request.form['username'] and request.form['password'] == 123456:
        session['logged_in'] = True
        token = jwt.encode({
            'user':request.form['username'],
            'expiration': str(datetime.utcnow() + timedelta(seconds=120))
        },
            app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8')})
    else:
        return make_response('Could not verify', 403, {'WWW-Authenticate': 'Basic realm="Authentication Failed!"'})

@app.route('/logout', methods=['POST'])
def logout():
    pass

if __name__ == '__main__':
    app.run(debug=True, port=5018)