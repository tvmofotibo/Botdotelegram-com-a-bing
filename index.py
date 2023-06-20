from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def start():
    os.system("python  server.py > output.txt")
    return 'BOT ONLINE'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
