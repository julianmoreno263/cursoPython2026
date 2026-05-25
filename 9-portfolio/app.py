from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")






if __name__ == '__main__':
    # Ejecuta el servidor local en modo desarrollo (debug)
    app.run(debug=True, port=5000)