import sys
import time
import random
import string


secret_key = "qazplmwsxokndcijbrefvtghuy"
# Create the encryption table
cipher_table = str.maketrans(alphabet, secret_key)