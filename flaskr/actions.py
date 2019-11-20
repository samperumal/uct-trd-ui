def available_actions(state):
    if state == 5: return (["INITIALIZE", "TEST"])
    elif state == 43: return (["CONFIGURE", "GO_STANDBY"])
    else: return (["RESET"])
