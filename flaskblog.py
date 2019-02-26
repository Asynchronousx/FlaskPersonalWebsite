from flask import Flask, render_template, url_for
import MySQLdb
import html
app = Flask(__name__)

#route means redirect something on that specific "address".
#i.e: "/" is the root of our website, aka the homepage.
#also, two route decorator means that we're adding another route to that page.
#see decorator example for understanding.
@app.route("/")
@app.route("/home")
def home():
    #the second argument means that whatever variable we pass into the render_template function, 
    #it will be accessible by that same function. (posts can be now elaborated)
    return render_template('home.html', title='')

#second example: this route, when added to the route, will route the user to the /about page.
@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/posts")
def posts():

    postList = []

    #instantiate connection
    postDB = MySQLdb.connect (
        host="host",
        user="user",
        passwd="passwd",
        db="db"
    )

    #init the cursor and query the bd
    cursor = postDB.cursor()
    query = "SELECT * FROM TABLE ORDER BY ID DESC"
    cursor.execute(query)

    #fetch all the rows
    result = cursor.fetchall()

    for row in result:
        #save html content and format properly
        postList.append(
            {'title': row[1],
             'content': row[2],
             'author': row[3],
             'date': row[4].strftime('%d %b, %Y')
            }
        )

    return render_template('posts.html', title="Posts", posts=postList)

@app.route("/resumee")
def resumee():
    return render_template('resumee.html', title="Resumee")


#This will be true only when RUNNED by terminal. 
if __name__ == "__main__":
    #if ran by terminal, run the app in debug mode.
    app.run(debug=True)    
