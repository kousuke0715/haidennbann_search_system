from flask import Flask,request,render_template
import sqlite3
app=Flask(__name__)
@app.route("/")
def login():
    return render_template("okada_log_in.html")
@app.route("/login",methods=["POST"])
def Login():
    s_id=request.form.get("syain_id")
    name=request.form.get("name")
    return render_template("okada.html", syain_id=s_id, name=name)
@app.route("/search",methods=["POST"])
def search():
    s_id=request.form.get("syain_id")
    name=request.form.get("name")
    maker=request.form.get("maker")
    pole=request.form.get("pole")
    frame=request.form.get("frame")
    trip=request.form.get("trip")
    connect=request.form.get("connect")
    setten=request.form.get("setten")
    conn=sqlite3.connect("okada.db")
    conn.row_factory=sqlite3.Row
    cur=conn.cursor()
    cur.execute("""SELECT*FROM prodacts WHERE maker=? AND pole=? AND frame=? AND trip=? AND connect=? AND setten=?""",(maker,pole,frame,trip,connect,setten))
    detail=cur.fetchall()
    return render_template("okada.html",detail=detail,syain_id=s_id,name=name)
@app.route("/next",methods=["GET"])
def next():
    return render_template("test.katana1000.html")
if __name__=="__main__":
    app.run(debug=True)
