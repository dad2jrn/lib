from __future__ import annotations

import os
import time, string, random
from multiprocessing import Pool

filename = "temp"
n = 100000
s = 8
random_text = "".join(random.choices(string.ascii_uppercase + string.digits, k = n))
random_name = "".join(random.choices(string.ascii_uppercase + string.digits, k = s))
# print(f"The randomly generated string is : {str(random_text)}") # print the random data

if __name__ == "__main__":
    count = 0
    while count < 500:
        for i in range(10):
            with open(f"files/{filename}{random_name}.txt", "w") as f:
                f.write(random_text)
        count =+ 1