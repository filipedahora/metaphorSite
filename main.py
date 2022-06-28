from flask import Flask, render_template

app = Flask(__name__)

#criar a primeira pagina do site

@app.route("/")

def index():
    first_name = "Filipe"
    stuff = "Isto é <strong>negrito</strong>"
    favorite_pizza = ["Peperoni", "Cheese", "Mushrooms", 41]
    return render_template("index.html",
                            first_name=first_name,
                            stuff=stuff,
                            favorite_pizza=favorite_pizza )

@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name)


#criando paginas de erro customizadas 
#URL invalida
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
#internal Server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


if __name__=='__main__':
    app.run(debug=True)