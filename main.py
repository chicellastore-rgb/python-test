from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "تجربة هنادي على Render!"

if __name__ == "__main__":
    app.run()
