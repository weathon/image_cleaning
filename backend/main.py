from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import sqlite3
import os 
from fastapi.staticfiles import StaticFiles

# app = FastAPI()


con = sqlite3.connect("database.db")
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/get_image_url")
async def get_image():
    cur = con.cursor()
    res = cur.execute("SELECT filename FROM images WHERE accept IS NULL LIMIT 1")
    ans = res.fetchone()
    if ans is None:
        return "finished"
    return ans

@app.get("/api/reset_database")
async def reset_database():
    cur = con.cursor()
    filenames = [(i,) for i in os.listdir("images")]
    cur.execute("delete from images;")
    res = cur.executemany("INSERT INTO images VALUES(?, NULL)", filenames)
    con.commit()
    return res 

@app.post("/api/submit")
async def submit(filename, decision):
    cur = con.cursor()
    res = cur.execute("UPDATE images SET accept=? WHERE filename=?", (decision, filename))
    con.commit()
    return res 

@app.get("/api/view_table")
async def view_table():
    cur = con.cursor()
    res = cur.execute("SELECT * FROM images")
    return res 

@app.get("/api/img")
async def img(filename):
    return FileResponse("images/"+filename)

app.mount("/", StaticFiles(directory="dist"), name="dist")
@app.exception_handler(404)
async def custom_404_handler(_, __):
    return FileResponse('./dist/index.html')