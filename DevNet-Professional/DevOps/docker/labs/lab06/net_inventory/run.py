from flask_migrate import Migrate
from sys import exit
from flask import redirect

from app import create_app, DB

app = create_app()
@app.route('/')
def base():
    return redirect("./views/inventory/devices", code=302)

Migrate(app, DB)
if __name__ == "__main__":
    app.run(host=app.config["HOST"], port=app.config["PORT"])
