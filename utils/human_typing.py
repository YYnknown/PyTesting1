import time
import random

def slow_typing(element, text, delay_range=(0.1, 0.25)):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(*delay_range))
