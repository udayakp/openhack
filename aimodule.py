import aiml
from os import listdir
from os.path import dirname, isfile

kernel = aiml.Kernel()

aiml_path = dirname(__file__) + "/aiml"
brain_path = dirname(__file__) +"/bot_brain.brn"

def train():
    if isfile(brain_path):
        kernel.bootstrap(brainFile = "bot_brain.brn")
    else:
        aimls = listdir(aiml_path)
        for aiml in aimls:
            kernel.bootstrap(learnFiles=aiml_path + "/" + aiml)
        kernel.saveBrain("bot_brain.brn")

def record():
    print (kernel.getSessionData())

def respond(msg):
    return kernel.respond(msg)

def incident():
    return kernel.getSessionData()
    

    
