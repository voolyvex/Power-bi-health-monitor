# Power BI Real-Time System Health Monitor

A Python-based system monitoring solution that integrates with Power BI to provide real-time infrastructure health visibility through REST API streaming.

## Overview

This project captures local system metrics (CPU, RAM, Disk) and pushes them to a Power BI Streaming Dataset via REST API, enabling live dashboard updates without manual refreshes.

## Prerequisites

- Python 3.x
- Required libraries: `psutil`, `requests`
- Power BI Pro account (or trial)

## Setup Instructions

### 1. Create the Streaming Dataset in Power BI

1. Log in to [app.powerbi.com](https://app.powerbi.com)
2. Navigate to **My Workspace** > **+ New** > **Streaming dataset**
3. Select **API** and click **Next**
4. Name the dataset `SystemHealthMonitor`
5. Define the following fields (case-sensitive):
   - `Timestamp` (DateTime)
   - `CPU_Usage` (Number)
   - `RAM_Usage` (Number)
   - `Disk_Usage` (Number)
6. Enable **Historic data analysis**
7. Click **Create** and copy the Push URL

### 2. Configure the Python Script

1. Open `system_monitor.py`
2. Replace `YOUR_POWER_BI_PUSH_URL_HERE` with your Push URL
3. Install dependencies: `pip install psutil requests`

### 3. Run the Monitor

```bash
python system_monitor.py
```

## Key Technical Capabilities

- **Automation**: Automated telemetry collection eliminates manual monitoring overhead
- **API Integration**: Demonstrates REST API proficiency bridging local infrastructure with cloud BI platforms
- **User Enablement**: Provides non-technical stakeholders with accessible system health visibility
- **Scalability**: Architecture supports enterprise-scale deployment using centralized logging servers or message brokers (e.g., Kafka)

## Troubleshooting

- **API Errors**: Verify Push URL accuracy and network connectivity
- **Missing Dependencies**: Install required libraries with `pip install psutil requests`
- **Schema Errors**: Ensure field names in the script exactly match the dataset definition
