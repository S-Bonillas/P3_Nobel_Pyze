#------------------------------------------------------------------------
#                       Import dependancies
#------------------------------------------------------------------------ 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify
from datetime import datetime


#------------------------------------------------------------------------
#               Configure the database connection URI
#------------------------------------------------------------------------
app = Flask(__name__)

#------------------------------------------------------------------------
# FORMAT YOUR DATABASE PATH LIKE THIS:  'postgresql://{username}:{password}@{host}:{port}/{database_name}'
#------------------------------------------------------------------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:{PASSWORDHERE}@localhost:5432/Laureates_DB'                              
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#------------------------------------------------------------------------
#          Create a SQLAlchemy database connection object
#------------------------------------------------------------------------
db = SQLAlchemy(app)


#========================================================================
#               Reflect tables to Python classes:
#========================================================================

#------------------------------------------------------------------------
#                           Laureates Table
#------------------------------------------------------------------------
class Laureates(db.Model):
    __tablename__ = 'Laureates'
    Laureate_id = db.Column(db.Integer, primary_key=True)
    Org_id = db.Column(db.String(20))
    Laureate_Full_Name = db.Column(db.String(100))
    Laureate_Known_Name = db.Column(db.String(100))
    Birth_Date = db.Column(db.Date, default=datetime.utcnow)
    Birth_City = db.Column(db.String(100))
    Birth_Country = db.Column(db.String(100))
    Birth_Lat = db.Column(db.Float)
    Birth_Lon = db.Column(db.Float)
    Gender = db.Column(db.String(10))
    Age_When_Awarded = db.Column(db.Float)

#------------------------------------------------------------------------
#                           Awards Table
#------------------------------------------------------------------------
class Awards(db.Model):
    __tablename__ = 'Awards'
    Laureate_id = db.Column(db.Integer, primary_key=True)
    Category = db.Column(db.String(30))
    Affiliation_Name = db.Column(db.String)
    Award_year = db.Column(db.Integer)
    Motivation = db.Column(db.String)
    Date_Awarded = db.Column(db.Date, default=datetime.utcnow)
    Award_City = db.Column(db.String(100))
    Award_Country = db.Column(db.String(100))
    Award_Lat = db.Column(db.Float)
    Award_Lon = db.Column(db.Float)

#------------------------------------------------------------------------
#                           Prizes Table
#------------------------------------------------------------------------
class Prizes(db.Model):
    __tablename__ = 'Prizes'
    Laureate_id = db.Column(db.Integer, primary_key=True)
    Prize_Amount = db.Column(db.Integer)
    Prize_Amount_Adj = db.Column(db.Integer)
    Sole_Winner = db.Column(db.Boolean)  # Change to Boolean
    Portion = db.Column(db.String)  # Consider using an appropriate numeric type


#------------------------------------------------------------------------
#                           Orgs Table
#------------------------------------------------------------------------
class Orgs(db.Model):
    __tablename__ = 'Orgs'
    Laureate_id = db.Column(db.Integer, primary_key=True)
    Org_id = db.Column(db.String(20))
    Organization_Name = db.Column(db.String)
    Founded_country = db.Column(db.String(20))
    Org_Founded_Date = db.Column(db.Date, default=datetime.utcnow)

#========================================================================



    
#========================================================================
# Define App Routes
#========================================================================
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Welcome to my 'home' page!"

#------------------------------------------------------------------------
#                       Laureates App route
#------------------------------------------------------------------------
@app.route("/Laureates")
def get_Laureates():
    laureates = Laureates.query.all()
    laureates_list = [{'Laureate_id': laureate.Laureate_id,
                       'Org_id': laureate.Org_id,
                       'Laureate_Full_Name': laureate.Laureate_Full_Name,
                       'Laureate_Known_Name': laureate.Laureate_Known_Name,
                       'Birth_Date': laureate.Birth_Date,
                       'Birth_City': laureate.Birth_City,
                       'Birth_Country': laureate.Birth_Country,
                       'Birth_Lat': laureate.Birth_Lat,
                       'Birth_Lon': laureate.Birth_Lon,
                       'Gender': laureate.Gender,
                       'Age_When_Awarded': laureate.Age_When_Awarded,
                       } for laureate in laureates]

    return jsonify({'Laureates': laureates_list})



#------------------------------------------------------------------------
#                       Awards App route
#------------------------------------------------------------------------
@app.route("/Awards")
def get_awards():
    awards_data = Awards.query.all()
    awards_list = [{'Laureate_id': award.Laureate_id,
                    'Category': award.Category,
                    'Affiliation_Name': award.Affiliation_Name,
                    'Award_year': award.Award_year,
                    'Motivation': award.Motivation,
                    'Date_Awarded': award.Date_Awarded,
                    'Award_City': award.Award_City,
                    'Award_Country': award.Award_Country,
                    'Award_Lat': award.Award_Lat,
                    'Award_Lon': award.Award_Lon,
                    } for award in awards_data]

    return jsonify({'Awards': awards_list})



#------------------------------------------------------------------------
#                       Prizes App route
#------------------------------------------------------------------------
@app.route("/Prizes")
def get_prizes():
    prizes_data = Prizes.query.all()
    prizes_list = [{'Laureate_id': prize.Laureate_id,
                    'Prize_Amount': prize.Prize_Amount,
                    'Prize_Amount_Adj': prize.Prize_Amount_Adj,
                    'Sole_Winner': prize.Sole_Winner,
                    'Portion': prize.Portion,
                    } for prize in prizes_data]

    return jsonify({'Prizes': prizes_list})



#------------------------------------------------------------------------
#                       Orgs App route
#------------------------------------------------------------------------
@app.route("/Orgs")
def get_orgs():
    orgs_data = Orgs.query.all()
    orgs_list = [{'Laureate_id': org.Laureate_id,
                  'Org_id': org.Org_id,
                  'Organization_Name': org.Organization_Name,
                  'Founded_country': org.Founded_country,
                  'Org_Founded_Date': org.Org_Founded_Date,
                  } for org in orgs_data]

    return jsonify({'Orgs': orgs_list})
#------------------------------------------------------------------------
#========================================================================





#------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
#------------------------------------------------------------------------