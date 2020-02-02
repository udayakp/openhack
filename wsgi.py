from flask import Flask, render_template, request, jsonify
import aimodule
import aimfmodule
#import requests
import json
application = Flask(__name__)
url = "http://10.123.79.234:9081/zosapiconnect/fetchapplicant/"
@application.route("/")
def hello():
    aimodule.train()
    return render_template('chat.html')
    
@application.route("/ask", methods=['POST'])
def ask():
    # kernel now ready for use
    while True:
        message = str(request.form['messageText'])
        m1 = message[:5]
        if message == "quit":
            aimodule.record()
        elif message == "save":
            aimodule.saveBrain("bot_brain.brn")
        elif message == "#elp":
            aimodule.incident()
        elif m1 == "fetch":
            bot_response = aimfmodule.fetch(url,message)
            return jsonify({'status':'OK','answer':bot_response})
        else:
            bot_response = aimodule.respond(message)
            # print bot_response
            return jsonify({'status':'OK','answer':bot_response})


if __name__ == "__main__":
    application.run()
