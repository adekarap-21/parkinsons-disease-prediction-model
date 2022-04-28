from flask import Flask,render_template
import parkinson

app = Flask(__name__)

@app.route("/")
def index():
    result = parkinson.parkinsons_detection()
    return render_template("./result.html",res=result[0])

if __name__ == '__main__':
    app.run(debug=True)