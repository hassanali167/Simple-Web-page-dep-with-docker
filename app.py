from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory('static', filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
