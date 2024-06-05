from flask import Flask, json, request, jsonify
from Core.AuthenticateManagement.classes.IdentityManager import IdentityManager
from Common.LogManager import LogManager
from Core.ConfigManagement.ConfigManager import *

logger = LogManager()
app = Flask(__name__)






@app.route('/Register', methods=['POST'])
def register():
    try:
        if stub == 1:
            stubJson = load_json_file("Stub\\registerStub.json")
            return jsonify(stubJson)
        else:
            input_json = request.get_json()
            identity = IdentityManager.register(input_json)
            return jsonify(identity)
    except Exception as e:
        logger.log("ERROR",f'Error in register Function: {e}')
        return  str(e)

@app.route('/Login', methods=['POST'])
def Authenticate():
    try:
        if stub == 1:
            stubJson = load_json_file("Stub\\authenticateStub.json")
            return jsonify(stubJson)
        else:
            input_json = request.get_json()
            identity = IdentityManager.Authenticate(input_json)
            return jsonify(identity)
    except Exception as e:
        logger.log("ERROR",f'Error in authenticate Function: {e}')
        return  str(e)
    

@app.route('/Logout', methods=['POST'])
def logout():
    try:
        if stub == 1:
            stubJson = load_json_file("Stub\logoutStub.json")
            return jsonify(stubJson)
        else:
            input_json = request.get_json()
            identity = IdentityManager.logout(input_json)
            return jsonify(identity)
    except Exception as e:
        logger.log("ERROR",f'Error in logout Function: {e}')
        return  str(e)
    

@app.route('/activateUser', methods=['POST'])
def activateUser():
    try:
        if stub == 1:
            stubJson = load_json_file("Stub\logoutStub.json")
            return jsonify(stubJson)
        else:
            input_json = request.get_json()
            authkey = input_json.get("authkey","")
            identity = IdentityManager.ActivateUser(authkey)
            return jsonify(identity)
    except Exception as e:
        logger.log("ERROR",f'Error in activate user Function: {e}')
        return  str(e)


@app.route('/display', methods=['GET'])
def display():
    """ Display Function"""
    try:
        return ("NLP-API Version 5.0")
    except Exception as e:
        logger.log("ERROR",f'Error in display Function: {e}')
        return (str(e))



if __name__ == '__main__':
    app.run(port=5002, debug=True)




