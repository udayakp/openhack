from flask import Flask
import aimodule
application = Flask(__name__)

@application.route("/")
def hello():
	return render_template('chat.html')
    	aimodule.train()

@app.route("/ask", methods=['POST'])
def ask():
	message = str(request.form['messageText'])
    	# kernel now ready for use
    	while True:
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
