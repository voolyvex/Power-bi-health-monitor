import psutil
import requests
import time
import json
from datetime import datetime

# =================================================================
# CONFIGURATION
# Paste your Power BI Streaming Dataset "Push URL" here
# =================================================================
PUSH_URL = "YOUR_POWER_BI_PUSH_URL_HERE"

def get_system_metrics():
    """
    Captures local system metrics using psutil.
    """
    metrics = {
        "Timestamp": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
        "CPU_Usage": psutil.cpu_percent(interval=1),
        "RAM_Usage": psutil.virtual_memory().percent,
        "Disk_Usage": psutil.disk_usage('/').percent
    }
    return metrics

def push_to_power_bi(data):
    """
    Sends the metrics JSON to the Power BI REST API endpoint.
    """
    if PUSH_URL == "YOUR_POWER_BI_PUSH_URL_HERE":
        print("[!] Error: Please paste your Power BI Push URL into the script.")
        return False

    try:
        # Power BI expects an array of objects
        response = requests.post(PUSH_URL, data=json.dumps([data]))
        if response.status_code == 200:
            print(f"[+] Successfully pushed metrics at {data['Timestamp']}")
            return True
        else:
            print(f"[-] Failed to push data. Status Code: {response.status_code}")
            print(f"[-] Response: {response.text}")
            return False
    except Exception as e:
        print(f"[!] API Connection Error: {e}")
        return False

def main():
    print("--- Power BI Real-Time System Health Monitor ---")
    print(f"Pushing to: {PUSH_URL[:30]}...")
    print("Press Ctrl+C to stop.")
    
    try:
        while True:
            metrics = get_system_metrics()
            push_to_power_bi(metrics)
            time.sleep(5)  # Collect data every 5 seconds
    except KeyboardInterrupt:
        print("\n[!] Monitor stopped by user.")

if __name__ == "__main__":
    main()
