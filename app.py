import os
import socket

#data_dir = "/Users/sushmakumbham/Desktop/python1"
data_dir="/app"
output_file="/app/result.txt"
#output_file = "/Users/sushmakumbham/Desktop/python1/result.txt"

def list_files():
    files = os.listdir(data_dir)
    with open(output_file, "a") as f:
        f.write("List of files:\n")
        for file in files:
            f.write(f"{file}\n")

def count_words():
    if_file = os.path.join(data_dir, "IF.txt")
    limerick_file = os.path.join(data_dir, "Limerick.txt")
    with open(if_file, "r") as f:
        if_count = len(f.read().split())
    with open(limerick_file, "r") as f:
        limerick_count = len(f.read().split())
    with open(output_file, "a") as f:
        f.write(f"Number of words in IF.txt: {if_count}\n")
        f.write(f"Number of words in Limerick.txt: {limerick_count}\n")
        f.write(f"Grand total: {if_count + limerick_count}\n")

def top_words():
    if_file = os.path.join(data_dir, "IF.txt")
    with open(if_file, "r") as f:
        words = f.read().split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], 
reverse=True)
    with open(output_file, "a") as f:
        f.write("Top 3 words in IF.txt:\n")
        for word, count in sorted_word_counts[:3]:
            f.write(f"{word}: {count}\n")

def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    with open(output_file, "a") as f:
        f.write(f"IP address of the machine: {ip_address}\n")

list_files()
count_words()
top_words()
get_ip()

