from flask import Flask

from registration.registration import registration

app = Flask(__name__)
app.register_blueprint(registration)



if __name__ == '__main__':
    app.run()
