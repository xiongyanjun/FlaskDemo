from flask import Flask

from model.model import User

app = Flask(__name__)


@app.route("/")
def append_comment():
    user = User.query.filter_by(id=1)
    user.update({"comment": "comment_"})
    return User.query.filter_by(id=1)


@app.route("/users")
def users():
    return User.query.all()


if __name__ == "__main__":
    app.run(debug=True)
