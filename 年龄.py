import hashlib
import platform
import psutil
import subprocess
import random
import time
import os

# 定义一些无意义的函数
def calculate_something():
    x = 42
    y = "Hello, world!"
    z = x * len(y)
    print(f"Calculation result: {z}")
    return z

def loop_through_numbers():
    for i in range(10):
        print("Looping through numbers!", end=" ")
    print()
    return "Loop done!"

def concatenate_lists():
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = a + b
    print(f"Concatenated lists: {c}")
    return c

def call_functions():
    loop_through_numbers()
    return concatenate_lists()

def print_message():
    return "I am just printing a message!"

def concatenate_strings():
    x = "useless"
    y = "function"
    z = x + y
    print(f"Concatenated strings: {z}")
    return z

def take_up_space():
    print("This function is just here to take up space.")
    return None

def another_calculation():
    x = 100
    y = 200
    z = x + y
    print(f"Another calculation: {z}")
    return z

def calculate_hash():
    data = "This is some random data"
    hash_object = hashlib.sha256(data.encode())
    hash_hex = hash_object.hexdigest()
    print(f"Calculated hash: {hash_hex}")
    return hash_hex

def calculate_more_hashes():
    data = "Another piece of random data"
    hash_object = hashlib.sha256(data.encode())
    hash_hex = hash_object.hexdigest()
    print(f"Another calculated hash: {hash_hex}")
    return hash_hex

def compare_numbers():
    a = 42
    b = 24
    if a > b:
        print(f"{a} is greater than {b}.")
    else:
        print(f"{b} is greater than {a}.")
    return None

def compare_more_numbers():
    c = 100
    d = 200
    if c < d:
        print(f"{c} is less than {d}.")
    else:
        print(f"{d} is less than {c}.")
    return None

def get_system_info():
    system_info = {
        "platform": platform.system(),
        "platform_version": platform.version(),
        "platform_release": platform.release(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
        "cpu_count": psutil.cpu_count(),
        "cpu_freq": psutil.cpu_freq(),
        "memory_info": psutil.virtual_memory(),
        "disk_info": psutil.disk_usage('/'),
        "network_info": psutil.net_if_addrs()
    }
    return system_info

def get_gpu_info():
    try:
        if platform.system() == "Windows":
            gpu_info = subprocess.check_output("wmic path win32_videocontroller get name", shell=True).decode()
        elif platform.system() == "Linux":
            gpu_info = subprocess.check_output("lspci | grep -i nvidia", shell=True).decode()
        elif platform.system() == "Darwin":
            gpu_info = subprocess.check_output("system_profiler SPDisplaysDataType", shell=True).decode()
        else:
            gpu_info = "Unknown GPU"
    except Exception as e:
        gpu_info = f"Error getting GPU info: {e}"
    return gpu_info

def generate_random_data():
    random_data = [random.randint(1, 100) for _ in range(10)]
    print(f"Random data: {random_data}")
    return random_data

def simulate_long_running_task():
    print("Starting a long-running task...")
    time.sleep(2)
    print("Task completed!")
    return None

def manipulate_strings():
    s = "This is a useless string"
    reversed_s = s[::-1]
    upper_s = s.upper()
    lower_s = s.lower()
    print(f"Reversed string: {reversed_s}")
    print(f"Uppercase string: {upper_s}")
    print(f"Lowercase string: {lower_s}")
    return None

def perform_useless_math():
    a = 10
    b = 5
    c = a * b
    d = a / b
    e = a + b
    f = a - b
    print(f"Useless math results: {c}, {d}, {e}, {f}")
    return None

def manipulate_lists():
    lst = [1, 2, 3, 4, 5]
    lst.append(6)
    lst.pop(0)
    lst.reverse()
    lst.sort()
    print(f"Manipulated list: {lst}")
    return None

def manipulate_dicts():
    d = {"key1": "value1", "key2": "value2"}
    d["key3"] = "value3"
    del d["key1"]
    print(f"Manipulated dictionary: {d}")
    return None

def manipulate_sets():
    s = {1, 2, 3, 4, 5}
    s.add(6)
    s.remove(1)
    print(f"Manipulated set: {s}")
    return None

def manipulate_tuples():
    t = (1, 2, 3, 4, 5)
    print(f"Tuple element: {t[2]}")
    return None

def manipulate_files():
    try:
        with open("useless_file.txt", "w") as f:
            f.write("This is a useless file.")
        with open("useless_file.txt", "r") as f:
            content = f.read()
            print(f"File content: {content}")
    except Exception as e:
        print(f"Error manipulating files: {e}")
    return None

def handle_exceptions():
    try:
        x = 1 / 0
    except ZeroDivisionError as e:
        print(f"Caught an exception: {e}")
    return None

def manipulate_environment():
    os.environ["USELESS_VAR"] = "useless_value"
    print(f"Environment variable USELESS_VAR set to {os.environ['USELESS_VAR']}")
    return None

def simulate_network_request():
    try:
        print("Simulating a network request...")
        time.sleep(1)
        print("Network request completed!")
    except Exception as e:
        print(f"Error simulating network request: {e}")
    return None

def simulate_multithreading():
    import threading
    def thread_function():
        print("Thread is running...")
        time.sleep(1)
        print("Thread completed!")
    thread = threading.Thread(target=thread_function)
    thread.start()
    thread.join()
    return None

def useless_loop():
    for i in range(100):
        print(f"Useless loop iteration: {i}")
    return None

def useless_recursive_function(n):
    if n <= 0:
        print("Recursive function ended.")
        return
    print(f"Recursive call {n}")
    useless_recursive_function(n - 1)

# 主程序
while True:
    age = input("请输入你的年龄（数字哦）：")

    if age.isdigit():
        age = int(age)
        if age in [114, 1145, 114514, 514, 1919810, 11451, 1145141919810]:
            print("这个年龄不能要了！")
        elif age == 321:
            print("看！煤气灶！！！")
        elif age < 1:
            print("哇哦，你还没出生呢！穿越者？")
        elif age < 10:
            print(f"哇，你才{age}岁啊，真是个可爱的小宝宝！")
        elif age < 20:
            print(f"哟，{age}岁，青春无敌啊！")
        elif age < 30:
            print(f"哇，{age}岁，正是风华正茂的时候！")
        elif age < 50:
            print(f"哎呀，{age}岁，人生经验满满，是不是觉得自己越来越成熟了？")
        elif age < 70:
            print(f"哇，{age}岁，真是人生阅历丰富啊，是不是觉得自己越来越有智慧了？")
        elif age < 100:
            print(f"哇塞，{age}岁！您是传说中的老寿星吧？")
        elif age < 150:
            print(f"哇哦，{age}岁！您是不老的传说吗？")
        else:
            print(f"你是在开玩笑吗(=°Д°=)！{age}岁不可能吧？")
    else:
        print("你输入的不是数字哦，我猜你是个秘密特工，年龄保密吧！")
