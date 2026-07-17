import psutil

def get_memory_metrics(

)->dict:
    memory = psutil.virtual_memory()
    memory_percent = memory.percent
    memory_used = memory.used
    memory_available = memory.available

    return {
    "memory_percent": memory_percent,
    "memory_used": memory_used,
    "memory_available": memory_available
    }
    