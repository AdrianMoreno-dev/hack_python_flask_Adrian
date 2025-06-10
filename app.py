from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route("/users", methods=["GET"])
def get_users(): 
    return jsonify({'payload': 'success'}), 200 

@app.route("/user", methods=["POST","DELETE"])
def  post_user():
    return jsonify({'payload': 'success'}), 200

@app.route("/user", methods=["PUT"])
def  put_user():
    return jsonify({'payload': "success", "error":False}), 200

@app.route("/api/v1/users", methods=["GET"])
def  get_user():
    payload = []
    return jsonify({'payload':payload}), 200

@app.route("/api/v1/user", methods=["POST"])
def create_user():
    email = request.args.get('email')
    name = request.args.get('name')
    
    payload = {
                'email': email,
                'name': name,
            }
    return jsonify({'payload': payload}), 200

@app.route("/api/v1/user/add", methods=["POST"])
def add_user():
    email = request.form.get('email')
    name = request.form.get('name')
    user_id = request.form.get('id')
    payload = {
                'email': email,
                'name': name,
                'id': user_id,

            }
    return jsonify({'payload': payload}), 200

@app.route('/api/v1/user/create', methods=['POST'])
def create_users():
    data = request.get_json()
    email = data.get('email')
    name = data.get('name')
    user_id = data.get('id')

    payload = {
        'email': email,
        'name': name,
        'id': user_id,
    }

    return jsonify({'payload': payload}), 200


@app.route ("/index")
def index():
    user_ip_information = request.remote_addr
    return render_template("ip_information.html", user_ip_information=user_ip_information)

if __name__ == "__main__":
    app.run(debug=True)