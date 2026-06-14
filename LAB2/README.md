# CST8919 - Lab 2

## Student Information

**Name:** Diniz Rodrigues Martins
**Student ID:** 041179475
**Course:** CST8919 - Cloud Industry Trends
**Lab:** Azure Monitor and KQL Alerting

---

# Lab Overview

In this lab, I deployed a Python web application to Azure App Service and configured Azure Monitor to collect and analyze application logs.

The main goal was to simulate brute-force login attempts, create Kusto Query Language (KQL) queries to detect suspicious activity, and configure Azure Alerts to automatically notify administrators when abnormal login behavior occurs.

---

# What I Learned

During this lab, I learned how to:

* Deploy a Python application to Azure App Service.
* Configure Azure Monitor and Log Analytics Workspace.
* Collect and inspect application logs.
* Create KQL queries for security monitoring.
* Configure Azure Alert Rules.
* Create Action Groups for email notifications.
* Trigger and validate alerts based on log data.

This lab provided practical experience with cloud monitoring and security event detection using Microsoft Azure services.

---

# Challenges Faced

Some of the challenges encountered during this lab included:

* Understanding the relationship between Azure Monitor, Log Analytics Workspace, and Alert Rules.
* Creating a KQL query that correctly aggregated failed login attempts.
* Configuring the alert threshold so that alerts would trigger consistently.
* Waiting for Azure Monitor to process and evaluate log data. (It scared me because it took a while to arrive.)

These challenges helped improve my understanding of cloud monitoring workflows and alerting mechanisms.

---

# Real-World Improvements

In a production environment, I would improve the detection logic by:

* Tracking failed login attempts per IP address.
* Monitoring failed logins per user account.
* Using dynamic thresholds instead of fixed values.
* Correlating failed logins with geographic locations.
* Integrating alerts with Microsoft Sentinel or a SIEM platform.
* Automatically blocking suspicious IP addresses using Azure automation.

These improvements would reduce false positives and provide more accurate threat detection.

---

# KQL Query Used

```kusto
AppServiceConsoleLogs
| where ResultDescription contains "FAILED LOGIN"
| summarize FailedAttempts = count() by bin(TimeGenerated, 5m)
| where FailedAttempts > 5
```

## Query Explanation

This query performs the following steps:

1. Searches application logs stored in AppServiceConsoleLogs.
2. Filters events containing the text "FAILED LOGIN".
3. Counts the number of failed login attempts within 5-minute intervals.
4. Returns only time periods where more than five failed login attempts occurred.

This logic helps identify potential brute-force login attacks.

---

# Alert Configuration

The alert rule was configured with:

* Signal Type: Custom Log Search
* Query Type: Aggregated Logs
* Threshold: Greater Than 5
* Evaluation Frequency: 1 Minute
* Action Group: Email Notification

When the threshold is exceeded, Azure Monitor automatically sends an email notification.

---

# Testing

The application was tested using a VS Code REST Client compatible file named:

```text
test-app.http
```

This file generates both successful and failed login requests, allowing the monitoring solution to detect brute-force patterns.

---

# YouTube Demonstration

Video Link:

https://youtu.be/Y51hMW76UnU


---

# Conclusion

This lab demonstrated how Azure Monitor and KQL can be used to build a simple but effective security monitoring solution. By combining log collection, query analysis, and automated alerting, organizations can quickly detect suspicious authentication activity and respond to potential security threats.
