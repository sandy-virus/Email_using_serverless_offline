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

### Install dependencies

#### 🐍 Python packages:
```bash
pip install -r requirements.txt 
```
#### 🧱 Node.js packages:
```bash
 npm install
```
Installation
------------

First, add Serverless Offline to your project:
```bash
npm install serverless-offline --save-dev   
```
Then inside your project's serverless.yml file add following entry to the plugins section: serverless-offline. If there is no plugin section you will need to add it to the file.

**Note that the "plugin" section for serverless-offline must be at root level on serverless.yml.**

[Usage and command line options](https://www.serverless.com/plugins/serverless-offline#usage-and-command-line-options)
----------------------------------------------------------------------------------------------------------------------

In your project root run:

**serverless offline** or **sls offline**.

### Configure .env

Create a .env file in your project root:
```bash
SENDER_EMAIL=your@gmail.com
SMTP_PASSWORD=your_app_password   # Use Gmail App Password (not your main password)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=your smtp port   `
```
> ⚠️ Add .env to your .gitignore to avoid exposing secrets.

To generate an **App Password**:

*   Go to your Google Account → **Security → App passwords**
    
*   Create one for "Mail" + "Other (Custom name)"
    
*   Copy the 16-character password here.
    

Run locally (serverless-offline)

Start the API:
```bash
sls offline
```
Now open your terminal or Postman and test:
```bash
curl -X POST http://localhost:3000/dev/send \
    -H "Content-Type: application/json" \
-d '{"receiver_email": "recipient@example.com", "subject": "Test Email", "body_text": "Hello from Serverless Offline!"    }'   
```
✅ You’ll get a JSON response:
```bash
 { "message": "Email sent"  }   
```
and a real email will be delivered.

🌐 API Details
--------------

**Endpoint:**POST /send

**Request Body:**
```bash
{"receiver_email": "recipient@example.com", "subject": "Subject line", "body_text": "Email message body"  }  
```
**Responses:**

Example:

200Success{ "message": "Email sent" }

400Bad Request{ "error": "Invalid JSON or missing fields" }

401Auth Error{ "error": "SMTP authentication failed" }

502SMTP Error{ "error": "SMTP service error" }

500Internal Error{ "error": "Internal server error" }

🧠 Folder Structure
-------------------
```bash
serverless-email-api/
│
├── handler.py                # Lambda function logic
├── requirements.txt          # Python dependencies
├── serverless.yml            # Serverless config (API, env, plugins)
├── package.json              # Node dev dependencies
├── .env                      # Local secrets (ignored by git)
└── README.md                 # Project documentation
```

⚠️ Notes
--------

*   Gmail blocks “less secure apps”. Always use an **App Password**.
    
*   Gmail has a daily send limit (~500 mails/day for personal accounts).
    
*   For large scale or transactional use, consider **SendGrid**, **Mailgun**, or **AWS SES**.
    
*   Never commit .env or plaintext secrets to GitHub.
    
*   Use HTTPS in production.
    

🪪 License
----------

This project is licensed under the **MIT License** — free to use and modify.

### ⭐ If you found this useful, give it a star on GitHub!
