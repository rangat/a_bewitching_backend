import sys
sys.path.insert(0,"../")
import json
import config
import boto3
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
client = boto3.client('sns')

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/flicker', methods=['POST'])
def flicker():
    #push to sns
    try:
        action_dict = {"action":"flicker"}
        send_message(json.dumps(action_dict),"action")
        return jsonify(success=True)
    except:
        return jsonify(success=False)

@app.route('/clown', methods=['POST'])
def clown():
    try:
        action_dict = {"action":"clown"}
        send_message(json.dumps(action_dict),"action")
        return jsonify(success=True)
    except:
        return jsonify(success=False)

@app.route('/blinds', methods=['POST'])
def blinds():
    try:
        action_dict = {"action":"blinds"}
        send_message(json.dumps(action_dict),"action")
        return jsonify(success=True)
    except:
        return jsonify(success=False)

@app.route('/shadow', methods=['POST'])
def shadow():
    try:
        action_dict = {"action":"shadow"}
        send_message(json.dumps(action_dict),"action")
        return jsonify(success=True)
    except:
        return jsonify(success=False)

@app.route('/fog', methods=['POST'])
def fog():
    try:    
        action_dict = {"action":"fog"}
        send_message(json.dumps(action_dict),"action")
        return jsonify(success=True)
    except:
        return jsonify(success=False)

@app.route('/coffin', methods=['POST'])
def coffin():
    try:
        action_dict = {"action":"coffin"}
        send_message(json.dumps(action_dict),"action")
        return jsonify(success=True)
    except:
        return jsonify(success=False)

@app.route('/doll', methods=['POST'])
def doll():
    try:
        action_dict = {"action":"doll"}
        send_message(json.dumps(action_dict),"action")
        return jsonify(success=True)
    except:
        return jsonify(success=False)

def send_message(msg,subject:str):
    client.publish(
            TopicArn = config.sns_arn,
            Message = msg,
            Subject = subject,
            MessageStructure = 'string'
        )
