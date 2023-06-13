from flask import Flask

from app.main.views import main_blueprint
from app.api.views import api_blueprint


app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(api_blueprint)


@app.errorhandler(404)
def page_not_found(error):
    return "<h1>Вибачте, але токої сторінки не знайдено</h1>"


@app.errorhandler(500)
def internal_server_error(error):
    return "<h1>Вибачте, помилка на сервері</h1>"


if __name__ == "__main__":
    app.run(debug=True)