import os, psutil, datetime
from app import app

@app.route('/')
@app.route('/metrics')
def index():
    memmory = get_memory()
    cpu = get_cpu()
    uptime = get_boot_time()
    metrics = {"memory": memmory, "cpu" : cpu, "uptime" : uptime} 
    return metrics
    
def get_memory():
    memory_raw = psutil.virtual_memory()
    memory = { "total" : memory_raw[0], "available" : memory_raw[1],"used" : memory_raw[3], "used_percent" : memory_raw[2]}

    return memory

def get_cpu():
    cpu_raw = psutil.cpu_count()
    cpu = {"total_cores" : cpu_raw}
    return cpu

def get_boot_time():
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    uptime = {"uptime" : today, "boot_time" : boot_time}
    return uptime