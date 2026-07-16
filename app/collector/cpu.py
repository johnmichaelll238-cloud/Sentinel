import psutil

def get_cpu_metrics(

)->dict:
    #Take snapshot of CPU usage with psutil
    cpu_percent = psutil.cpu_percent(interval=1)

    #Create and return Dictionary containing cpu_usage
    cpu_dict = {"cpu_percent" : cpu_percent}
    
    return cpu_dict
    