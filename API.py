import requests
from app import Cocktails, db,app
import json

#მივიღეთ მონაცემები JSON_ის სახით გადავიყვანეთ ლექსიკონში, შემდეგ ვაქციეთ ობიექტებად და შევიტანეთ მონაცემები ბაზაში.
with app.app_context():

    url = "https://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Cocktail"
    r = requests.get(url)

    if r.status_code == 200:
        print("SUCCESS!!!\n")
        dic = r.json()
        drinks = dic['drinks']
        n=0
        for drink in drinks:
            cocktail = Cocktails(drink['idDrink'],drink['strDrink'], drink['strDrinkThumb'])
            db.session.add(cocktail)
            db.session.commit()
            print(n+1)
    else:
        print("There Is a Problem.\n")


