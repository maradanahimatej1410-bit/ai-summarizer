from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "AI Summarizer Agent is running!"

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Please provide text"}), 400

    text = data["text"]

    # Simple summarization logic
    words = text.split()
    summary = " ".join(words[:10])  # first 10 words

    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
