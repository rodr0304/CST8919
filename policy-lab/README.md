# Cloud Governance Gone Rogue – Azure Policy Lab

**Course:** CST8919 – DevOps Security and Compliance

## Lab Summary

This lab demonstrates how Azure Policy can be used to enforce governance, security, and compliance within Azure.

The following custom Azure Policies were created:

- Only-CanadaCentral
- Require-ProjectName-Tag
- Deny-Public-IP

These policies were grouped into the **MapleTech Secure Foundation** Initiative and assigned to the **MapleTech-RG** Resource Group using **Enforcement Mode = Deny**.

---

# Policy Definitions

## 1. Only-CanadaCentral

- Effect: Deny
- Purpose:
  Prevents resources from being deployed outside Canada Central.

---

## 2. Require-ProjectName-Tag

- Effect: Deny
- Purpose:
  Requires every deployed resource to contain the tag:

```
ProjectName
```

---

## 3. Deny-Public-IP

- Effect: Deny

Purpose:

Blocks creation of Public IP Address resources.

---

# Initiative

**Name**

```
MapleTech Secure Foundation
```

Category

```
Security
```

Policies included

- Only-CanadaCentral
- Require-ProjectName-Tag
- Deny-Public-IP

---

# Assignment

The initiative was assigned to:

```
MapleTech-RG
```

Enforcement Mode

```
Deny
```

---

# Testing

The following deployment scenarios were tested.

| Test | Result |
|-------|--------|
| VM outside Canada Central | Blocked |
| Storage Account without ProjectName tag | Deployment blocked before custom policy evaluation |
| Public IP Address | Deployment blocked before custom policy evaluation |
| Storage Account in Mexico Central | Successfully deployed |

---

# Investigation

Additional troubleshooting was performed using Azure Cloud Shell and Azure CLI.

The following commands were executed:

```bash
az policy assignment list
```

```bash
az policy assignment show
```

```bash
az storage account create
```

```bash
az network public-ip create
```

```bash
az rest
```

The investigation confirmed that the Azure for Students subscription already contains a Microsoft System Policy named:

```
Allowed resource deployment regions
```

The policy assignment is:

```
sys.regionrestriction
```

The allowed locations configured by Microsoft are:

```
eastus
eastus2
westus3
mexicocentral
northcentralus
```

During deployment testing, Azure returned the following error:

```text
RequestDisallowedByAzure

Resource 'saca2081322134' was disallowed by Azure:

This policy maintains a set of best available regions where your subscription can deploy resources.

Should you need additional or different regions, contact support.
```

The same error was returned when attempting to create:

- Storage Account
- Public IP Address

inside Canada Central.

However, the exact same Storage Account deployment succeeded when using:

```
Mexico Central
```

with the same parameters and required ProjectName tag.

This demonstrates that the deployment restriction originated from an existing Microsoft subscription policy rather than from the custom policies created for this lab.

---

# Challenges

The Azure for Students subscription contains a built-in Microsoft Policy that restricts deployments for specific Azure resources.

Because this policy is enforced before the custom initiative is evaluated, some deployment scenarios requested in the lab (such as creating resources in Canada Central) could not be fully validated despite the custom policies being successfully created, assigned, and enforced.

---

# Lessons Learned

This lab provided practical experience with:

- Creating Custom Azure Policies
- Azure Policy Definitions
- Policy Initiatives
- Policy Assignments
- Azure Governance
- Compliance
- Azure CLI troubleshooting
- Azure Policy evaluation order
- Difference between custom policies and Microsoft built-in policies

---

# Repository Structure

```
policy-lab/
│
├── README.md
├── screenshots/
├── policy-definitions/
│   ├── Only-CanadaCentral.json
│   ├── Require-ProjectName-Tag.json
│   └── Deny-Public-IP.json
│
└── video-link.txt
```

---

# Video

Video demonstration:

```
[<Insert YouTube or OneDrive link here>
](https://youtu.be/L1ZWARfxu78)```
