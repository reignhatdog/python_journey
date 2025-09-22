#Stopwatch
import time

def main():
    print("Day 8: Stopwatch")
    input("Press Enter to start...")
    start = time.time()
    input("Press Enter to stop...")
    end = time.time()
    elapsed = round(end - start, 2)
    print(f"Elapsed time: {elapsed} seconds")

if __name__ == "__main__":
    main()
