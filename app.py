import json
from flask import Flask, jsonify, request




app = Flask(__name__)

# read file
with open('\data.json', 'r') as myfile:
    data = json.load(myfile)
    


@app.route("/", methods=["GET"])
def index():
    return "Booking system home page"

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

@app.route("/venues", methods=["GET","POST","DELETE","PUT"])
def venue():
    #READ VENUE
    if(request.method=="GET"):
        venues=[]
        for i in data["venue"]:

            venues.append(i)
        

        return venues
    #CREATE VENUE
    elif(request.method=="POST"):
        body=request.get_json()
        venues=data["venue"]
        
        venues.append(body)
        with open("\data.json", 'w') as f:
            json.dump(data, f, indent=4)
        return venues  
    #DELETE VENUE  
    elif(request.method=="DELETE"):
        body=request.get_json()
        venues=data["venue"]
        
        index=venues.index(body)
        venues.pop(index)
        
        with open("\data.json", 'w') as f:
            json.dump(data, f, indent=4)
        return venues
    #UPDATE VENUE
    elif(request.method=="PUT"):
        body=request.get_json()
        venues=data["venue"]
        index=venues.index(body[0])
        venues.pop(index)
        venues.append(body[1])

        
        
        
        with open("\data.json", 'w') as f:
            json.dump(data, f, indent=4)
        return venues
    



    
@app.route("/venues/<int:id>", methods=["GET","POST","DELETE"])
def venue_id(id):
    #VENUES READ PER ID
    if(request.method=="GET"):
        venues=data["venue"]
        for i in venues:
            if((i["ID"])==id):
                return i
            else:
                return ("not found")
                
    
    if(request.method=="DELETE"):
        venues=data["venue"]
        for i in venues:
            if((i["ID"])==id):
                index=venues.index(i)
                venues.pop(index)
                return venues  
        else:
            return("element not found")


        

        

   













    



@app.route("/shows", methods=["GET","POST","DELETE","PUT"])
def show():
     #READ SHOW
    if(request.method=="GET"):
        shows=[]
        for i in data["show"]:

            shows.append(i)
        

        return shows
    #CREATE SHOW
    elif(request.method=="POST"):
        body=request.get_json()
        shows=data["venue"]
        
        shows.append(body)
        with open("\data.json", 'w') as f:
            json.dump(data, f, indent=4)
        return shows  
    #DELETE SHOW 
    elif(request.method=="DELETE"):
        body=request.get_json()
        shows=data["show"]
        
        index=shows.index(body)
        shows.pop(index)
        
        with open("\data.json", 'w') as f:
            json.dump(data, f, indent=4)
        return shows
    #UPDATE SHOW
    elif(request.method=="PUT"):
        body=request.get_json()
        shows=data["show"]
        index=shows.index(body[0])
        shows.pop(index)
        shows.append(body[1])

        
        
        
        with open("\data.json", 'w') as f:
            json.dump(data, f, indent=4)
        return shows
    



if __name__ == "__main__":
    app.run(debug=True, port=8000)