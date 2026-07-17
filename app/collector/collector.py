from datetime import datetime

#import results from individual collectors
from app.collector.cpu import get_cpu_metrics
from app.collector.memory import get_memory_metrics
from app.collector.disk import get_disk_metrics
from app.collector.network import get_network_metrics 

 #import database insert function
from app.storage.database import insert_metrics


def collect_metrics(

)->dict:    
    cpu = get_cpu_metrics()
    memory = get_memory_metrics()
    disk = get_disk_metrics()
    network = get_network_metrics()

    metrics = {
    "timestamp": datetime.now().isoformat()
    }

    metrics.update(cpu)
    metrics.update(memory)
    metrics.update(disk)
    metrics.update(network)

    insert_metrics(metrics)

    return metrics
    
