# Power BI Real-Time System Health Monitor

This project demonstrates how a Systems Engineer can integrate Python automation with Power BI to provide real-time enterprise visibility into infrastructure health.

## 🚀 Overview
The project captures local system metrics (CPU, RAM, Disk) using Python and pushes them directly to a **Power BI Streaming Dataset** via a REST API endpoint. This enables a live dashboard that updates without manual refreshes.

## 🛠️ Prerequisites
- Python 3.x
- `psutil` library: `pip install psutil`
- `requests` library: `pip install requests`
- Power BI Pro account (or trial)

## 📋 Setup Instructions

### 1. Create the Streaming Dataset in Power BI
1. Log in to [app.powerbi.com](https://app.powerbi.com).
2. Go to **My Workspace** > **+ New** > **Streaming dataset**.
3. Select **API** and click **Next**.
4. Name the dataset `SystemHealthMonitor`.
5. Define the following fields (Case Sensitive):
   - `Timestamp` (DateTime)
   - `CPU_Usage` (Number)
   - `RAM_Usage` (Number)
   - `Disk_Usage` (Number)
6. **Enable "Historic data analysis"** (Crucial for trend charts).
7. Click **Create** and **Copy the Push URL**.

### 2. Configure the Python Script
1. Open `system_monitor.py`.
2. Replace `YOUR_POWER_BI_PUSH_URL_HERE` with the URL you copied.
3. Save the file.

### 3. Run the Monitor
```bash
python system_monitor.py
```

## 📊 Interview Talking Points (Systems Engineer Context)
- **Automation over Manual Checks:** "Instead of checking server health manually, I developed a script to automate telemetry collection."
- **API Integration:** "Demonstrates proficiency in using REST APIs to bridge the gap between local infrastructure and cloud BI platforms."
- **User Enablement:** "By surfacing real-time metrics in Power BI, I enable non-technical stakeholders to monitor system health without needing terminal access."
- **Scalability & Security:** "This pattern can be scaled to monitor thousands of endpoints by using a centralized logging server or a message broker like Kafka before hitting the Power BI API."

## 🔧 Troubleshooting
- **API Errors:** Ensure the Push URL is correct and your internet connection is stable.
- **Library Missing:** Run `pip install psutil requests`.
- **Formatting:** Power BI is strict about JSON schema. Ensure the field names in the script exactly match the dataset definition.
