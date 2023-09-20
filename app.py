import sys, json, uuid
import sqlite3 as sql
sys.path.insert(1, 'C:\\Users\\yoyow\\Desktop\\פרויקטים כיתה\\chess_project\\piecesClass')
from flask import Flask, render_template, url_for, request, jsonify, redirect,session
from board import Board
from appFuncs import turnCount







app = Flask(__name__)
app.secret_key = "uuid.uuid1()"


login = True

@app.route('/',methods=['GET', 'POST'])
def index():
        global board
        global count
        count = 0
        turn = turnCount(count)
        board = Board()
        board.set_game()
        return render_template("index.html", board=board, turn=turn, login=login)

@app.route('/get_moves/<yx>')
def get_moves(yx):
    global board
    global count
    turn = turnCount(count)
    y,x = int(yx[0]),int(yx[1])
    obj = board.board[y][x]
    moves = obj.move(board.board)
    print(moves)
    return render_template("get_moves.html", board=board, moves=moves ,obj=obj, turn=turn)

@app.route('/move/<yxyx>')
def move(yxyx):
    global count
    global board
    count +=1
    turn = turnCount(count)
    y,x = int(yxyx[0]),int(yxyx[1])
    y2,x2 = int(yxyx[2]),int(yxyx[3])
    board.move((y2,x2),(y,x))
    #if board.check_win():
    #    return board.check_win()
    return render_template("move.html", board=board, turn=turn)


@app.route("/login",  methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        statement = f""" SELECT * FROM users WHERE username = '{username}' AND password='{password}';"""
        con = sql.connect("C:\\Users\\yoyow\\Desktop\\mysqlDATABASES\\users.db")
        cur = con.cursor()
        cur.execute(statement)
        user = cur.fetchall()
        if user !=[]:
            session.permanent = True
            session['user'] = user[0]
            return redirect(url_for("user"))
        else:
            return render_template("login.html", fail=True)
    else:
        return render_template("login.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")


@app.route("/user")
def user():
    if "user" in session:
        return render_template("user.html")
    else:
        return "you are not loged in"



@app.route("/register", methods= ["POST","GET"])
def register():
    if request.method == "POST":
        failString = ""
        
        username = request.form.get("username").lower()
        if  len(username)<8 or len(username)>16:
            failString += " Username must be between 8-16 charecters"

        password = request.form.get("password")
        if  len(password)<8 or len(password)>16:
            failString += " Password  must be between 8-16 charecters"

        firstname = request.form.get("firstname").lower
        if firstname == "":
            failString += " must input first name"

        lastname = request.form.get("lastname").lower
        if lastname == "":
            failString += " must input last name"

        date = request.form.get("date")
        if date == "":
            failString += " must input date"

        email = request.form.get("email").lower
        if email == "":
            failString += " Must input email"
        
        if failString != "":
            return failString

        statement = f"""INSERT INTO 'users' ('username', 'password', 'firstname', 'lastname', 'date', 'email') VALUES ('{username}', '{password}', '{firstname}', '{lastname}', '{date}', '{email}');"""

        try:
            con = sql.connect("C:\\Users\\yoyow\\Desktop\\mysqlDATABASES\\users.db")
            print("con ok")
            con.execute(statement)
            print("exectiontion ok")
            con.commit()
            print("commit ok")
            con.close()
        except:
            return "something went wrong with your registeraion"
        return redirect("/")
    else:
        return render_template("register.html")



if __name__ == "__main__":
    app.run(debug=True, port=9000)