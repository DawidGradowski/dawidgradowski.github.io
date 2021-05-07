from flask import Flask, redirect, url_for, render_template, request
import random

app = Flask(__name__)

def generator(*coZawiera, dlugosc=12):
    litery_male = "qwertyuiopasdfghjklzxcvbnm"
    litery_duze = litery_male.upper()
    liczby = "1234567890"
    znaki_specjalne = "!@$%&?"
    znaki = []
    haslo = ""
    for i in coZawiera:
        if i == "lm":
            for x in litery_male:
                znaki.append(x)

        if i == "ld":
            for x in litery_duze:
                znaki.append(x)

        if i == "liczby":
            for x in liczby:
                znaki.append(x)

        if i == "znaki":
            for x in znaki_specjalne:
                znaki.append(x)
    for i in range (0,dlugosc):
        haslo = haslo + znaki[random.randint(0,abs(len(znaki)-1))]

    return haslo


@app.route("/")
def home():
    return render_template('Strona_glowna.html/')

@app.route("/O_mnie.html/")
def omnie():
    return render_template('O_mnie.html/')

@app.route("/Kox_rzeczy.html/")
def kox():
    return render_template('Kox_rzeczy.html/')

@app.route("/Kontakt.html/")
def kontakt():
    return render_template('Kontakt.html/')

@app.route("/Program.html/", methods=['GET','POST'])
def program():
    if request.method == 'POST':
        a = []
        if request.form.get('lm'):
            a.append(request.form.get('lm'))

        if request.form.get('ld'):
            a.append(request.form.get('ld'))

        if request.form.get('liczby'):
            a.append(request.form.get('liczby'))

        if request.form.get('znaki'):
            a.append(request.form.get('znaki'))

        if len(a) > 0:
            wygenerowane_haslo = generator(*a)
        
        else:
            wygenerowane_haslo = "miejsce na hasło"

        return render_template('Program.html/', password = wygenerowane_haslo)
    else:
        return render_template('Program.html/', password = "miejsce na hasło")
    

if __name__ == "__main__":
    app.run(debug=True)
    print(program.a)