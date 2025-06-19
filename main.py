import os
import platform
import time

def ping_host(ip):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = f"ping {param} 1 {ip} >nul 2>&1" if os.name == 'nt' else f"ping {param} 1 {ip} >/dev/null 2>&1"
    return os.system(command) == 0

def main():
    print("="*50)
    print("      HIGH-RATE PING TOOL (EDUCATIONAL)")
    print("="*50)

    ip = input("\nEnter IP or Hostname to ping: ")
    pings_per_second = float(input("How many pings per second? (e.g. 2, 5, 10): "))
    duration = int(input("Total duration in seconds: "))

    delay = 1 / pings_per_second
    total_pings = int(duration * pings_per_second)

    print(f"\nPinging {ip} at {pings_per_second}x/sec for {duration} sec ({total_pings} pings total)...\n")

    success = 0
    fail = 0

    start = time.time()
    try:
        for _ in range(total_pings):
            t = time.strftime("%H:%M:%S")
            if ping_host(ip):
                print(f"[{t}] {ip} is UP")
                success += 1
            else:
                print(f"[{t}] {ip} is DOWN")
                fail += 1
            time.sleep(delay)
    except KeyboardInterrupt:
        print("\n\nStopped by user.")
    finally:
        print("\nFinished.")
        print(f"Success: {success}")
        print(f"Failed:  {fail}")

if __name__ == "__main__":
    main()
