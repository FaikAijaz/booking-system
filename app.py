import json
from flask import Flask, jsonify, request


app = Flask(__name__)

# read file
with open('\data.json', 'r') as myfile:
    data = json.load(myfile)
    


@app.route("/", methods=["GET"])
def index():
    return "Booking system home page"



############### ADMIN #############################   

# Register route for admin
@app.route("/admin/register", methods=["POST"])
def admin_register():
    if(request.method=="POST"):
        body=request.get_json()
        admins=data["admin"]
        admins.append(body)
        with open("\data.json", 'w') as f:
            json.dump(data, f, indent=4)
        return admins


@app.route("/admin/login", methods=["GET","POST"])
def admin_login():
    if(request.method=="POST"):
        body=request.get_json()
        for i in data["admin"]:
            un=i["username"]
            ps=i["password"]
            if(body["username"] == un):
                if(body["password"]==ps):
                
                
                    return ({"message":"login successfull"})
                else:
                    return({"message":"password does not exist"})
                

            
        return({"message":"Admin does not exist"})
        
    elif(request.method=="GET"):
        return jsonify({})

@app.route("/admin/venues", methods=["GET","POST"])
def admin_venue():
    #READ VENUE
    if(request.method=="GET"):
        venues=[]
        for i in data["venue"]:
            venues.append(i)
        return jsonify(venues)
    #CREATE VENUE
    elif(request.method=="POST"):
        body=request.get_json()
        venues=data["venue"]
        
        venues.append(body)
        with open("\data.json", 'w') as f:
            json.dump(data, f, indent=4)
        return venues  




    
@app.route("/admin/venues/<id>", methods=["DELETE","GET"])
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



@app.route("/admin/shows", methods=["GET","POST"])
def admin_show():
     #READ SHOW
    if(request.method=="GET"):
        shows=[]
        for i in data["show"]:
            shows.append(i)
        return (shows)
    #CREATE SHOW
    elif(request.method=="POST"):
        body=request.get_json()
        shows=data["show"]
        
        shows.append(body)
        with open("\data.json", 'w') as f:
            json.dump(data, f, indent=4)
        return shows  
    ### EDIT SHOWS
@app.route("/admin/shows", methods=["PUT"])
def edit_shows():
    body=request.get_json()
    shows=data["show"]
    index=shows.index(body[0])
    shows.pop(index)
    shows.append(body[1])
    
    with open("\data.json", 'w') as f:
        json.dump(data, f, indent=4)
    return shows
#### EDIT VENUES
@app.route("/admin/venues", methods=["PUT"])
def edit_venues():
    body=request.get_json()
    venues=data["venue"]
    index=venues.index(body[0])
    venues.pop(index)
    venues.append(body[1])
    
    with open("\data.json", 'w') as f:
        json.dump(data, f, indent=4)
    return venues

    
@app.route("/admin/shows/<int:id>", methods=["DELETE","GET"])
def show_id(id):
    #SHOWS READ PER ID
    if(request.method=="GET"):
        shows=data["show"]
        for i in shows:
            if((i["ID"])==id):
                return i
        else:
            return ("not found")
                
    
    if(request.method=="DELETE"):
        shows=data["show"]
        for i in shows:
            if((i["ID"])==id):
                index=shows.index(i)
                shows.pop(index)
                return shows  
        else:
            return("element not found")
        ##admin summary
@app.route("/admin/summary", methods=["GET"])
def summary():
    return jsonify({})



#########################   USER   ##########################

@app.route("/user/login", methods=["POST","GET"])
def user_login():
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
    

# Register route for user
@app.route("/user/register", methods=["POST"])
def user_register():     
    if(request.method=="POST"):
        body=request.get_json()
        users=data["user"]
        users.append(body)
        with open("\data.json", 'w') as f:
            json.dump(data, f, indent=4)
        return users
    

@app.route("/user/shows", methods=["GET"])
def user_show():
     #READ SHOW
    if(request.method=="GET"):
        shows=[]
        for i in data["show"]:

            shows.append(i) 

    return jsonify(shows)
@app.route("/user/venues", methods=["GET"])
def user_venue():
     #READ venues
    if(request.method=="GET"):
        venues=[]
        for i in data["venue"]:

            venues.append(i)    

        return jsonify(venues)
@app.route("/user/bookings", methods=["GET","POST"])
def booking():
     #READ bookings
    if(request.method=="GET"):
        bookings=[]
        for i in data["booking"]:

            bookings.append(i)
        

        return bookings
    #CREATE booking
    elif(request.method=="POST"):
        body=request.get_json()
        bookings=data["booking"]
        
        bookings.append(body)
        with open("\data.json", 'w') as f:
            json.dump(data, f, indent=4)
        return bookings                       

if __name__ == "__main__":
    app.run(debug=True, port=8000)