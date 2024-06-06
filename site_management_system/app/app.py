from flask import Flask, render_template

app = Flask(__name__)
app.static_folder = 'static'  # This line sets the static folder to 'static'

@app.route('/')
def index():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(host= '0.0.0.0')
