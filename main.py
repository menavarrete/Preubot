import flask
import os
import telegram as tg

app = flask.Flask(__name__)

@app.route("/")
def main():
    return "Hola"


@app.route('/telegram', methods=["POST"])
def telegram():
    message = flask.request.get_json()
    if "message" in message:
        user = message["message"]["from"]["id"]
        try:
            body = message["message"]["text"]
            tg.handle(user, body)
        except:
            pass
    return ""



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 33507))
    app.run(host='localhost', port=port)
    #app.run(host='0.0.0.0', port=port)
