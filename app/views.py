from flask import Blueprint, render_template, request, jsonify, redirect
from .models import insert_url, get_url_by_code
import uuid

views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
def shorten_url():
    if request.method == "POST":
        data = request.get_json()
        long_url = data.get("long_url")

        if not long_url:
            return jsonify({"message": "URL não fornecida"}), 400
        
        generated_uuid = str(uuid.uuid4())
        short_code = generated_uuid[:6]

        insert_url(long_url, short_code)

        PRODUCTION = 'https://shorturl.onrender.com/';
        short_url = f"{PRODUCTION}{short_code}"
        
        return jsonify({"short_url": short_url})

    
    return render_template("index.html")

@views.route("/<short_code>")
def redirect_to_long_url(short_code):
    long_url = get_url_by_code(short_code)
    
    if long_url:
        return redirect(long_url)
    else:
        return jsonify({"message": "Código não encontrado"}), 404