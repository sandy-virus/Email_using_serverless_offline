# 📧 Serverless Email API (Python + Gmail SMTP + Offline Support)

A simple **Serverless Framework (Python)** project that provides a REST API to send emails using **Gmail SMTP**.

It supports:
- Local development with **serverless-offline**
- Environment variables via **.env**
- Error handling with proper HTTP responses
- Secure secret management (using `.env` locally or AWS Secrets Manager in production)

---

## 🚀 Features

✅ REST API endpoint `/send`  
✅ Input validation (`receiver_email`, `subject`, `body_text`)  
✅ Uses **Gmail SMTP (smtplib)** for real email sending  
✅ Works fully **offline** for development (via `serverless-offline`)  
✅ Ready for AWS deployment (Lambda + API Gateway)

---

## 🧩 Tech Stack

| Component | Tool |
|------------|------|
| Language | Python 3.12 |
| Framework | Serverless Framework |
| Email | Gmail SMTP |
| Local Testing | serverless-offline |
| Validation | email-validator |

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/serverless-email-api.git
cd serverless-email-api


