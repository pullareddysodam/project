from crypt import methods
from email import message
from pprint import pprint
from flask import Flask, redirect, render_template, request
from database import registerUserQuery,loginQuery,movies,theaters,getComments
import sqlite3
import json

app= Flask(__name__)

global sqliteCon;


@app.route('/')
def homePage():
    return render_template("login.html");


@app.route('/register',methods=['POST'])
def register():
    name = request.form.get("nme");
    userName = request.form.get("username");
    password = request.form.get("confirmpassword");
    result =registerUser(name,userName,password);
    return render_template("login.html",message="Successfully Registered");

@app.route('/login',methods=['POST'])
def login():
    username= request.form.get("username");
    password = request.form.get("password");
    sqliteCon = sqlite3.connect('user.db');
    cursor = sqliteCon.cursor();
    result = cursor.execute(loginQuery,(username,password));
    count=0;
    for r in result:
        count=r[0];
    if count==1:
        return render_template("dashbaord.html",movie = movies);
    else:
        print("login")
        return render_template("login.html",error="invalid");


@app.route('/theaters',methods=['GET'])
def fetchMovies():
    return render_template("theaters.html",movie=movies)

@app.route('/logout',methods=['GET'])
def logout():
    return redirect('/');

@app.route('/theaters',methods=['GET'])
def fetchTheaters():
    return render_template("theaters.html",theater=theaters)

@app.route('/comments',methods=['POST'])
def fetchComments():
    movieId= request.form.get('id');
    comment= getComments(movieId);
    return render_template();




def registerUser(name,username,password):
    sqliteCon = sqlite3.connect('user.db');
    cursor= sqliteCon.cursor();
    cursor.execute(registerUserQuery,(name,username,password));
    #connection.execute("INSERT INTO USER (name,username,password) values("+name+","+username+","+password")")
    sqliteCon.commit();
    sqliteCon.close();
    return "Successfully Registed!";

