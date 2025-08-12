from flask import Flask, jsonify
import requests

app = Flask(__name__)

GITHUB_API_URL = "https://api.github.com/users/{}/gists"

@app.route("/<username>", methods=["GET"])
def get_user_gists(username):
    response = requests.get(GITHUB_API_URL.format(username))

    if response.status_code != 200:
        return jsonify({"error": "GitHub user not found"}), 404

    gists = response.json()
    gist_list = [{"id": gist["id"], "description": gist["description"], "url": gist["html_url"]} for gist in gists]

    return jsonify(gist_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
