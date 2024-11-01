from flask import Flask, render_template, request, jsonify, redirect
from flask_cors import CORS
import sqlite3
import uuid
app = Flask(__name__)
CORS(app)
def get_db_connection():
    conn = sqlite3.connect('url_shortener.db') 
    conn.row_factory = sqlite3.Row 
    return conn

def init_db():
    with get_db_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS url_mapping (
                id TEXT PRIMARY KEY,
                original_url TEXT NOT NULL
            )
        ''')
        conn.commit()

init_db()

@app.route("/")
def homePage():
       return render_template("index.html")

@app.route("/shorten", methods=["POST"])
def shortenUrl():
    data = request.get_json()
    original_Url = data.get("url")
    
    if not original_Url:
          return jsonify({"error": 'URL não fornecida'}), 400

    random_id = str(uuid.uuid4())
    short_id = random_id[:6]
    short_URL = f"http://localhost:5000/{short_id}"

    with get_db_connection() as conn:
        conn.execute('INSERT INTO url_mapping (id, original_url) VALUES (?, ?)', (short_id, original_Url))
        conn.commit()

    return jsonify({'shortenedURL': short_URL})

@app.route("/<string:id>")
def redirect_to_url(id):
    print(f"Buscando no banco de dados: ID={id}")
    with get_db_connection() as conn:
        original_url = conn.execute('SELECT original_url FROM url_mapping WHERE id = ?', (id,)).fetchone()
        
    if original_url:
        return redirect(original_url['original_url'])   
    else:
        return "URL não encontrada", 404
app.run(debug=True)
