# CST8919 – DevOps Security and Compliance

## Assignment 2 – Cloud Service Alternatives Report

**Student:** Diniz Rodrigues Martins  
**Email:** rodr0304@algonquinlive.com  
**Course:** CST8919 – DevOps Security and Compliance  
**Assignment:** Assignment 2 – Cloud Service Alternatives Report  
**Date:** August 2026

---

## Introduction

Cloud providers offer different services for security, monitoring, identity management, and compliance. In this report, I will compare Microsoft Azure services used during the CST8919 course with similar services available in Amazon Web Services (AWS) and Google Cloud Platform (GCP).

The comparison will focus on the main features, security and compliance capabilities, pricing models, and DevSecOps integration of each service.

The Azure services covered in this report are:

* Microsoft Entra ID (Azure Active Directory)
* Azure Policy
* Azure Key Vault
* Azure Network Security Groups (NSG)
* Azure DDoS Protection
* Azure Web Application Firewall (WAF)
* Azure Monitor and Log Analytics
* Microsoft Defender for Cloud
* Microsoft Sentinel

---

# Cloud Service Equivalents

Azure, AWS, and Google Cloud provide many similar security services. However, these services are not always exactly the same. Sometimes one Azure service can have two or more services with similar functions in AWS or GCP.

The table below shows the closest AWS and GCP equivalents for the Azure services covered in this report.

| Security Area | Microsoft Azure | Amazon Web Services (AWS) | Google Cloud Platform (GCP) |
|---|---|---|---|
| Identity and Access Management | Microsoft Entra ID | AWS IAM / IAM Identity Center | Cloud IAM / Cloud Identity |
| Governance and Compliance | Azure Policy | AWS Config / Service Control Policies (SCPs) | Organization Policy Service |
| Secrets and Key Management | Azure Key Vault | AWS Secrets Manager / AWS KMS | Secret Manager / Cloud KMS |
| Network Access Control | Azure Network Security Groups (NSG) | AWS Security Groups | VPC Firewall Rules |
| DDoS Protection | Azure DDoS Protection | AWS Shield | Google Cloud Armor |
| Web Application Security | Azure Web Application Firewall (WAF) | AWS WAF | Google Cloud Armor |
| Monitoring and Logging | Azure Monitor and Log Analytics | Amazon CloudWatch | Cloud Monitoring / Cloud Logging |
| Cloud Security | Microsoft Defender for Cloud | AWS Security Hub / Amazon GuardDuty | Security Command Center |
| SIEM and SOAR | Microsoft Sentinel | Amazon Security Lake / AWS Security Services | Google Security Operations |

---

## General Analysis

After comparing these services, I noticed that Azure, AWS, and Google Cloud provide similar security solutions, but they organize their services in different ways.

For identity and access management, Microsoft Entra ID, AWS IAM, and Google Cloud IAM help control access to cloud resources. They define who can access resources and what actions users are allowed to perform.

For governance and compliance, Azure Policy can create rules for Azure resources. AWS provides similar capabilities with AWS Config and Service Control Policies, while Google Cloud uses Organization Policy Service.

For secrets and keys, Azure Key Vault can protect passwords, secrets, certificates, and encryption keys. AWS uses services such as Secrets Manager and KMS, while Google Cloud provides Secret Manager and Cloud KMS.

For network security, Azure Network Security Groups, AWS Security Groups, and Google Cloud VPC Firewall Rules can control network traffic.

For DDoS protection, Azure provides Azure DDoS Protection and AWS provides AWS Shield. Google Cloud Armor also provides DDoS protection.

For web application security, Azure provides Web Application Firewall (WAF), while AWS provides AWS WAF. Google Cloud Armor also provides Web Application Firewall capabilities.

Monitoring and logging are important for cloud security. Azure Monitor and Log Analytics collect and analyze information from Azure resources. Amazon CloudWatch provides similar monitoring capabilities in AWS, while Google Cloud uses Cloud Monitoring and Cloud Logging.

Microsoft Defender for Cloud provides security posture management and workload protection. AWS uses multiple services for similar functions, including AWS Security Hub and Amazon GuardDuty. Google Cloud provides Security Command Center.

Microsoft Sentinel is a SIEM and SOAR platform. Google Security Operations provides similar security operations capabilities. AWS uses a more distributed approach with Amazon Security Lake and other AWS security services.

In my opinion, there is no single cloud provider that is the best for every company. The best option depends on the company's infrastructure, security requirements, budget, and technologies already being used.

---

# 1. Identity and Access Management

## Overview

### Microsoft Azure – Microsoft Entra ID

Microsoft Entra ID, previously called Azure Active Directory, is Microsoft's cloud identity and access management service. It helps organizations manage users, groups, applications, and access to cloud resources.

It also supports security features such as Single Sign-On (SSO), Multi-Factor Authentication (MFA), and Conditional Access.

### AWS – AWS IAM and IAM Identity Center

AWS Identity and Access Management (IAM) controls access to AWS resources using users, groups, roles, permissions, and policies.

AWS IAM Identity Center provides centralized access management and Single Sign-On for multiple AWS accounts and applications.

### Google Cloud – Cloud IAM and Cloud Identity

Google Cloud IAM controls who can access Google Cloud resources and what actions they can perform.

Cloud Identity provides identity management features such as user accounts, groups, Single Sign-On, and Multi-Factor Authentication.

---

## Core Features

| Feature | Microsoft Azure | AWS | Google Cloud |
|---|---|---|---|
| Identity Management | Microsoft Entra ID | AWS IAM | Cloud IAM |
| Single Sign-On (SSO) | Yes | IAM Identity Center | Cloud Identity |
| Multi-Factor Authentication (MFA) | Yes | Yes | Yes |
| Users and Groups | Yes | Yes | Yes |
| Roles and Permissions | Yes | Yes | Yes |
| Context-Based Access Controls | Conditional Access | IAM policies and related access controls | Context-Aware Access |

---

## Security & Compliance

All three cloud providers provide security controls to protect identities and access to cloud resources.

They support features such as MFA, roles, permissions, security policies, and centralized identity management.

Microsoft Entra ID provides Conditional Access. It can apply access rules based on information such as the user, device, location, application, or sign-in risk.

AWS IAM uses policies and roles to define what users and applications are allowed to do inside AWS.

Google Cloud IAM uses roles and permissions to control access to Google Cloud resources.

These controls support the principle of least privilege. This means users should receive only the permissions they need to perform their work.

The cloud providers also maintain compliance programs for standards and regulations such as ISO 27001, SOC reports, and PCI DSS. The exact certifications depend on the service and region.

---

## MFA and Password Security

Passwords are still an important part of identity security, but a strong password alone is not enough to protect an account.

Multi-Factor Authentication (MFA) adds another layer of security. It requires the user to provide more than one form of authentication. For example, a user may enter a password and then confirm the login using an authentication application.

Azure, AWS, and Google Cloud all support MFA. This is important because even if an attacker discovers or steals a user's password, the attacker may still be unable to access the account without another authentication factor.

Strong passwords should also be used together with good identity practices. Users should avoid simple or reused passwords. Organizations should also control access based on the user's role and responsibilities.

In my opinion, MFA is one of the most important security controls for user accounts because passwords can be compromised. Using MFA together with good password practices can reduce the risk of unauthorized access.

---

## Pricing Model

Microsoft Entra ID provides different licensing options. Basic capabilities are available without an additional Entra ID license in some scenarios, while advanced identity and security features are available through paid plans.

AWS IAM does not have an additional charge for basic IAM usage. Other AWS identity services or resources used with IAM can have costs.

Google Cloud IAM does not charge for the use of the IAM API. Some related identity products and advanced features can have separate pricing.

---

## DevSecOps Integration

Identity management is important in DevSecOps because developers, applications, and CI/CD pipelines need secure access to cloud resources.

Microsoft Entra ID can provide identities and access control for Azure resources and can integrate with development and automation tools.

AWS IAM can provide roles and temporary credentials for applications, developers, and CI/CD pipelines.

Google Cloud IAM can provide roles, service accounts, and workload identities for applications and automated deployments.

MFA is also important for human accounts that can access source code, CI/CD systems, cloud resources, or production environments.

For automated systems, applications and CI/CD pipelines should use secure machine identities, roles, or short-lived credentials instead of personal passwords.

---

## Analysis

The three platforms provide strong identity and access management solutions, but they organize their services differently.

Microsoft Entra ID has strong integration with Microsoft products and provides features such as SSO, MFA, and Conditional Access.

AWS IAM provides detailed access control using policies and roles, while IAM Identity Center provides centralized access and SSO.

Google Cloud IAM uses roles and permissions to control access, while Cloud Identity provides additional identity management capabilities.

In my opinion, the best option depends on the environment already used by the company. A company that uses Microsoft 365 and Azure may find Microsoft Entra ID easier to integrate. A company mainly using AWS or Google Cloud may prefer the native identity services from those platforms.

However, independently of the cloud provider, I believe that MFA, strong identity controls, and the principle of least privilege are very important because identity is one of the first security layers used to protect cloud resources.

---

# 2. Governance and Compliance

## Overview

### Microsoft Azure – Azure Policy

Azure Policy helps organizations create and enforce rules for Azure resources.

### AWS – AWS Config and Service Control Policies

AWS Config records resource configurations and can evaluate resources for compliance.

Service Control Policies (SCPs), which are part of AWS Organizations, can define permission limits for accounts inside an AWS organization.

### Google Cloud – Organization Policy Service

Google Cloud Organization Policy Service allows administrators to create centralized rules and restrictions for Google Cloud resources.

---

## Core Features

| Feature | Microsoft Azure | AWS | Google Cloud |
|---|---|---|---|
| Policy Enforcement | Azure Policy | SCPs / AWS Config Rules | Organization Policy |
| Compliance Evaluation | Yes | AWS Config | Yes |
| Centralized Governance | Yes | AWS Organizations | Yes |
| Resource Restrictions | Yes | Yes | Yes |
| Automation Support | Yes | Yes | Yes |

---

## Security & Compliance

These services can help companies follow internal security requirements and external compliance requirements.

They can identify or prevent resources that do not follow company policies.

For example, an organization can create policies that restrict resource locations, require specific configurations, or prevent resources that do not follow security requirements.

Cloud providers also provide tools and compliance programs that can support standards such as ISO 27001, SOC, and PCI DSS.

These services are not exactly the same, but they have a similar goal: helping organizations apply governance rules and keep cloud resources compliant.

---

## Pricing Model

Azure Policy is available to Azure subscribers at no additional cost. Other Azure services used with policies can have their own costs.

AWS Config is usage-based. Costs can depend on configuration items, rule evaluations, and conformance pack evaluations. Service Control Policies are part of AWS Organizations.

Google Cloud does not charge for use of the Organization Policy Service API. Other Google Cloud services controlled by these policies can have their own costs.

---

## DevSecOps Integration

Policies can be used with Infrastructure as Code and automated deployments.

This can prevent developers from deploying resources that do not follow security requirements.

For example, a company can create a policy that prevents the creation of resources in an unauthorized region.

Policy checks can also become part of automated cloud governance.

---

## Analysis

The objective is similar in all three platforms. They help companies control how cloud resources are created and configured.

The implementation is different. Azure uses Azure Policy, AWS combines services such as AWS Config and Organizations, and Google Cloud uses Organization Policy.

This is important for DevSecOps because security rules can be applied automatically instead of depending only on manual checks.

---

# 3. Secrets and Key Management

## Overview

### Microsoft Azure – Azure Key Vault

Azure Key Vault securely stores and manages secrets, certificates, and encryption keys.

### AWS – AWS Secrets Manager and AWS KMS

AWS Secrets Manager stores and manages secrets such as passwords and API keys. AWS Key Management Service (KMS) manages encryption keys.

### Google Cloud – Secret Manager and Cloud KMS

Google Secret Manager stores sensitive information such as passwords and API keys. Cloud KMS manages encryption keys.

---

## Core Features

| Feature | Microsoft Azure | AWS | Google Cloud |
|---|---|---|---|
| Secret Storage | Key Vault | Secrets Manager | Secret Manager |
| Encryption Keys | Key Vault | AWS KMS | Cloud KMS |
| Access Control | Yes | Yes | Yes |
| Secret Rotation Support | Yes | Yes | Yes |
| Application Integration | Yes | Yes | Yes |

---

## Security & Compliance

These services help prevent developers from storing passwords and secrets directly inside application code.

Access to secrets can be controlled using the identity and access management system of each cloud provider.

Encryption can also help protect sensitive information.

Secrets management services can support compliance requirements by providing controlled access, encryption, logging, and secret management.

---

## Pricing Model

Azure Key Vault pricing depends on operations and the type of keys or protection being used.

AWS Secrets Manager is usage-based. Customers are generally charged for secrets stored and API calls. AWS KMS has separate pricing for keys and cryptographic operations.

Google Secret Manager pricing is based on factors such as active secret versions and access operations. Cloud KMS has separate pricing for keys and cryptographic operations.

---

## DevSecOps Integration

Secrets management is very important for DevSecOps.

CI/CD pipelines can retrieve passwords, API keys, or other credentials securely instead of saving them directly in source code or Git repositories.

Applications can also retrieve secrets when they need them without exposing the secret directly to developers.

---

## Analysis

The three providers offer similar solutions.

One difference is that Azure Key Vault provides secrets, certificates, and key management through one main service, while AWS and GCP separate some of these functions into different services.

In my opinion, using a secrets management service is much safer than storing passwords or API keys directly in application code.

---

# 4. Network Access Control

## Overview

### Microsoft Azure – Network Security Groups

Azure Network Security Groups control inbound and outbound network traffic using security rules.

### AWS – Security Groups

AWS Security Groups act as virtual firewalls for supported AWS resources. They control allowed inbound and outbound traffic.

### Google Cloud – VPC Firewall Rules

Google Cloud VPC Firewall Rules control network traffic for resources connected to VPC networks.

---

## Core Features

| Feature | Microsoft Azure | AWS | Google Cloud |
|---|---|---|---|
| Inbound Rules | Yes | Yes | Yes |
| Outbound Rules | Yes | Yes | Yes |
| Port Control | Yes | Yes | Yes |
| Protocol Control | Yes | Yes | Yes |
| Source/Destination Controls | Yes | Yes | Yes |

---

## Security & Compliance

Network access control helps reduce unauthorized connections to cloud resources.

For example, administrators can allow HTTPS traffic on port 443 while restricting access to administrative services.

Another important security practice is to only open ports that are really necessary.

Network security controls can also help organizations meet security requirements by limiting unnecessary access to systems.

---

## Pricing Model

Basic network security rules are generally part of the cloud networking services and normally do not have a separate charge just for creating a rule.

Other networking services, traffic processing, logging, or advanced security features can create additional costs.

---

## DevSecOps Integration

Network rules can be created automatically using Infrastructure as Code tools such as Terraform.

This allows security rules to be reviewed and deployed together with the infrastructure.

Network configuration can also be stored in version control, making changes easier to review and audit.

---

## Analysis

Azure NSG, AWS Security Groups, and Google Cloud VPC Firewall Rules have the same general objective: control network traffic.

The configuration and rule models are different, but all three are important for protecting cloud resources.

---

# 5. DDoS Protection

## Overview

### Microsoft Azure – Azure DDoS Protection

Azure DDoS Protection helps protect Azure resources against Distributed Denial-of-Service attacks.

### AWS – AWS Shield

AWS Shield provides protection against DDoS attacks for supported AWS applications and resources.

### Google Cloud – Google Cloud Armor

Google Cloud Armor provides DDoS protection and security policies for applications using supported Google Cloud infrastructure.

---

## Core Features

| Feature | Microsoft Azure | AWS | Google Cloud |
|---|---|---|---|
| DDoS Detection | Yes | Yes | Yes |
| Attack Mitigation | Yes | Yes | Yes |
| Traffic Protection | Yes | Yes | Yes |
| Monitoring | Yes | Yes | Yes |
| Advanced Protection Option | Yes | Shield Advanced | Cloud Armor Enterprise |

---

## Security & Compliance

DDoS protection is important for availability.

A successful DDoS attack can make a website or service unavailable to legitimate users.

These services help detect and reduce malicious traffic before it affects applications.

Availability and network protection are also important parts of many security and compliance programs.

---

## Pricing Model

Azure provides different DDoS protection options. Advanced protection has additional costs that depend on the protection model and deployment.

AWS Shield Standard is automatically included for supported AWS services. AWS Shield Advanced provides additional capabilities for a fee.

Google Cloud Armor has Standard and Enterprise pricing options. Costs can depend on security policies, rules, requests, protected resources, and the selected service level.

---

## DevSecOps Integration

DDoS protection can be included in cloud architecture and Infrastructure as Code deployments.

Monitoring and alerts can also be integrated with security operations so teams can identify attacks and respond to problems.

---

## Analysis

All three providers offer DDoS protection.

The main goal is to maintain application availability during attacks. The pricing and level of protection depend on the service and plan selected.

Google Cloud Armor is also interesting because the same service provides DDoS protection and Web Application Firewall capabilities.

---

# 6. Web Application Security

## Overview

### Microsoft Azure – Web Application Firewall

Azure Web Application Firewall protects web applications from common web attacks.

### AWS – AWS WAF

AWS WAF monitors web requests and allows administrators to create rules to block or allow requests.

### Google Cloud – Google Cloud Armor

Google Cloud Armor provides Web Application Firewall capabilities and security policies for supported applications.

---

## Core Features

| Feature | Microsoft Azure | AWS | Google Cloud |
|---|---|---|---|
| Web Traffic Filtering | Yes | Yes | Yes |
| Custom Security Rules | Yes | Yes | Yes |
| Managed Rules | Yes | Yes | Yes |
| IP Filtering | Yes | Yes | Yes |
| Protection Against Common Web Attacks | Yes | Yes | Yes |

---

## Security & Compliance

WAF services can help protect applications from attacks such as SQL injection and Cross-Site Scripting (XSS).

They add an extra security layer between internet users and web applications.

WAF rules can also help organizations apply security requirements to public web applications.

---

## Pricing Model

Azure WAF pricing depends on the Azure service used with the WAF, such as Application Gateway or Front Door, and its configuration.

AWS WAF pricing is usage-based and can depend on web ACLs, rules, and requests.

Google Cloud Armor pricing can depend on policies, rules, requests, protected resources, and the selected service level.

---

## DevSecOps Integration

WAF rules can be managed using automation and Infrastructure as Code.

Security teams can also monitor WAF events and use them in security detection systems.

This allows application security rules to become part of the deployment and operations process.

---

## Analysis

Azure WAF and AWS WAF are direct solutions for web application protection.

Google Cloud Armor combines WAF capabilities with other network and DDoS security features.

All three services can help protect applications before malicious requests reach the application.

---

# 7. Monitoring and Logging

## Overview

### Microsoft Azure – Azure Monitor and Log Analytics

Azure Monitor collects monitoring data from applications and infrastructure. Log Analytics is a tool in Azure Monitor that allows administrators to query and analyze log data.

### AWS – Amazon CloudWatch

Amazon CloudWatch collects and monitors metrics, logs, and events from AWS resources and applications.

### Google Cloud – Cloud Monitoring and Cloud Logging

Cloud Monitoring collects metrics and provides visibility into resources. Cloud Logging collects, stores, and analyzes logs.

---

## Core Features

| Feature | Microsoft Azure | AWS | Google Cloud |
|---|---|---|---|
| Log Collection | Yes | Yes | Yes |
| Metrics | Yes | Yes | Yes |
| Alerts | Yes | Yes | Yes |
| Dashboards | Yes | Yes | Yes |
| Log Analysis | Log Analytics | CloudWatch Logs | Cloud Logging |
| Infrastructure Monitoring | Yes | Yes | Yes |

---

## Security & Compliance

Monitoring and logging are important for security because logs can show suspicious activity, errors, and unauthorized access attempts.

Logs can also provide evidence for security investigations and compliance audits.

Organizations can create alerts when specific security events are detected.

Logging and monitoring can help organizations support auditing and compliance requirements by keeping records of system activity.

---

## Pricing Model

Azure Monitor pricing depends on the features being used. Log costs can depend on data ingestion, retention, and the selected plan.

Amazon CloudWatch pricing depends on usage such as metrics, logs, alarms, dashboards, and other monitoring features.

Google Cloud Monitoring and Cloud Logging are priced mainly by data volume or usage. Google also provides free usage allowances for some observability features.

---

## DevSecOps Integration

Monitoring can be integrated with applications and CI/CD processes.

Teams can create alerts when an application has a problem or when suspicious activity is detected.

Logs can also be sent to SIEM platforms for additional security analysis.

Monitoring is important after deployment because DevSecOps includes both development and operations.

---

## Analysis

The three platforms provide similar monitoring capabilities.

Azure uses Azure Monitor with Log Analytics for log queries and analysis. Google provides Cloud Monitoring and Cloud Logging. AWS provides many of these monitoring functions through Amazon CloudWatch.

Monitoring is important in DevSecOps because security does not stop after deployment. Applications and infrastructure need to be monitored continuously.

---

# 8. Cloud Security

## Overview

### Microsoft Azure – Microsoft Defender for Cloud

Microsoft Defender for Cloud provides cloud security posture management, security recommendations, and workload protection.

### AWS – AWS Security Hub and Amazon GuardDuty

AWS Security Hub centralizes security findings and helps organizations understand their cloud security posture.

Amazon GuardDuty provides threat detection by analyzing supported AWS data sources for suspicious or malicious activity.

### Google Cloud – Security Command Center

Google Cloud Security Command Center provides security posture management, threat detection, vulnerability information, and centralized security findings.

---

## Core Features

| Feature | Microsoft Azure | AWS | Google Cloud |
|---|---|---|---|
| Security Posture Management | Yes | Security Hub | Security Command Center |
| Threat Detection | Yes | GuardDuty | Yes |
| Security Recommendations | Yes | Yes | Yes |
| Security Findings | Yes | Security Hub | Yes |
| Compliance Monitoring | Yes | Yes | Yes |

---

## Security & Compliance

These services help organizations identify security problems and improve their cloud security posture.

They can compare configurations with security standards and provide recommendations for improving security.

Security teams can use these findings to identify resources that may be vulnerable or incorrectly configured.

The cloud providers also support many compliance programs and standards, including ISO 27001, SOC reports, and PCI DSS. However, using a compliant cloud service does not automatically make an application compliant. The organization is still responsible for configuring and using the service correctly.

---

## Pricing Model

Microsoft Defender for Cloud has different plans and pricing based on the workloads and protections enabled.

AWS Security Hub and Amazon GuardDuty use usage-based pricing. GuardDuty costs depend on the amount and type of security data analyzed.

Google Security Command Center provides different service tiers. The available capabilities and pricing depend on the selected tier.

---

## DevSecOps Integration

These platforms can help identify security problems during development and operation.

Security findings can be integrated with automated workflows, monitoring systems, and security tools.

This can help teams detect problems earlier and respond faster.

---

## Analysis

There is not a perfect one-to-one equivalent for Defender for Cloud in AWS.

AWS divides similar functions between services such as Security Hub and GuardDuty.

Google Security Command Center provides many similar cloud security capabilities in one platform.

This shows that different cloud providers can solve similar security problems using different architectures.

---

# 9. SIEM and SOAR

## Overview

### Microsoft Azure – Microsoft Sentinel

Microsoft Sentinel is Microsoft's cloud-native SIEM and SOAR platform.

It collects and analyzes security data and helps security teams detect, investigate, and respond to incidents.

### AWS – Amazon Security Lake and AWS Security Services

AWS does not provide one single service that is a direct replacement for Microsoft Sentinel.

Amazon Security Lake can centralize security data from AWS and other sources. Other AWS security services can then be used for threat detection, investigation, and response.

Because of this, AWS uses a more distributed approach compared with Microsoft Sentinel.

### Google Cloud – Google Security Operations

Google Security Operations provides SIEM and security operations capabilities for collecting, analyzing, detecting, and investigating security information.

---

## Core Features

| Feature | Microsoft Azure | AWS | Google Cloud |
|---|---|---|---|
| Centralized Security Data | Yes | Security Lake | Yes |
| Threat Detection | Yes | Multiple AWS services | Yes |
| Security Analytics | Yes | Multiple AWS services | Yes |
| Incident Investigation | Yes | Multiple AWS services | Yes |
| Automated Response | SOAR | Automation using AWS services | Security Operations capabilities |
| Integration with Security Tools | Yes | Yes | Yes |

---

## Security & Compliance

SIEM platforms help security teams monitor events from many different systems.

They can identify suspicious activity and provide information that helps teams investigate security incidents.

Centralized security logs can also help with auditing and compliance requirements.

SIEM and security operations tools can support compliance programs by providing visibility, logging, investigation, and incident response capabilities.

---

## Pricing Model

Microsoft Sentinel pricing is mainly based on the amount of security data ingested and analyzed. Microsoft provides different pricing options, including pay-as-you-go and commitment tiers for eligible data.

AWS security operations costs depend on the individual AWS services being used. Amazon Security Lake pricing can depend on data ingestion, transformation, storage, and other services used with it.

Google Security Operations pricing depends on the selected service agreement and security operations package.

---

## DevSecOps Integration

SIEM and SOAR platforms are useful in DevSecOps because they can collect security information from applications, cloud resources, CI/CD environments, and security tools.

They can also automate responses to security incidents.

For example, a security alert can start an automated workflow that sends a notification or performs a security action.

This can reduce the time between detecting a security problem and responding to it.

---

## Analysis

Microsoft Sentinel provides SIEM and SOAR capabilities in one security operations platform.

Google Security Operations provides similar SIEM and security operations capabilities.

AWS takes a more distributed approach where Security Lake and different AWS security services can work together.

This is an important difference between the three cloud providers. It also shows why cloud services are not always direct one-to-one equivalents.

---

# Overall Comparison

After researching these services, I found that Azure, AWS, and Google Cloud provide strong security capabilities, but they organize their services differently.

Azure provides many security tools that integrate with Microsoft products and services.

AWS has many specialized security services. Sometimes multiple AWS services are needed to provide capabilities similar to one Azure service.

Google Cloud also provides strong security services. Some products, such as Cloud Armor and Security Command Center, provide multiple security capabilities.

Another important point is that the services are not always direct replacements for each other. Microsoft Sentinel is a good example because AWS does not have one single service that works exactly the same way.

From a DevSecOps perspective, all three providers support automation, Infrastructure as Code, monitoring, identity management, and security controls.

This allows security to be included during development, deployment, and operations instead of only checking security after an application is deployed.

Identity security is also an important part of DevSecOps. Strong authentication, MFA, least privilege, and secure management of secrets can reduce the risk of unauthorized access to development and production environments.

---

# Conclusion

This comparison helped me understand that cloud security concepts are similar across Azure, AWS, and Google Cloud, even when the service names and implementations are different.

Identity management, network security, secrets management, monitoring, governance, threat detection, and incident response are important in all three cloud platforms.

One important lesson is that security should use multiple layers. A strong password is useful, but it should not be the only protection. MFA adds another security layer, while access controls can limit what a user is allowed to do.

Another important lesson is the principle of least privilege. Users, applications, and automated systems should only receive the permissions they really need.

In my opinion, there is no cloud provider that is always the best choice. The best platform depends on the company, its infrastructure, security requirements, budget, and existing technologies.

Because we used Microsoft Azure during this course, I am more familiar with Azure services. However, after this research, I can see that many of the same security concepts can also be applied in AWS and Google Cloud.

This is important for my understanding of DevSecOps because the tools can change between cloud providers, but the main security concepts remain very similar.

---

# References

## Microsoft Azure

* [Microsoft Entra ID Documentation](https://learn.microsoft.com/en-us/entra/identity/)
* [Microsoft Entra Conditional Access Documentation](https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview)
* [Azure Policy Documentation](https://learn.microsoft.com/en-us/azure/governance/policy/)
* [Azure Key Vault Documentation](https://learn.microsoft.com/en-us/azure/key-vault/)
* [Azure Network Security Groups Documentation](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)
* [Azure DDoS Protection Documentation](https://learn.microsoft.com/en-us/azure/ddos-protection/ddos-protection-overview)
* [Azure Web Application Firewall Documentation](https://learn.microsoft.com/en-us/azure/web-application-firewall/overview)
* [Azure Monitor Documentation](https://learn.microsoft.com/en-us/azure/azure-monitor/)
* [Microsoft Defender for Cloud Documentation](https://learn.microsoft.com/en-us/azure/defender-for-cloud/)
* [Microsoft Sentinel Documentation](https://learn.microsoft.com/en-us/azure/sentinel/)
* [Microsoft Azure Compliance Offerings](https://learn.microsoft.com/en-us/azure/compliance/)

## Amazon Web Services

* [AWS Identity and Access Management Documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)
* [AWS IAM Identity Center Documentation](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)
* [AWS Config Documentation](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)
* [AWS Organizations Documentation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)
* [AWS Secrets Manager Documentation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)
* [AWS Key Management Service Documentation](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html)
* [AWS Security Groups Documentation](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html)
* [AWS Shield Documentation](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html)
* [AWS WAF Documentation](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html)
* [Amazon CloudWatch Documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
* [AWS Security Hub Documentation](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html)
* [Amazon GuardDuty Documentation](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)
* [Amazon Security Lake Documentation](https://docs.aws.amazon.com/security-lake/latest/userguide/what-is-security-lake.html)
* [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/)

## Google Cloud

* [Google Cloud IAM Documentation](https://cloud.google.com/iam/docs/overview)
* [Cloud Identity Documentation](https://cloud.google.com/identity/docs/overview)
* [Organization Policy Service Documentation](https://cloud.google.com/resource-manager/docs/organization-policy/overview)
* [Secret Manager Documentation](https://cloud.google.com/secret-manager/docs/overview)
* [Cloud Key Management Service Documentation](https://cloud.google.com/kms/docs)
* [VPC Firewall Rules Documentation](https://cloud.google.com/firewall/docs/firewalls)
* [Google Cloud Armor Documentation](https://cloud.google.com/armor/docs/cloud-armor-overview)
* [Cloud Monitoring Documentation](https://cloud.google.com/monitoring/docs)
* [Cloud Logging Documentation](https://cloud.google.com/logging/docs)
* [Security Command Center Documentation](https://cloud.google.com/security-command-center/docs)
* [Google Security Operations Documentation](https://cloud.google.com/chronicle/docs/overview)
* [Google Cloud Compliance](https://cloud.google.com/security/compliance)
