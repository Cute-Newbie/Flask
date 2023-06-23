from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route("/login")
def login():
    username = request.args.get("user_name") # 파라미터 값이 username변수에 저장된다.
    password = request.args.get("pw")
    email = request.args.get("email_address")
    print(username,password,email)
    
    if username == "dave":
        return_data = {"auth":"success"}
    else:
        return_data = {"auth":"failed"}
        
    return jsonify(return_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port = "8081") 

    
