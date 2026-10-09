# Ultimate DevOps Project

An end-to-end DevOps learning project focused on containerization, CI/CD automation, container image publishing, Kubernetes deployment, and monitoring.

## Overview

This project demonstrates a practical DevOps workflow that automates the journey from application source code to containerized deployment and monitoring.

The goal is to understand how modern DevOps tools work together to build, test, package, deploy, and monitor applications.

## Architecture

```text
Developer
    |
    v
GitHub Repository
    |
    v
GitHub Actions (CI/CD)
    |
    v
Docker Build
    |
    v
Docker Hub
    |
    v
Kubernetes Deployment
    |
    v
Prometheus + Grafana
```

## Tech Stack

* **Version Control:** Git, GitHub
* **CI/CD:** GitHub Actions
* **Containerization:** Docker
* **Container Registry:** Docker Hub
* **Orchestration:** Kubernetes, Minikube
* **Infrastructure as Code:** Terraform
* **Monitoring:** Prometheus, Grafana

## Key Learning Objectives

* Build and package applications using Docker.
* Automate build and test workflows with GitHub Actions.
* Publish container images to Docker Hub.
* Deploy and manage containerized applications in Kubernetes.
* Explore infrastructure provisioning using Terraform.
* Understand application monitoring and observability with Prometheus and Grafana.

## Project Structure

The repository contains the application code, Docker configuration, CI/CD workflow definitions, and infrastructure-related files.

Refer to the repository directories for the implementation of each component.

## Run Locally

### Prerequisites

Install Git, Docker, kubectl, and Minikube.

### Clone the repository

```bash
git clone https://github.com/gayatrri024/ultimate-devops-project.git
cd ultimate-devops-project
```

Follow the instructions in the relevant project directories to build, run, and deploy the application.

## What I Learned

* Containerizing applications and managing image versions.
* Automating software delivery pipelines.
* Deploying workloads on Kubernetes.
* Understanding infrastructure automation and monitoring.
* Troubleshooting integration issues across the DevOps toolchain.

## Future Improvements

* Implement automated security and image scanning.
* Improve Kubernetes deployment automation.
* Add infrastructure provisioning and validation.
* Configure dashboards and application health monitoring.

## Author

**Gayatri Shinde**

* GitHub: [@gayatrri024](https://github.com/gayatrri024)
* Portfolio: [gayatrishinde-portfolio.vercel.app](https://gayatrishinde-portfolio.vercel.app)

---

*This project is part of my hands-on journey toward becoming a DevOps and Infrastructure as Code Engineer.*
