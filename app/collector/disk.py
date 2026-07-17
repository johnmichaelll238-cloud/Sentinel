import psutil

def get_disk_metrics(

)->dict:
    disk = psutil.disk_usage("/")

    disk_percent = disk.percent
    disk_used = disk.used
    disk_free = disk.free
    
    return {
        "disk_percent" : disk_percent,
        "disk_used" : disk_used,
        "disk_free" : disk_free
    }