from flasgger import Swagger
from flask import Flask, render_template

from router.auth import auth_router
from router.user import user_route

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")


app.register_blueprint(auth_router)
app.register_blueprint(user_route)
swagger = Swagger(app)
