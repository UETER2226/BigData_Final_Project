from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from uuid import uuid4
from chat import ask_question
from gg_search import get_google_search_results
import os
import sys
app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["POST"])
def chat():
    msg = request.form["msg"]
    question = msg
    session_id = request.args.get("session_id", str(uuid4()))
    chatbot_answer = ask_question(question, session_id)
    search_results = get_google_search_results(question)
    return jsonify({
        "answer": chatbot_answer,
        "search_results": search_results
    })
@app.cli.command()
def create_index():
    """Create or re-create the Elasticsearch index."""
    basedir = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(f"{basedir}/../")

    from data import index_data

    index_data.main()

if __name__ == '__main__':
    app.run(debug= True)