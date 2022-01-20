from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/socialmedia'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class User(db.Model):
  
    tablename = 'user'
    user_ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    birthday = db.Column(db.DateTime, nullable=False)
    email = db.Column(db.String(64), nullable=False)
    phone = db.Column(db.String(64), nullable=False)
    city = db.Column(db.String(64), nullable=False)
    country = db.Column(db.String(64), nullable=False)

    def init(self, user_ID, name, age, birthday, email, phone, city, country): #Initialise the objects
        self.user_ID = user_ID
        self.name = name
        self.age = age
        self.birthday = birthday
        self.email = email
        self.phone = phone
        self.city = city
        self.country = country
        

    def json(self):
        return {"user_ID": self.user_ID, "name": self.name,  "age": self.age, "birthday": self.birthday, 
            "email": self.email, "phone": self.phone, "city": self.city, "country": self.city}


@app.route('/', methods=['GET'])
def get_all_users():
    return jsonify({"users": [user.json() for user in User.query.all()]})
    
if __name__ == "__main__":
    app.run(host = '0.0.0.0',port=5010, debug=True)