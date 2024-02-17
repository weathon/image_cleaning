from fastapi import FastAPI
import sqlite3
import os 

con = sqlite3.connect("database.db")
app = FastAPI()


@app.get("/get_image_url")
async def get_image():
    cur = con.cursor()
    res = cur.execute("SELECT filename FROM images WHERE accept IS NULL LIMIT 1")
    return res.fetchone()

@app.get("/reset_database")
async def reset_database():
    cur = con.cursor()
    filenames = [(i,) for i in os.listdir("images")]
    cur.execute("delete from images;")
    res = cur.executemany("INSERT INTO images VALUES(?, NULL)", filenames)
    con.commit()
    return res 

@app.get("/submit")
async def submit(filename, decision):
    cur = con.cursor()
    res = cur.execute("UPDATE images SET accept=? WHERE filename=?", (decisionm, filename))
    con.commit()
    return res 

@app.get("/view_table")
async def view_table(filename, decision):
    cur = con.cursor()
    res = cur.execute("SELECT * FROM images")
    return res 