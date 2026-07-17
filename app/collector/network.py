import psutil

def get_network_metrics(

)->dict:
    network = psutil.net_io_counters()

    return {
        "bytes_sent" : network.bytes_sent,
        "bytes_received" : network.bytes_recv
    }
    