import requests
import time
import random

if __name__ == '__main__':

    while True:
        r_per_batch = random.randint(250, 400)
        sleep_time = random.uniform(0.1, 1.9)
        print(f"Making {r_per_batch} requests after {sleep_time} seconds")
        for i in range(r_per_batch):
            r = requests.get('http://172.40.0.10:5000/labels')
        time.sleep(sleep_time)

