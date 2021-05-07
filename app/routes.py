import os, psutil
from app import app

@app.route('/')
@app.route('/metrics')
def index():
    memmory = get_mommory()
    metrics = {"memmory": memmory}
    return metrics
    
def get_mommory():
    process = psutil.Process(os.getpid())
    total_memmory = process.memory_info().rss
    return total_memmory