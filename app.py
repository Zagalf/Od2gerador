from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from monstro import generate_monster  # Importar a função corretamente

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    monstro = None
    if request.method == 'POST':
        monstro = generate_monster()
    return render_template('index.html', monstro=monstro)

if __name__ == '__main__':
    app.run(debug=True)
