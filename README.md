<p align="center">
  <img src="https://github.com/100DaysOfCloud/100DaysOfCloudIdeas/blob/master/banner.png?raw=true">
</p>

# 100DaysOfCloud Ideas List

The purpose of this repo is to provide a list of micro-projects to help people with their #100DaysOfCloud Challenge.

- If you want to take the challenge go to: https://100daysofcloud.com
- The #100DaysOfCloud Challenge Template is here: https://github.com/100DaysOfCloud/100DaysOfCloud

## Contributing to this project list:

- You can propose a cloud project by opening a [ticket 🎟️](https://github.com/100DaysOfCloud/100DaysOfCloudIdeas/issues/new?assignees=&labels=&template=cloud-project-idea.md&title=)
- You need to use our [Project Template](Templates/PROJECT-TEMPLATE.md) and submit it as a pull request.

### Please do your best to tag your commits

When you open a ticket it will have a Github Issue ID eg. 23

You should reference this number both in your branch name and your PR's commit message.

Including this number will keep track of your commits in the project idea's Github Issue.

eg. Branch Name

```
git checkout -b 23-COM01-AWS100
```

eg. Commit Message

```
#23 — Launching an EC2 instance
```

### We may edit your project submissions in your Pull Requests

When you submit a Pull Request (PR) we may edit the following without notice:

- Typos
- Markdown formatting
- Difficulty Level

We do this to expedite the review process so your project is quickly
accepted into the Ideas repository.

## Which Cloud Service Providers?

Projects covered could be for:

- Microsoft Azure
- Amazon Web Services
- Google Cloud Platform

We aren't limited to the big three, but thats where you'll see the most examples since IaaS have the most cloud offerings.

We may be weary of third-party cloud services since the goal of these projects is to learn a concept first and a product last.

## What is the difficulty and time commitment for these projects?

Projects are labeled based these four levels:

- Level 100 (Introductory)
- Level 200 (Intermediate)
- Level 300 (Advanced)
- Level 400 (Expert)

The goal is to provide micro-projects that can be completed in minutes to hours and worst case a day.
The difficulty generally indicates greater time commitment.
For more difficult projects more instruction can be provided to reduce the time commitment.
Projects may suggest the time it takes to complete the project

# The Cloud Project Ideas

- [UNI — Unicorn Projects](#-uni--unicorn-projects)
- [SEC — Cloud Security](#-sec--cloud-security)
- [COM — Cloud Computing](#-com--cloud-computing)
- [NET — Cloud Networking](#-net---cloud-networking)
- [BIL — Cloud Billing and Pricing](#-bil--cloud-billing-and-pricing)
- [GLU — Application Integration](#-glu--application-integration)
- [LES — Serverless](#-les--serverless)
- [ARC — Solution Architecting](#%EF%B8%8F-arc--solution-architecting)
- [MLS — Machine Learning](#-mls--machine-learning)
- [IOT — Internet of Things](#-iot--internet-of-things)
- [STR — Cloud Storage](#-str--cloud-storage)
- [DBS — Databases](#-dbs--databases)
- [DEV — Developer Tools](#%EF%B8%8F-dev--developer-tools)
- [OPS — DevOps](#%EF%B8%8F-ops--devops)
- [BIG — Big Data and Analytics](#big--big-data-and-analytics)
- [GOV — Management and Governance](#-gov--management-and-governance)
- [MLT — Multi-Cloud](#%EF%B8%8F-mlt--multi-cloud)
- [HYR — Hybrid-Cloud](#%EF%B8%8F-hyr--hybrid-cloud)
- [BOT — Robots](#-bot--robots)
- [LOW — Low/No Code](#low--lowno-code)

## 🦄 UNI — Unicorn Projects

These are larger projects that use multiple cloud services.

- **UNI01** — Hosting your Dev Blog [First Project Recommendations]

## 🔒 SEC — Cloud Security

### **SEC01** — Hardware Security Modules (HSM)

| Project Code | Project Details                                              | Difficulty | CSP   | Author(s)                                        |
| :----------- | :----------------------------------------------------------- | :--------- | :---- | :----------------------------------------------- |
| SEC01-AWS200 | [Create a new CMK in KMS and encrypt an object](Projects/SEC/SEC01/SEC01-AWS200.md) | Level 200  | AWS   | [Andrew Brown](https://twitter.com/andrewbrown)  |
| SEC01-AZ200  | [Configure and manage secrets in Azure Key Vault](Projects/SEC/SEC01/SEC01-AZ200.md) | Level 200  | Azure | [Gwyneth Peña S.](https://twitter.com/madebygps) |
| SEC01-GCP100 | [Create and Use HSM-Protected Encryption Keys](Projects/SEC/SEC01/SEC01-GCP100.md) | Level 100  | GCP   | [Saran Mahadev](https://github.com/saranmahadev) |

### **SEC02** — Configuration and Remediation Service

| Project Code | Project Details                                                          | Difficulty | CSP   | Author(s)                                        |
| :----------- | :----------------------------------------------------------------------- | :--------- | :---- | :----------------------------------------------- |
| SEC02-AWS100 | [Use a managed rule from AWS Config](Projects/SEC/SEC02/SEC02-AWS100.md) | Level 100  | AWS   | [Andrew Brown](https://twitter.com/andrewbrown)  |
| SEC02-AZ100  | [Create an Azure Policy](Projects/SEC/SEC02/SEC02-AZ100.md)              | Level 100  | Azure | [Gwyneth Peña S.](https://twitter.com/madebygps) |
| SEC02-GCP100 |                                                                          | Level 100  | GCP   |                                                  |

### **SEC03** — Security Development Lifecycle

| Project Code | Project Details                                                                 | Difficulty | CSP   | Author(s)                                        |
| :----------- | :------------------------------------------------------------------------------ | :--------- | :---- | :----------------------------------------------- |
| SEC03-AWS100 |                                                                                 | Level 100  | AWS   |                                                  |
| SEC03-AZ100  | [Secure development best practices on Azure](Projects/SEC/SEC03/SEC03-AZ100.md) | Level 100  | Azure | [Gwyneth Peña S.](https://twitter.com/madebygps) |
| SEC03-GCP100 |                                                                                 | Level 100  | GCP   |                                                  |

### **SEC04** — Manage Identities

| Project Code | Project Details                                              | Difficulty | CSP   | Author(s)                                         |
| :----------- | :----------------------------------------------------------- | :--------- | :---- | :------------------------------------------------ |
| SEC04-AWS100 | [Create an IAM user](Projects/SEC/SEC04/SEC04-AWS100.md)     | Level 100  | AWS   | [Syed Auther](https://twitter.com/syedauther)     |
| SEC04-AZ100  | [Create a user in Azure AD](Projects/SEC/SEC04/SEC04-AZ100.md) | Level 100  | Azure | [Gwyneth Peña S.](twitter.com/madebygps)          |
| SEC04-GCP100 | [Create an IAM user](Projects/SEC/SEC04/SEC04-GCP100.md)     | Level 100  | GCP   | [Saran Mahadev ](https://github.com/saranmahadev) |

### **SEC05** — Identity Federation

| Project Code | Project Details                                          | Difficulty | CSP   | Author(s)                                |
| :----------- | :------------------------------------------------------- | :--------- | :---- | :--------------------------------------- |
| SEC05-AWS100 |                                                          | Level 100  | AWS   |                                          |
| SEC05-AZ100  | [Azure AD federation](Projects/SEC/SEC05/SEC05-AZ100.md) | Level 100  | Azure | [Gwyneth Peña S.](twitter.com/madebygps) |
| SEC05-GCP100 |                                                          | Level 100  | GCP   |                                          |

## 🖥 COM — Cloud Computing

### **COM01** - Bare Metal

| Project Code | Project Details                                            | Difficulty | CSP   | Author(s)                                |
| :----------- | :--------------------------------------------------------- | :--------- | :---- | :--------------------------------------- |
| COM01-AWS100 |                                                            | Level 100  | AWS   |                                          |
| COM01-AZ200  | [Azure VMware Solution](Projects/COM/COM01/COM01-AZ200.md) | Level 100  | Azure | [Gwyneth Peña S.](twitter.com/madebygps) |
| COM01-GCP100 |                                                            | Level 100  | GCP   |                                          |

### **COM02** - Dedicated

| Project Code | Project Details                                                                     | Difficulty | CSP   | Author(s)                                |
| :----------- | :---------------------------------------------------------------------------------- | :--------- | :---- | :--------------------------------------- |
| COM02-AWS100 |                                                                                     | Level 100  | AWS   |                                          |
| COM02-AZ200  | [Deploy VMs to dedicated hosts using the portal](Projects/COM/COM02/COM02-AZ200.md) | Level 200  | Azure | [Gwyneth Peña S.](twitter.com/madebygps) |
| COM02-GCP100 |                                                                                     | Level 100  | GCP   |                                          |

### **COM03** - Virtual Machines

| Project Code | Project Details                                                                    | Difficulty | CSP   | Author(s)                                        |
| :----------- | :--------------------------------------------------------------------------------- | :--------- | :---- | :----------------------------------------------- |
| COM03-AWS100 | [Launch a Hello World website on the internet](Projects/COM/COM03/COM03-AWS100.md) | Level 100  | AWS   | [Syed Auther](https://twitter.com/syedauther)    |
| COM03-AWS200 | [Create an Auto Scaling Group](Projects/COM/COM03/COM03-AWS200.md)                 | Level 200  | AWS   | [Chris Nagy](https://twitter.com/chris_the_nagy) |
| COM03-AZ100|   [Introduction to Azure virtual machines](Projects/COM/COM03/COM03-AZ100.md)                                                                                 | Level 100  | Azure |  [Gwyneth Peña S.](twitter.com/madebygps)                                                |
| COM03-GCP100 | [Deploy a Weather website to the Internet](Projects/COM/COM03/COM03-GCP100.md) | Level 100  | GCP   | [Saran Mahadev](https://github.com/saranmahadev) |

### **COM04** - Containers

| Project Code | Project Details                                                                               | Difficulty | CSP   | Author(s)                                          |
| :----------- | :-------------------------------------------------------------------------------------------- | :--------- | :---- | :------------------------------------------------- |
| COM04-AWS100 | [Push a Docker image to Amazon ECR repository](Projects/COM/COM04/COM04-AWS100.md)            | Level 100  | AWS   | [Johan Rin](https://twitter.com/johanrin)          |
| COM04-AWS200 | [Deploy a Docker container image on AWS Fargate](Projects/COM/COM04/COM04-AWS200.md)          | Level 200  | AWS   | [Johan Rin](https://twitter.com/johanrin)          |
| COM04-AWS400 | [Create a cluster of virtual machines using docker swarm](Projects/COM/COM04/COM04-AWS400.md) | Level 400  | AWS   | [Karan Gauswami](https://github.com/KaranGauswami) |
| COM04-AZ100  |                                                                                               | Level 100  | Azure |                                                    |
| COM04-GCP100 |                                                                                               | Level 100  | GCP   |                                                    |

## 🌐 NET — Cloud Networking

### **NET01** — Classless Inter-Domain Routing (CIDR)

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| NET01-AWS100 |        | Level 100  | AWS   |         |
| NET01-AZ200  |[Plan your Virtual Network](Projects/NET/NET01/NET01-AZ200.md) | Level 100  | Azure |  [Gwyneth Peña S.](https://twitter.com/madebygps)           |
| NET01-GCP100 |                 | Level 100  | GCP   |           |

### **NET02** — VPC / VNET Peering

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| NET02-AWS100 |                 | Level 100  | AWS   |           |
| NET02-AZ100  |   [Connect VNets with VNet peering](Projects/NET/NET02/NET02-AZ100.md)              | Level 100  | Azure |  [Gwyneth Peña S.](https://twitter.com/madebygps)          |
| NET02-GCP100 |                 | Level 100  | GCP   |           |

### **NET03** — Transfer Acceleration

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| NET03-AWS100 |                 | Level 100  | AWS   |           |
| NET03-AZ100  |                 | Level 100  | Azure |           |
| NET03-GCP100 |                 | Level 100  | GCP   |           |

### **NET04** — Content Distribution Networks (CDNs)

| Project Code | Project Details                                                                                                      | Difficulty | CSP   | Author(s)                                               |
| :----------- | :------------------------------------------------------------------------------------------------------------------- | :--------- | :---- | :------------------------------------------------------ |
| NET04-AWS100 | [Host a simple static webpage with S3 and CloudFront](Project/net/net04/../../../Projects/NET/NET04/NET04-AWS100.md) | Level 100  | AWS   | [Antonio Lo Fiego](https://twitter.com/antonio_lofiego) |
| NET04-AZ100 |[Azure CDN and Blob Services](Project/net/net04/../../../Projects/NET/NET04/NET04-AZ200.md)                                                                                                                      | Level 200  | Azure | [Gwyneth Peña S.](https://twitter.com/madebygps)                                                          |
| NET04-GCP200 | [Create a Load Balancer for a File in Cloud Storage with Cloud CDN](D:\Projects\Contribution\Projects\NET\NET04\NET04-GCP100.md) | Level 200 | GCP   | [Saran Mahadev](https://github.com/saranmahadev) |

## 🧾 BIL — Cloud Billing and Pricing

### **BIL01** — Billing alerts

This micro-project is all about avoiding overbilling due to misconfiguration.

> ⭐ BIL01 is recommended as a good first-time project

| Project Code | Project Details                                                      | Difficulty | CSP   | Author(s)                                        |
| :----------- | :------------------------------------------------------------------- | :--------- | :---- | :----------------------------------------------- |
| BIL01-AWS100 | [Create three Billing Alarms](Projects/BIL/BIL01/BIL01-AWS100.md)    | Level 100  | AWS   | [Chris Nagy](https://twitter.com/chris_the_nagy) |
| BIL01-AZ100  | [Create two types of Cost Alerts](Projects/BIL/BIL01/BIL01-AZ100.md) | Level 100  | Azure | [Gwyneth Peña S.](https://twitter.com/madebygps) |
| BIL01-GCP100 | [Create three Budget Alerts](Projects/BIL/BIL01/BIL01-GCP100.md)     | Level 100  | GCP   | [Andrew Brown](https://twitter.com/andrewbrown)  |

### **BIL02** — Budgets

This micro-project is all about controlling your spending.

> ⭐ BIL02 is recommended as a good first-time project

| Project Code | Project Details                                              | Difficulty | CSP   | Author(s)                                        |
| :----------- | :----------------------------------------------------------- | :--------- | :---- | :----------------------------------------------- |
| BIL02-AWS100 | [Create a Cost Budget](Projects/BIL/BIL02/BIL02-AWS100.md)   | Level 100  | AWS   | [Ariela](https://twitter.com/ari_hacks)          |
| BIL02-AZ100  | [Create budgets](Projects/BIL/BIL02/BIL02-AZ100.md)          | Level 100  | Azure | [Gwyneth Peña S.](https://twitter.com/madebygps) |
| BIL02-GCP100 | [Limit BigQuery query usage using Quotas](Projects/BIL/BIL02/BIL02-AZ100.md) | Level 100  | GCP   | [Saran Mahadev](https://github.com/saranmahadev) |

## 🩹 GLU — Application Integration

Application Integration are cloud services that are used to help other services or apps talk to each other.
Messaging Systems are commonly used for Application Integration.

### **GLU01** — Messaging Queueing Service

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| GLU01-AWS100 |                 | Level 100  | AWS   |           |
| GLU01-AZ100  | [Create an Azure Queue in the Portal](Projects/GLU/GLU01/GLU01-AZ100.md)                | Level 100  | Azure | [Gwyneth Pena S.](https://twitter.com/madebygps)          |
| GLU01-GCP100 |                 | Level 100  | GCP   |           |

### **GLU02** — Pub/Sub Messaging Service

| Project Code | Project Details                                              | Difficulty | CSP   | Author(s)                                                  |
| :----------- | :----------------------------------------------------------- | :--------- | :---- | :--------------------------------------------------------- |
| GLU02-AWS100 | [Introduction to SNS (Simple Notification Service)](Projects/GLU/GLU02/GLU02-AWS100.md) | Level 100  | AWS   | [Edward Allen Mercado](https://twitter.com/edwardmercado_) |
| GLU02-AZ200  | [Introduction to Azure Service Bus](Projects/GLU/GLU02/GLU02-AZ200.md) | Level 200  | Azure | [Gwyneth Pena S.](https://twitter.com/madebygps)           |
| GLU02-GCP100 | [Introduction to Cloud Pub/Sub](Projects/GLU/GLU02/GLU02-GCP100.md) | Level 100  | GCP   | [Saran Mahadev](https://github.com/saranmahadev)           |

### **GLU03** — Streaming Service

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| GLU03-AWS100 |                 | Level 100  | AWS   |           |
| GLU03-AZ100  |                 | Level 100  | Azure |           |
| GLU03-GCP100 |                 | Level 100  | GCP   |           |

### **GLU04** — Event Bus Service

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| GLU04-AWS100 |                 | Level 100  | AWS   |           |
| GLU04-AZ100  |                 | Level 100  | Azure |           |
| GLU04-GCP100 |                 | Level 100  | GCP   |           |

### **GLU05** — GraphQL Service

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| GLU05-AWS100 |                 | Level 100  | AWS   |           |
| GLU05-AZ100  |                 | Level 100  | Azure |           |
| GLU05-GCP100 |                 | Level 100  | GCP   |           |

### **GLU06** — PartiQ

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| GLU06-AWS100 |                 | Level 100  | AWS   |           |
| GLU06-AZ100  |                 | Level 100  | Azure |           |
| GLU06-GCP100 |                 | Level 100  | GCP   |           |

### **GLU07** — State Machine Service

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| GLU07-AWS200 | [Setup a simple state machine with at least 2 steps](Projects/GLU/GLU07/GLU07-AWS200.md) | Level 200  | AWS   | [Syed Auther](https://twitter.com/syedauther) |
| GLU07-AZ100  |                 | Level 100  | Azure |           |
| GLU07-GCP100 |                 | Level 100  | GCP   |           |

## 🐹 LES — Serverless

Serverless tech abstracts the need to care for the underlying infrastructure, giving you more time to focus on logic.

### **LES01** — Serverless Functions

| Project Code | Project Details                                              | Difficulty | CSP   | Author(s)                                        |
| :----------- | :----------------------------------------------------------- | :--------- | :---- | :----------------------------------------------- |
| LES01-AWS100 | [Create a Lambda to add 2 numbers](Projects/LES/LES01/LES01-AWS100.md) | Level 100  | AWS   | [Syed Auther](https://twitter.com/syedauther)    |
| LES01-AWS200 | [Create a simple serverless API](Projects/LES/LES01/LES01-AWS200.md) | Level 200  | AWS   | [Syed Auther](https://twitter.com/syedauther)    |
| LES01-AZ200  | [Create an Azure Function in the Azure Portal](Projects/LES/LES01/LES01-AZ200.md) | Level 200  | Azure | [Gwyneth Pena S.](https://twitter.com/madebygps) |
| LES01-GCP100 |                                                              | Level 100  | GCP   |                                                  |

### **LES02** — Serverless Containers

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| LES02-AWS100 |                 | Level 100  | AWS   |           |
| LES02-AZ100  |                 | Level 100  | Azure |           |
| LES02-GCP100 |                 | Level 100  | GCP   |           |

### **LES03** — Serverless Storage

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| LES03-AWS100 |                 | Level 100  | AWS   |           |
| LES03-AZ100  |                 | Level 100  | Azure |           |
| LES03-GCP100 |                 | Level 100  | GCP   |           |

### **LES04** — Serverless NoSQL

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| LES04-AWS100 |                 | Level 100  | AWS   |           |
| LES04-AZ100  |                 | Level 100  | Azure |           |
| LES04-GCP100 |                 | Level 100  | GCP   |           |

### **LES05** — Serverless SQL

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| LES05-AWS100 |                 | Level 100  | AWS   |           |
| LES05-AZ100  |                 | Level 100  | Azure |           |
| LES05-GCP100 |                 | Level 100  | GCP   |           |

## ✍️ ARC — Solution Architecting

### **ARC01** - Creating an architectural diagram

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| ARC01-AWS100 |                 | Level 100  | AWS   |           |
| ARC01-AZ100  |                 | Level 100  | Azure |           |
| ARC01-GCP100 |                 | Level 100  | GCP   |           |

### **ARC02** - Well-Architected Framework

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| ARC02-AWS100 |                 | Level 100  | AWS   |           |
| ARC02-AZ100  |                 | Level 100  | Azure |           |
| ARC02-GCP100 |                 | Level 100  | GCP   |           |

## 🤖 MLS — Machine Learning

### **MLS01** — AutoML Service

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| MLS01-AWS100 |                 | Level 100  | AWS   |           |
| MLS01-AZ100  |                 | Level 100  | Azure |           |
| MLS01-GCP100 |                 | Level 100  | GCP   |           |

### **MLS02** — Image Recognition Service

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| MLS02-AWS100 |                 | Level 100  | AWS   |           |
| MLS02-AZ100  |                 | Level 100  | Azure |           |
| MLS02-GCP100 |                 | Level 100  | GCP   |           |

### **MLS03** — Text Extraction Service

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| MLS03-AWS100 |                 | Level 100  | AWS   |           |
| MLS03-AZ100  |                 | Level 100  | Azure |           |
| MLS03-GCP100 |                 | Level 100  | GCP   |           |

### **MLS04** — Natural Language Processing Service

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| MLS04-AWS100 |                 | Level 100  | AWS   |           |
| MLS04-AZ100  |                 | Level 100  | Azure |           |
| MLS04-GCP100 |                 | Level 100  | GCP   |           |

## 📱 IOT — Internet of Things

### **IOT01** - Voice-based IOT

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| IOT01-AWS100 |                 | Level 100  | AWS   |           |
| IOT01-AZ100  |                 | Level 100  | Azure |           |
| IOT01-GCP100 |                 | Level 100  | GCP   |           |

## 📦 STR — Cloud Storage

### **STR01** — Data Migration

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| STR01-AWS100 |                 | Level 100  | AWS   |           |
| STR01-AZ100  |                 | Level 100  | Azure |           |
| STR01-GCP100 |                 | Level 100  | GCP   |           |

### **STR02** — Virtual SSD, HDD and Tape Drives

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| STR02-AWS100 |                 | Level 100  | AWS   |           |
| STR02-AZ100  |                 | Level 100  | Azure |           |
| STR02-GCP100 |                 | Level 100  | GCP   |           |

### **STR03** — Shared File Storage Service

| Project Code | Project Details                                                        | Difficulty | CSP   | Author(s)                                        |
| :----------- | :--------------------------------------------------------------------- | :--------- | :---- | :----------------------------------------------- |
| STR03-AWS200 | [Create an EFS shared file system](Projects/STR/STR03/STR03-AWS200.md) | Level 200  | AWS   | [Chris Nagy](https://twitter.com/chris_the_nagy) |
| STR03-AZ100  | [Create a FileShare](Projects/STR/STR03/STR03-AZ100.md)                                    | Level 100  | Azure |   [Gwyneth Peña S.](https://twitter.com/madebygps)                                               |
| STR03-GCP100 |                                                                        | Level 100  | GCP   |                                                  |

### **STR04** — Object Storage

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| STR04-AWS100 |[Create an S3 Bucket and store an object in it](Projects/STR/STR04/STR04-AWS100.md) | Level 100 | AWS | [Syed Auther](https://twitter.com/syedauther) |
| STR04-AZ100  |                 | Level 100  | Azure |           |
| STR04-GCP100 |                 | Level 100  | GCP   |           |

### **STR05** — Data Lakes

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| STR05-AWS100 |                 | Level 100  | AWS   |           |
| STR05-AZ100  |                 | Level 100  | Azure |           |
| STR05-GCP100 |                 | Level 100  | GCP   |           |

## 🗄 DBS — Databases

### **DBS01** — OLAP vs OLTP

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| DBS01-AWS100 |                 | Level 100  | AWS   |           |
| DBS01-AZ100  |                 | Level 100  | Azure |           |
| DBS01-GCP100 |                 | Level 100  | GCP   |           |

### **DBS02** — CAP Theorem

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| DBS02-AWS100 |                 | Level 100  | AWS   |           |
| DBS02-AZ100  |                 | Level 100  | Azure |           |
| DBS02-GCP100 |                 | Level 100  | GCP   |           |

### **DBS03** — Relational Database

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| DBS03-AWS100 | [Create an Amazon RDS DB Instance (MS SQL Server)](Projects/DBS/DBS03/DBS03-AWS100.md) | Level 100 | AWS |[Jagan](https://twitter.com/JAG2wt) |
| DBS03-AWS200 | [Create an Amazon Aurora Database](Projects/DBS/DBS03/DBS03-AWS200.md) | Level 200 | AWS |[Nathan Cho](https://twitter.com/hatchcanon) |
| DBS03-AWS201 | [SQLServer Native Backup and Restore on RDS](Projects/DBS/DBS03/DBS03-AWS201.md)                | Level 200  | AWS   |[Jagan](https://twitter.com/JAG2wt)           |
| DBS03-AZ100  |                 | Level 100  | Azure |           |
| DBS03-GCP100 |                 | Level 100  | GCP   |           |

### **DBS04** — Sharding

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| DBS04-AWS100 |                 | Level 100  | AWS   |           |
| DBS04-AZ100  |                 | Level 100  | Azure |           |
| DBS04-GCP100 |                 | Level 100  | GCP   |           |

### **DBS05** — NoSQL Database

| Project Code | Project Details                                               | Difficulty | CSP   | Author(s)                                        |
| :----------- | :------------------------------------------------------------ | :--------- | :---- | :----------------------------------------------- |
| DBS05-AWS100 | [Create a DynamoDB table](Projects/DBS/DBS05/DBS05-AWS100.md) | Level 100  | AWS   | [Chris Nagy](https://twitter.com/chris_the_nagy) |
| DBS05-AZ100  | [Creating a Microsoft Azure Cosmos Db (SQL API)](Projects/DBS/DBS05/DBS05-AZ100.md) | Level 100  | Azure | [Edward Haigh](https://twitter.com/EddyHaigh)                                                 |
| DBS05-GCP100 |                                                               | Level 100  | GCP   |                                                  |

### **DBS06** — Graph Database

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| DBS06-AWS100 |                 | Level 100  | AWS   |           |
| DBS06-AZ100  |                 | Level 100  | Azure |           |
| DBS06-GCP100 |                 | Level 100  | GCP   |           |

### **DBS07** — Qauntum Database

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| DBS07-AWS100 |                 | Level 100  | AWS   |           |
| DBS07-AZ100  |                 | Level 100  | Azure |           |
| DBS07-GCP100 |                 | Level 100  | GCP   |           |

## 🛠️ DEV — Developer Tools

### **DEV01** - Platform as a Service (Just code and deploy, don't worry about infrastructure)

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| DEV01-AWS100 |                 | Level 100  | AWS   |           |
| DEV01-AZ100  |                 | Level 100  | Azure |           |
| DEV01-GCP100 |                 | Level 100  | GCP   |           |

### **DEV02** - NoCode Service

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| DEV02-AWS100 |                 | Level 100  | AWS   |           |
| DEV02-AZ100  |                 | Level 100  | Azure |           |
| DEV02-GCP100 |                 | Level 100  | GCP   |           |

### **DEV03** - Command Line Interfaces (CLI)

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| DEV03-AWS100 | [Install & Configure AWS CLI then create an S3 Bucket](/Projects/DEV/DEV03/DEV03-AWS100.md)               | Level 100  | AWS   |    [Ariela](https://twitter.com/ari_hacks)       |
| DEV03-AZ100  |                 | Level 100  | Azure |           |
| DEV03-GCP100 |                 | Level 100  | GCP   |           |

### **DEV04** - Software Development Kit (SDK)

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| DEV04-AWS100 |                 | Level 100  | AWS   |           |
| DEV04-AZ100  |                 | Level 100  | Azure |           |
| DEV04-GCP100 |                 | Level 100  | GCP   |           |

## ♻️ OPS — DevOps

### **OPS01** — Infrastructure as Code

| Project Code | Project Details                                                         | Difficulty | CSP   | Author(s)                                        |
| :----------- | :---------------------------------------------------------------------- | :--------- | :---- | :----------------------------------------------- |
| OPS01-AWS100 | [Deploy a CloudFormation template from the AWS Console](Projects/OPS/OPS01/OPS01-AWS100.md) | Level 100 | AWS | [Syed Auther](https://twitter.com/syedauther)<br>[Chris Nagy](https://twitter.com/chris_the_nagy) |
| OPS01-AWS300 | [Deploy a VPC with Terraform](Projects/OPS/OPS01/OPS01-AWS300.md) | Level 300 | AWS | [Markus Mabson ](https://www.linkedin.com/in/markus-mabson-86917a133/) |
| OPS01-AZ100  | [Deploy an ARM template](projects/../Projects/OPS/OPS01/OPS01-AZ100.md) | Level 100  | Azure | [Gwyneth Peña S.](https://twitter.com/madebygps) |
| OPS01-GCP100 |                                                                         | Level 100  | GCP   |                                                  |

### **OPS02** — Build Servers

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| OPS02-AWS100 |                 | Level 100  | AWS   |           |
| OPS02-AZ100  |                 | Level 100  | Azure |           |
| OPS02-GCP100 |                 | Level 100  | GCP   |           |

### **OPS03** — Continuous Deployment

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| OPS03-AWS100 |                 | Level 100  | AWS   |           |
| OPS03-AZ100  |                 | Level 100  | Azure |           |
| OPS03-GCP100 |                 | Level 100  | GCP   |           |

### **OPS04** — Monitoring

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| OPS04-AWS200 | [Create a CloudWatch Alarm ](Projects/OPS/OPS04/OPS04-AWS200.md)           | Level 200  | AWS   |  [Andrew Brown](https://twitter.com/andrewbrown)          |
| OPS04-AZ100  |                 | Level 100  | Azure |           |
| OPS04-GCP100 |                 | Level 100  | GCP   |           |

## BIG — Big Data and Analytics

### **BIG01** — Elastic Map Reduce

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| BIG01-AWS100 |                 | Level 100  | AWS   |           |
| BIG01-AZ100  |                 | Level 100  | Azure |           |
| BIG01-GCP100 |                 | Level 100  | GCP   |           |

### **BIG02** — Data Warehouses

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| BIG02-AWS100 |                 | Level 100  | AWS   |           |
| BIG02-AZ100  |                 | Level 100  | Azure |           |
| BIG02-GCP100 |                 | Level 100  | GCP   |           |

### **BIG03** — Extract, Transform, Load (ETL)

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| BIG03-AWS100 |                 | Level 100  | AWS   |           |
| BIG03-AZ100  |                 | Level 100  | Azure |           |
| BIG03-GCP100 |                 | Level 100  | GCP   |           |

## 👔 GOV — Management and Governance

### **GOV01** — Multi-account strategy

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| GOV01-AWS100 |                 | Level 100  | AWS   |           |
| GOV01-AZ100  |                 | Level 100  | Azure |           |
| GOV01-GCP100 |                 | Level 100  | GCP   |           |

## ☁️ MLT — Multi-Cloud

### **MLT01** — Containers Dataplane running across multiple CSPs

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| MLT01-AWS100 |                 | Level 100  | AWS   |           |
| MLT01-AZ100  |                 | Level 100  | Azure |           |
| MLT01-GCP100 |                 | Level 100  | GCP   |           |

## ☁️ HYR — Hybrid-Cloud

### **HYR01** —

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| HYR01-AWS100 |                 | Level 100  | AWS   |           |
| HYR01-AZ100  |                 | Level 100  | Azure |           |
| HYR01-GCP100 |                 | Level 100  | GCP   |           |

## 🤖 BOT — Robots

### **BOT01** Robot Simulation

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| BOT01-AWS100 |                 | Level 100  | AWS   |           |
| BOT01-AZ100  |                 | Level 100  | Azure |           |
| BOT01-GCP100 |                 | Level 100  | GCP   |           |

### **BOT02** Autonomous Driving Simulation

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| BOT02-AWS100 |                 | Level 100  | AWS   |           |
| BOT02-AZ100  |                 | Level 100  | Azure |           |
| BOT02-GCP100 |                 | Level 100  | GCP   |           |

### **BOT03** Fleet Management

| Project Code | Project Details | Difficulty | CSP   | Author(s) |
| :----------- | :-------------- | :--------- | :---- | :-------- |
| BOT03-AWS100 |                 | Level 100  | AWS   |           |
| BOT03-AZ100  |                 | Level 100  | Azure |           |
| BOT03-GCP100 |                 | Level 100  | GCP   |           |

## **LOW** — Low/No Code

### **LOW** No-Code Apps

| Project Code | Project Details              | Difficulty | CSP   | Author(s) |
| :----------- | :--------------------------- | :--------- | :---- | :-------- |
| LOW01-AWS100 | Create an app with Honeycode | Level 100  | AWS   |           |
| LOW01-AZ100  | Create an app with PowerApps | Level 100  | Azure |           |
| LOW01-GCP100 | Create an app with AppSheet  | Level 100  | GCP   |           |

# 💡 Project Idea Contributors

- Andrew Brown [@andrewbrown](https://twitter.com/andrewbrown)
- Gwyneth Peña S. [@madebygps](https://twitter.com/madebygps)
- Antonio Lo Fiego [@antonio_lofiego](https://twitter.com/antonio_lofiego)
- Syed Auther Abbas [@syedauther](https://twitter.com/syedauther)
- Chris Nagy [@chris_the_nagy](https://twitter.com/chris_the_nagy)
- Johan Rin [@johanrin](https://twitter.com/johanrin)
- Ariela [@ari_hacks](https://twitter.com/ari_hacks)
- Edward Allen Mercado [@edwardmercado_](https://twitter.com/edwardmercado_)
- Jagan [@JAG2wt](https://twitter.com/JAG2wt)
- Nathan Cho [@hatchcanon](https://twitter.com/hatchcanon)
- Contribute a project to see your name added to the list!
