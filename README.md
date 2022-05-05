# file-browser

Surf through your filesystem via Flask web application.

For VM security issues is your concern.
Don't forget to change rules of your firewall to open ports. 😏

![Web Interface example](file_browser/static/screenshot.png)

## Prepare and activate environment (Unix)

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Development run

```bash
export FLASK_APP=file_browser
export FLASK_ENV=development
flask run
```
