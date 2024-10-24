#!/usr/bin/env python3

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import json
import os

app = FastAPI()

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