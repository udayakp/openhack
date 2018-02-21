from flask import Flask, render_template, request, jsonify
import aimodule
application = Flask(__name__)

@application.route("/")
def hello():
    aimodule.train()
    return render_template('chat.html')
    
@application.route("/ask", methods=['POST'])
def ask():
    # kernel now ready for use
    while True:
        message = str(request.form['messageText'])
        if message == "quit":
            aimodule.record()
        elif message == "save":
            aimodule.saveBrain("bot_brain.brn")
        elif message == "#elp":
            aimodule.incident()
        else:
            bot_response = aimodule.respond(message)
            # print bot_response
            return jsonify({'status':'OK','answer':bot_response})


if __name__ == "__main__":
    application.run()
