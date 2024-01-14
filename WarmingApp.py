import os
import subprocess
import flask as Flask
import pandas as pd
import os
import subprocess


#_____Kloniranje repozitorija_____
def kloniraj_repozitorij():
    url = "https://github.com/fsuman20/prog-analiza-pod.git"
    trenutni_dir = os.path.dirname(os.path.abspath(__file__))
    odredište = os.path.join(trenutni_dir, "suman_repozitorij") # odredišna mapa

    if os.path.exists(odredište):
        # Ako repozitorij već postoji, samo ga osvježi
        subprocess.run(["git", "-C", odredište, "pull"])
    else:
        # Ako repozitorij ne postoji, kloniraj ga
        subprocess.run(["git", "clone", url, odredište])


#_____Uspostava veze s Flaskom_____ 
def uspostava_veze_s_flaskom():
    app = Flask(__name__)

    @app.route('/') #početna stranica
    def hello():
        return 'Pozdrav! Ovo je početna stranica mog PAP projekta. Prati upute iz Jupiter bilježnice. :)'

    @app.route('/default_csv')
    def default_csv():
        df = pd.read_csv1('data/annual-co2-emissions-per-country.csv') #prikaz podataka iz csv datoteke
        return df.to_html()

    if __name__ == '__main__': #pokretanje web aplikacije
        app.run(port=5001)
        print("Localhost: http://127.0.0.1:5000/")

# Switch case
section = input("Upiši broj naredbe (1: Kloniraj repozitorij, 2: Uspostava veze s Flaskom): ")
if section == "1":
    kloniraj_repozitorij()
elif section == "2":
    uspostava_veze_s_flaskom()
else:
    print("Invalid section.")
