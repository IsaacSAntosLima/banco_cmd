from flask import Flask

from routes.livros import livros_bp

app = Flask(__name__)

app.register_blueprint(livros_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)



