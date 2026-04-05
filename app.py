# Noah Haeger - Flask Application

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to Noah Haeger's Flask App</h1>
    <p>This is my first dynamic website using Flask.</p>
    <p>Future Technology Risk Auditor 🚀</p>
    """

@app.route("/about")
def about():
    return """
    <h2>About Me</h2>
    <p>I am a Business Analytics and Finance student interested in technology and data.</p>
    <p>I am currently building skills in Python, data analysis, and web development.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)