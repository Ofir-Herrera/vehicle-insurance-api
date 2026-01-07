# 🚗 **Vehicle Insurance API – Insait Assignment**

Backend API for retrieving vehicle information and calculating vehicle market values.  
Designed as part of the **Insait insurance onboarding flow**.

---

## 🚀 **How to Run the Project**

### 🐳 **Option 1: Using Docker (Recommended)**

The easiest way to run the application with all dependencies pre-configured.

**1. Build the Docker image**

    docker build -t vehicle-app .

**2. Run the container**

    docker run -p 8000:8000 vehicle-app

**3. Test the API**

    http://127.0.0.1:8000/docs

---

### 💻 **Option 2: Running Locally (Manual)**

**1. Install dependencies**

    pip install -r requirements.txt

**2. Start the development server**

    uvicorn main:app --reload

**3. Access the API**

    http://127.0.0.1:8000/docs

---

## 💰 **Vehicle Value Calculation**

The vehicle market value is calculated using **linear depreciation** based on vehicle age.

### 📐 **Formula**

    value = max(0,BASE_VALUE - (age * DEPRECIATION_PER_YEAR))

### 🧠 **Explanation**
- A fixed amount is subtracted from the base value each year.
- The depreciation rate remains constant over time.
- Simple, transparent, and predictable valuation model.

---

## ☁️ **Deployment Process (Google Cloud Run)**

The API is deployed as a **serverless service** using **Google Cloud Run**.

### 🔧 **Deployment Steps**
- **Containerization:** Packaging the FastAPI application using Docker.
- **Artifact Registry:** Pushing the Docker image to Google Cloud’s private registry.
- **Service Deployment:** Deploying the container to Cloud Run.
- **CORS Configuration:** Enabling cross-origin requests from the Insait platform.

---
## 🔒 API Security & Authentication

To ensure the API is secured and only accessible by authorized clients (like our Insait AI Agent), I have implemented a **Header-based Authentication** mechanism.

### How it works:
- The endpoint `/vehicle-info` requires an `Authorization` header.
- The system validates a **Bearer Token** to grant access.
- Any request without a valid token will receive a `401 Unauthorized` response.

### Usage in Insait / Swagger:
- **Header Key:** `Authorization`
- **Header Value:** `Bearer mysecrettoken123`

> **Note:** For development purposes, the token validation is case-insensitive to ensure robust integration across different platforms.
--- 
## 🤖 **AI Usage & Development Process**

AI tools were used as **supporting development aids**, not as code authors.

### 🧠 **Use of Gemini**
- **Gemini** was used for code review, and validation of implementation ideas.
- Supported debugging, documentation wording, and deployment troubleshooting.
- All core logic, final code, and design decisions were implemented and reviewed by the developer.

---

## 🧰 **Tech Stack**

- **Language:** Python 3.11
- **Framework:** FastAPI
- **Validation:** Pydantic
- **Containerization:** Docker
- **Cloud Platform:** Google Cloud Run
