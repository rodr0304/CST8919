# Assignment 1 - Securing and Monitoring an Authenticated Flask App

---
YouTube: https://youtu.be/3LJkIYu9Yx8
---

## Overview

This project demonstrates how to secure and monitor a Flask web application using Auth0 and Microsoft Azure.

The application authenticates users through Auth0, logs user activity, stores logs in Azure Monitor, and automatically generates alerts when suspicious behavior is detected.

---

# Technologies

- Python 3
- Flask
- Auth0
- Azure App Service
- Azure Monitor
- Azure Log Analytics
- Kusto Query Language (KQL)

---

# Project Structure

```
Assignment1/
│
├── server.py
├── requirements.txt
├── .env.example
├── test-app.http
├── README.md
```

---

# Setup

## 1. Clone the repository

```bash
git clone <repository-url>
cd Assignment1
```

---

## 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Auth0

Create a `.env` file based on `.env.example`.

Required variables:

```text
AUTH0_DOMAIN=xxx
AUTH0_CLIENT_ID=xxx
AUTH0_CLIENT_SECRET=xxx
AUTH0_SECRET=xxx
APP_BASE_URL=https://xxx
```

Configure the following settings in Auth0:

### Allowed Callback URLs

```
https://xxx.azurewebsites.net/callback
```

### Allowed Logout URLs

```
https://xxx.azurewebsites.net
```

### Allowed Web Origins

```
https://xxx.azurewebsites.net
```

---

# Azure Deployment

The application is deployed to Azure App Service.

Azure Diagnostic Settings were configured to send logs to Azure Log Analytics.

Enabled log categories:

- App Service Console Logs
- App Service Application Logs
- HTTP Logs

---

# Logging

The application records the following events:

- Successful login
- Access to the `/protected` endpoint
- Unauthorized access attempts

Example log:

```json
{
  "event": "protected_access",
  "user_id": "google-oauth2|xxxxxxxx",
  "email": "user@email.com",
  "route": "/protected"
}
```

---

# Detection Logic

The following KQL query identifies users who access the protected endpoint more than **10 times within 15 minutes**.

```kusto
AppServiceConsoleLogs
| where ResultDescription contains "protected_access"
| extend UserId = extract('"user_id":"([^"]+)"', 1, ResultDescription)
| extend Email = extract('"email":"([^"]+)"', 1, ResultDescription)
| summarize
    AccessCount = count(),
    Timestamp = max(TimeGenerated)
by UserId, Email
| where AccessCount > 10
| project UserId, Email, Timestamp, AccessCount
| order by AccessCount desc
```

---

# Azure Alert

An Azure Monitor Alert Rule was configured with the following settings:

- Signal: Custom Log Search
- Query: KQL query above
- Threshold: More than 10 accesses
- Evaluation Frequency: Every 5 minutes
- Severity: 3 (Low)
- Notification: Email using an Azure Action Group

---

# Running the Application

```bash
python3 server.py
```

Open the application:

```
http://127.0.0.1:5000
```

---

# Test File

The project includes a simple HTTP request collection:

```
test-app.http
```

---

# Demo Video

The demonstration includes:

- Auth0 authentication
- Azure App Service deployment
- Login logging
- Protected route logging
- Azure Monitor logs
- KQL query execution
- Azure Alert Rule
- Alert email notification

---

# Reflection

This project demonstrates how identity management, monitoring, and alerting can be integrated into a cloud application. Using Auth0 together with Azure Monitor enables secure authentication, centralized logging, and automated detection of suspicious user activity.
