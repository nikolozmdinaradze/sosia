from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#შეიქმნა ქოკტეილების კლასი, რომლის ობიექტებიც დაემატება მონაცემთა ბაზაში.
class Cocktails(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(60), nullable = False)
    image = db.Column(db.String(1000), nullable = False)
    
    def __init__(self, id, name,image):
        self.id = id
        self.name = name
        self.image = image


@app.route('/')
def results():
    search = request.args.get('search')
    if search:
        results = Cocktails.query.filter(Cocktails.name.ilike(f'%{search}%')).all()
    else:
        results = Cocktails.query.limit(10).all()
        
    return render_template('template.html', cocktails = results)
    


if __name__ == '__main__':
    app.run(debug=True)