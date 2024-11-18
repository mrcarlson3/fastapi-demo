#!/usr/bin/env python3

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import json
import os
import mysql
import mysql.connector
from mysql.connector import Error
from fastapi.middleware.cors import CORSMiddleware

DBHOST = "ds2022.cqee4iwdcaph.us-east-1.rds.amazonaws.com"
DBUSER = "ds2022"
DBPASS = os.getenv('DBPASS')
DB = "mjy7nw"

db = mysql.connector.connect(user=DBUSER, host=DBHOST, password=DBPASS, database=DB)
cur=db.cursor()

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins= ['*'],
    allow_methods= ['*'],
    allow_headers= ['*'],
)
@app.get("/")  # zone apex
def zone_apex():
    return {"Greetings": "Breadloaf"}

@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"sum": a + b}

@app.get("/multiply/{c}/{d}")
def multiply(c: int, d: int):
    return {"product": c * d}

@app.get("/data")
async def get_data():
    example_data = {
        "id" : 1,
        "name" : "Pesto",
        "animal" : "Penguin"
    }
    return example_data

@app.get("/story")
async def get_story():
    storytime = {
        "story": "There once was a lad, that's it that the story :)"
    }
    return storytime


#get methods for Spotify
 
@app.get('/genres')
def get_genres():
    query = "SELECT * FROM genres ORDER BY genreid;"
    try:    
        cur.execute(query)
        headers=[x[0] for x in cur.description]
        results = cur.fetchall()
        json_data=[]
        for result in results:
            json_data.append(dict(zip(headers,result)))
        return(json_data)
    except Error as e:
        print("MySQL Error: ", str(e))
        return {"Error": "MySQL Error: " + str(e)}

@app.get('/songs')
def get_songs():
    query = "Select * From songs ORDER BY id;"
    try:
        cur.execute(query)
        headers=[x[0] for x in cur.description]
        results = cur.fetchall()
        json_data=[]
        for result in results:
            json_data.append(dict(zip(headers,result)))
        return(json_data)
    except Error as e:
        print("MySQL Error: ", str(e))
        return {"Error": "MySQL Error: " + str(e)}