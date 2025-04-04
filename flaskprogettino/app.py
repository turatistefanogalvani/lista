from flask import Flask, render_template

app = Flask(__name__)
lista = ["ciao1","ciao2","ciao3","ciao4","ciao5"]
@app.route('/')
def home():
    return render_template("index.html", x = lista)

if __name__ == '__main__':
    app.run(debug=True)