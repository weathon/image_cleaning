from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import sqlite3
import os 

con = sqlite3.connect("database.db")
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/get_image_url")
async def get_image():
    cur = con.cursor()
    res = cur.execute("SELECT filename FROM images WHERE accept IS NULL LIMIT 1")
    ans = res.fetchone()
    if ans is None:
        return "finished"
    return ans

@app.get("/reset_database")
async def reset_database():
    cur = con.cursor()
    filenames = [(i,) for i in os.listdir("images")]
    cur.execute("delete from images;")
    res = cur.executemany("INSERT INTO images VALUES(?, NULL)", filenames)
    con.commit()
    return res 

@app.post("/submit")
async def submit(filename, decision):
    cur = con.cursor()
    res = cur.execute("UPDATE images SET accept=? WHERE filename=?", (decision, filename))
    con.commit()
    return res 

@app.get("/view_table")
async def view_table():
    cur = con.cursor()
    res = cur.execute("SELECT * FROM images")
    return res 

@app.get("/img")
async def img(filename):
    return FileResponse("images/"+filename)