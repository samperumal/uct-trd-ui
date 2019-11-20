import sys
import time
import pydim
from flask import Flask, g, request

app = Flask(__name__)
cache = {}

def feeState(state):
    print("Message received: '%s' (%s)" % (state, type(state)))
    cache["state"] = state

@app.before_first_request
def activate_job():
    if not pydim.dis_get_dns_node():
        print("No Dim DNS node found. Please set the environment variable DIM_DNS_NODE")
        sys.exit(1)

    # res3 = pydim.dic_sync_info_service("trdbox/RUN_NUMBER")
    # print("example-service-sync returned %s" % str(res3[0]))

    pydim.dic_info_service("ztt_dimfed_server_trd-fee_00_2_0_STATE", feeState)

@app.route('/')
def hello_world():
    return 'Hello, World! Current state is {0}'.format(cache["state"])

if __name__ == "__main__":
    app.run()