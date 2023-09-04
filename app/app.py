from flask import Flask, request, jsonify, make_response

app = Flask(__name__)


def handle_cors_response(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'  # allows any origin, adjust if necessary
    resp.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    resp.headers['Access-Control-Allow-Headers'] = 'Content-Type, User-Agent'
    return resp


@app.route('/email', methods=['POST', 'OPTIONS'])
def record_email():
    if request.method == 'OPTIONS':  # this will handle the pre-flight request
        resp = make_response()
        return handle_cors_response(resp)

    try:
        # Get email from the incoming JSON
        data = request.json
        email = data.get('email')

        if not email:
            resp = make_response(jsonify({"succeeded": False, "error": "Email not provided"}), 400)
        else:
            # Append email to the local file
            with open('emails.txt', 'a') as f:
                f.write(email + '\n')
            resp = make_response(jsonify({"succeeded": True}))

        return handle_cors_response(resp)
    except Exception as e:
        resp = make_response(jsonify({"succeeded": False, "error": str(e)}))
        return handle_cors_response(resp)


@app.route('/is-up', methods=['GET'])
def is_up():
    return "A rollicking band of pirates we"

if __name__ == '__main__':
    app.run(debug=True, port=1234)

