import pydim

def get_service_callback(key, signal_update_delegate):
    # Curry function to remember key against which to store updated value
    def update(value):
        from . import store

        s = store.Store()
        s.UpdateValue(key, value)
        
        if signal_update_delegate != None: 
            signal_update_delegate()

    return update

def subscribe_to_service(service_name, state_name, signal_update_delegate):
    print ("Subscribing to service: {0}".format(service_name))
    callback = get_service_callback(state_name, signal_update_delegate)
    pydim.dic_info_service(service_name, callback)

def subscribe(signal_update_delegate):
    if not pydim.dis_get_dns_node():
        print("No Dim DNS node found. Please set the environment variable DIM_DNS_NODE")
        sys.exit(1)

    # Register listeners
    subscribe_to_service("trdbox/RUN_NUMBER", "runnumber", signal_update_delegate)
    subscribe_to_service("ztt_dimfed_server_trd-fee_00_2_0_STATE", "state", signal_update_delegate)
    subscribe_to_service("fee_00_2_0_STATE", "fee_state", signal_update_delegate)
