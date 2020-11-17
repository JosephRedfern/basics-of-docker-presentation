import numpy as np
import socket
import os

random_numbers = np.random.random((20,2))
hostname = socket.gethostname()
cwd = os.getcwd()

print(f"Hostname of system is: {hostname}")
print(f"Current working directory is: {cwd}")
print(f"Here are some random numbers: \n{random_numbers}")
