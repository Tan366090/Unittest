from flask import Flask, request, render_template, redirect, url_for, make_response
import configparser

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hihi'

config = configparser.ConfigParser()
config.read('config.ini')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email'] + "@blu.edu.vn"
        password = request.form['password']
        ma_so = request.form['ma_so']

        user_found = False
        for user in config.sections():
            if config[user]['email'] == email and config[user]['password'] == password and config[user]['ma_so'] == ma_so:
                user_found = True
                resp = make_response(redirect(url_for('upload')))
                resp.set_cookie('user_email', email, max_age=180)
                return resp

        if not user_found:  # Nếu không tìm thấy user
            return 'Invalid credentials!', 404  # Trả về mã 404

    return render_template('login.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        uploaded_files = request.files.getlist('myfile')
        file_paths = []
        for file in uploaded_files:
            if file:
                file_path = f"uploads/{file.filename}"
                file.save(file_path)
                file_paths.append(file_path)
        return render_template('upload.html', file_paths=file_paths)
    return render_template('upload.html')

@app.errorhandler(404)
def page_not_found(e):
    return 'Invalid credentials!', 404

if __name__ == '__main__':
    app.run(debug=True)
