from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def entry():
    return render_template("index.html")

@app.route("/about/about.html")
def about():
    # Getting information of contributors from GitHub
    r = requests.get("https://api.github.com/repos/cb38335/cb38335.github.io/contributors")
    
    # Store data as json file
    json = r.json()

    # Create dictionary for contributors' information
    contributors = {}

    # Variable for the total number of commits
    total = 0

    # Reading json file
    for x in json:
        # Gets each person's number of commits and store in the dictionary
        contributionNum = x["contributions"]
        contributors[x["login"]] = contributionNum

        # Calculates the total number of commits
        total = total + contributionNum

    return render_template("about/about.html", daniel=contributors["danielvuong7"], christian=contributors["caa2783"], grecia=contributors["greciareyna"], chaquette=contributors["cb38335"], rin=contributors["pomeryt"], total=total)

@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/globalComponent/topNavigator.html")
def topNavigator():
    return render_template("globalComponent/topNavigator.html")

@app.route("/mainPage/creator-main.html")
def creatorMain():
    return render_template("mainPage/creator-main.html")

@app.route("/mainPage/creator-main2.html")
def creatorMain2():
    return render_template("mainPage/creator-main2.html")

@app.route("/mainPage/cname-main.html")
def cNameMain():
    return render_template("mainPage/cname-main.html")

@app.route("/mainPage/cname-main2.html")
def cNameMain2():
    return render_template("mainPage/cname-main2.html")

@app.route("/mainPage/country-main.html")
def countryMain():
    return render_template("mainPage/country-main.html")

@app.route("/mainPage/country-main2.html")
def countryMain2():
    return render_template("mainPage/country-main2.html")

@app.route("/creator/creator1.html")
def creator1():
    return render_template("creator/creator1.html")

@app.route("/creator/creator2.html")
def creator2():
    return render_template("creator/creator2.html")

@app.route("/creator/creator3.html")
def creator3():
    return render_template("creator/creator3.html")

@app.route("/creator/creator4.html")
def creator4():
    return render_template("creator/creator4.html")

@app.route("/creator/creator5.html")
def creator5():
    return render_template("creator/creator5.html")

@app.route("/creator/creator6.html")
def creator6():
    return render_template("creator/creator6.html")

@app.route("/cartoon/Arthur.html")
def cartoon1():
    return render_template("/cartoon/Arthur.html")

@app.route("/cartoon/FullMetalAlchemist.html")
def cartoon2():
    return render_template("/cartoon/FullMetalAlchemist.html")

@app.route("/cartoon/Gumball.html")
def cartoon3():
    return render_template("/cartoon/Gumball.html")

@app.route("/cartoon/Masha.html")
def cartoon4():
    return render_template("/cartoon/Masha.html")

@app.route("/cartoon/Miraculous.html")
def cartoon5():
    return render_template("/cartoon/Miraculous.html")

@app.route("/cartoon/TheSimpsons.html")
def cartoon6():
    return render_template("/cartoon/TheSimpsons.html")

@app.route("/countryOfOrigin/canada.html")
def country1():
    return render_template("/countryOfOrigin/canada.html")

@app.route("/countryOfOrigin/france.html")
def country2():
    return render_template("/countryOfOrigin/france.html")

@app.route("/countryOfOrigin/japan.html")
def country3():
    return render_template("/countryOfOrigin/japan.html")

@app.route("/countryOfOrigin/russia.html")
def country4():
    return render_template("/countryOfOrigin/russia.html")

@app.route("/countryOfOrigin/uk.html")
def country5():
    return render_template("/countryOfOrigin/uk.html")

@app.route("/countryOfOrigin/usa.html")
def country6():
    return render_template("/countryOfOrigin/usa.html")

if __name__ == "__main__":
    # Actual Web Address
    app.run("107.170.56.162", "80")

    # For Test
    # app.run()
    
