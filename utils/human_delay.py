import random
import time

def wait_random(min_sec=0.5, max_sec=2.5):
    """Случайная пауза между действиями"""
    time.sleep(random.uniform(min_sec, max_sec))
