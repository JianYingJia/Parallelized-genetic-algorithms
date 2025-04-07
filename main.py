import time
from algorithms.genetic_algorithm import run_parallel_ga
from algorithms.serial_ga import genetic_algorithm_serial

if __name__ == "__main__":
    print("Choose mode: (1) Serial  (2) Parallel")
    mode = input("Enter 1 or 2: ").strip()
    if mode == "1":  
        genetic_algorithm_serial()
    elif mode == "2":
        run_parallel_ga()
    else:
        print("Invalid mode.")
