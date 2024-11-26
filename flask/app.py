from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, YouTeam Flask is running!"

def health():
    return "App is healthy!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
