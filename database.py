from operator import gt
from pprint import pprint
import sqlite3
import pymongo
from bson.objectid import ObjectId


#sqlite
connection = sqlite3.connect('user.db')
createTable= "CREATE TABLE IF NOT EXISTS USER( ID INTEGER PRIMARY KEY AUTOINCREMENT,NAME TEXT NOT NULL, USERNAME TEXT NOT NULL, PASSWORD TEXT NOT NULL)";
registerUserQuery = "INSERT INTO USER (name,username,password) values(?,?,?)";
loginQuery= "SELECT COUNT(1) FROM USER WHERE USERNAME=? AND PASSWORD=?";

connection.execute(createTable); 

#mongodb
client = pymongo.MongoClient("mongodb+srv://sodam:Reddy123@cluster0.ub4og.mongodb.net/?retryWrites=true&w=majority");
mongoDB = client.sample_mflix;
moviescol= mongoDB.movies;
commentscol= mongoDB.comments;
theaterscol= mongoDB.theaters;
movies= list(moviescol.find({'year': {'$gt': '2000'}}));
theaters=list(theaterscol.find());

def getComments(movieId):
    comments=commentscol.find({'movie_id':ObjectId(movieId)})
    return list(comments);

