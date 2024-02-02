from flask import Flask, render_template, url_for, request, redirect, jsonify
from pymongo import MongoClient
from flask_bcrypt import Bcrypt
from bson import ObjectId
app = Flask(__name__)
bcrypt = Bcrypt(app)
#our Mongo DB
client = MongoClient('localhost', 27017)
db = client.flask_database
#Create
@app.route("/registerUser", methods=['POST'])

def registerUser():
    user_data = request.get_json()
    if 'username' not in user_data or 'email' not in user_data or 'password' not in user_data:
        return jsonify({'error' : 'Missing Required Feilds'}), 400
    
    existing_user = users.find_one({'email' : user_data['email']})
    if existing_user:
        return jsonify({'error' : 'User alredy exits'}), 400
    user_id = users.insert_one({
        'username' : user_data['username'],
        'email' : user_data['email'],
        'password' : bcrypt.generate_password_hash(user_data['password']).decode('utf-8')
    }).inserted_id
    return jsonify({'message' : 'User Registered', 'user_id' : str(user_id)}), 201
#View All
@app.route("/getUsers", methods=['GET'])
def getAll():
    allUsers = users.find({}, {'password': 0})  # Exclude password field from the response
    user_list = []

    for user in allUsers:
        user['_id'] = str(user['_id'])  # Convert ObjectId to string for JSON serialization
        user_list.append(user)

    return jsonify({'users': user_list})
#view User with ID
@app.route("/getUser/<string:user_id>")
def getUserById(user_id):

    try:
        obj_id = ObjectId(user_id)
        user = users.find_one({'_id' : obj_id}, {'password' : 0})
        if user:
            user['_id'] = str(user['_id'])
            return jsonify({'user' : user})
        else:
            return jsonify({'error' : 'User not found'}), 404
    except Exception as e:
        return jsonify({'error' : 'Invalid user ID'}), 400

#Update User
@app.route("/updateUser/<string:user_id>", methods=['PUT'])
def updateUser(user_id):
    try:
        # Convert the provided user_id to ObjectId
        object_id = ObjectId(user_id)
        user = users.find_one({'_id': object_id})

        if user:
            # Get updated user data from the request
            updated_data = request.get_json()
            hashed_password = bcrypt.generate_password_hash(updated_data['password']).decode('utf-8')
            # Update user fields if provided
            if 'username' in updated_data:
                user['username'] = updated_data['username']
            if 'email' in updated_data:
                user['email'] = updated_data['email']
            if 'password' in updated_data:
                user['password'] = hashed_password

            # Save the updated user data to the database
            users.update_one({'_id': object_id}, {'$set': user})

            return jsonify({'message': 'User updated successfully'})
        else:
            return jsonify({'error': 'User not found'}), 404
    except Exception as e:
        return jsonify({'error': 'Invalid user ID'}), 400
#Delete User
@app.route("/deleteUser/<string:user_id>", methods=['DELETE'])

def deleteUser(user_id):
    try:
        # Convert the provided user_id to ObjectId
        object_id = ObjectId(user_id)
        result = users.delete_one({'_id': object_id})

        if result.deleted_count > 0:
            return jsonify({'message': 'User deleted successfully'})
        else:
            return jsonify({'error': 'User not found'}), 404
    except Exception as e:
        return jsonify({'error': 'Invalid user ID'}), 400


#Users Collections
users = db.users

if __name__ == "__main__":
    app.run(debug=True) 