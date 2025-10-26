### Install dependencies

#### 🐍 Python packages:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pip install -r requirements.txt   `

#### 🧱 Node.js packages:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   npm install   `

Installation
------------

First, add Serverless Offline to your project:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   npm install serverless-offline --save-dev   `

Then inside your project's serverless.yml file add following entry to the plugins section: serverless-offline. If there is no plugin section you will need to add it to the file.

**Note that the "plugin" section for serverless-offline must be at root level on serverless.yml.**

[Usage and command line options](https://www.serverless.com/plugins/serverless-offline#usage-and-command-line-options)
----------------------------------------------------------------------------------------------------------------------

In your project root run:

serverless offline or sls offline.

### Configure .env

Create a .env file in your project root:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   SENDER_EMAIL=your@gmail.com  SMTP_PASSWORD=your_app_password   # Use Gmail App Password (not your main password)  SMTP_HOST=smtp.gmail.com  SMTP_PORT=your smtp port   `

> ⚠️ Add .env to your .gitignore to avoid exposing secrets.

To generate an **App Password**:

*   Go to your Google Account → **Security → App passwords**
    
*   Create one for "Mail" + "Other (Custom name)"
    
*   Copy the 16-character password here.
    

Run locally (serverless-offline)

Start the API:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   sls offline   `

Now open your terminal or Postman and test:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   curl -X POST http://localhost:3000/dev/send \    -H "Content-Type: application/json" \    -d '{      "receiver_email": "recipient@example.com",      "subject": "Test Email",      "body_text": "Hello from Serverless Offline!"    }'   `

✅ You’ll get a JSON response:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   {    "message": "Email sent"  }   `

and a real email will be delivered.

🌐 API Details
--------------

**Endpoint:**POST /send

**Request Body:**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   {    "receiver_email": "recipient@example.com",    "subject": "Subject line",    "body_text": "Email message body"  }   `

**Responses:**

Example:

200Success{ "message": "Email sent" }

400Bad Request{ "error": "Invalid JSON or missing fields" }

401Auth Error{ "error": "SMTP authentication failed" }

502SMTP Error{ "error": "SMTP service error" }

500Internal Error{ "error": "Internal server error" }

🧠 Folder Structure
-------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   serverless-email-api/  │  ├── handler.py                # Lambda function logic  ├── requirements.txt          # Python dependencies  ├── serverless.yml            # Serverless Framework config  ├── package.json              # Node dev dependencies (offline + dotenv)  ├── .env                      # Local secrets (ignored in git)  └── README.md                 # Project documentation   `

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