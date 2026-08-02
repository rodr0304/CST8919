# Azure Policy Lab – MapleTech Secure Foundation

## Overview

This lab demonstrates how Azure Policy can be used to enforce governance and security standards across Azure resources.

A custom initiative named **MapleTech Secure Foundation** was created to group multiple custom policies and apply them to a Resource Group.

---

## Resource Group

- **Name:** MapleTech-RG

---

## Custom Policies

### 1. Only-CanadaCentral

**Purpose**

Restricts resource deployment to the **Canada Central** Azure region.

**Effect**

- Deny

---

### 2. Require-ProjectName-Tag

**Purpose**

Requires every deployed resource to contain the **ProjectName** tag.

**Effect**

- Deny

---

### 3. Deny-Public-IP

**Purpose**

Prevents the creation of Public IP resources.

**Effect**

- Deny

---

## Initiative

**Name**

MapleTech Secure Foundation

**Description**

Security baseline for MapleTech resources.

The initiative includes:

- Only-CanadaCentral
- Require-ProjectName-Tag
- Deny-Public-IP

---

## Assignment

The initiative was assigned to the following Resource Group:

- **MapleTech-RG**

This ensures every resource deployed inside the Resource Group must comply with all security policies.

---

## Validation

Several deployment attempts were performed to verify policy enforcement.

Examples include:

- Deploying resources outside Canada Central.
- Deploying resources without the required ProjectName tag.
- Deploying resources that require a Public IP.

Azure Policy successfully blocked non-compliant deployments.

---

## Result

The custom initiative successfully enforces organizational governance by:

- Restricting deployments to Canada Central.
- Requiring resource tagging.
- Preventing Public IP creation.

This provides a consistent security baseline for all resources inside the Resource Group.