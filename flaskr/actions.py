import subprocess
from . import pydim_wrapper

def available_actions(state):
    state = int(state)
    if state == 5: return ["INITIALIZE", "TEST"]
    elif state == 43: return ["CONFIGURE", "GO_STANDBY"]
    else: return ["RESET"]

def run_action(action):
    print("Running action: {0}".format(action))
    
    args = None
    if action == "INITIALIZE":
        args = ["nginject", "all", "10"]
    elif action == "RESET":
        args = ["nginject", "all", "90"]

    if args != None:
        #result = subprocess.run(args, stdout=subprocess.PIPE, universal_newlines= True)
        
        #return (result.stdout)
        pydim_wrapper.ConfigureFero(args[2])
        return "Requested ConfigureFero with tag {0}".format(args[2])