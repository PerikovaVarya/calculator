from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        try:
            subprocess.call(['git', 'pull'], cwd='/home/calculator')
            return 'Success', 200
        except Exception as e:
            return str(e), 500
    return 'Invalid request', 400

if name == '__main__':
    app.run(host='0.0.0.0', port=6005)