from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        message = data.get("message", "")

        if not message:
            return jsonify({"error": "No input received"}), 400

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": message}]
        )

        reply = response.choices[0].message.content
        return jsonify({"reply": reply})
    
    except Exception as e:
        print("🔥 Error:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
