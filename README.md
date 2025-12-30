# Power BI Real-Time System Health Monitor

Python script that captures system metrics (CPU, RAM, Disk) and streams them to Power BI via REST API for real-time dashboard visualization.

## Prerequisites

- Python 3.x
- `pip install psutil requests`
- Power BI Pro account

## Setup

1. Create Streaming Dataset in Power BI:
   - Go to **My Workspace** > **+ New** > **Streaming dataset** > **API**
   - Name: `SystemHealthMonitor`
   - Fields: `Timestamp` (DateTime), `CPU_Usage` (Number), `RAM_Usage` (Number), `Disk_Usage` (Number)
   - Enable **Historic data analysis**
   - Copy the Push URL

2. Configure `system_monitor.py`:
   - Replace `YOUR_POWER_BI_PUSH_URL_HERE` with your Push URL

3. Run:
   ```bash
   python system_monitor.py
   ```

## Features

- Automated metric collection via Python
- REST API integration with Power BI
- Real-time dashboard updates (5-second intervals)
- Scalable architecture for enterprise deployment

## Example Dashboard Visualization

<img src="example_visuals.png" alt="Power BI Dashboard Example" width="800">