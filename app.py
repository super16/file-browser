from pathlib import Path
from flask import Flask, render_template

app = Flask(__name__)

# Views

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/<path:subpath>')
def browse(subpath):
    p = Path('/' + subpath)
    return render_template('browser.html', path=p, folder_directory=folders_list(p), files_directory=files_list(p))

# Errors

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
    
@app.errorhandler(PermissionError)
def internal_server_error(e):
    return render_template('permission_error.html')
    
# Functions

def folders_list(path):
    """Making a list of folders for template"""
    return [x for x in path.iterdir() if x.is_dir()]

def files_list(path):
    """Making a list of files for template"""
    return [x for x in path.iterdir() if x.is_file()]

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
