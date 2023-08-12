import app
import sqlalchemy


if __name__ == "__main__":
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@192.168.133.233:5432/postgres'
    app.config['SQLALCHEMY_ECHO'] = True
    db = sqlalchemy(app)
    app.run(debug=True)
