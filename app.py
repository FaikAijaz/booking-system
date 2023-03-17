import json, html
from flask import Flask, jsonify, request




app = Flask(__name__)

# read file
with open('booking-system\data.json', 'r') as myfile:
    data = json.load(myfile)
    


@app.route("/", methods=["GET"])
def index():
    return jsonify(data["venue"])

@app.route("/login", methods=["GET","POST"])

def login():
    if(request.method=="POST"):
        body=request.get_json()
        for i in data["user"]:
            un=i["username"]
            ps=i["password"]
            if(body["username"] == un):
                if(body["password"]==ps):
                
                
                    return ({"message":"login successfull"})
                else:
                    return({"message":"password does not exist"})
                

            
        return({"message":"user does not exist"})
                
            
        
        
    elif(request.method=="GET"):
        return jsonify({})



if __name__ == "__main__":
    app.run(debug=True, port=8000)