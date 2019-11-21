#import pydim
import subprocess

def available_actions(state):
    state = int(state)
    if state == 5: return ["INITIALIZE", "TEST"]
    elif state == 43: return ["CONFIGURE", "GO_STANDBY"]
    else: return ["RESET"]

def run_action(action):
    print("Running action: {0}".format(action))
    
    if action == "INITIALIZE":
        subprocess.run(["nginject", "10"])
    elif action == "RESET":
        subprocess.run(["nginject", "90"])