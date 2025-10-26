import json
import smtplib
import os
from dotenv import load_dotenv
from email_validator import validate_email

# load .env if present
load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
PASS = os.getenv("PASS")
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT"))


def send_email(event, context=None):     
    # parse data from event
    try:
        payload = json.loads(event.get('body', {}))
        print("check:", payload)
        
    except json.JSONDecodeError:
        return {"statusCode": 400, 
                "body": json.dumps({"error": "Invalid JSON in request body"}) }
        
    # validate the payload
    is_valid = validate_payload(payload)
    print("after validate",type(is_valid), is_valid)
    
    # if get a list from validate_payload which shows missing data
    if isinstance(is_valid, list):
            print("checking:", is_valid)
            return {"statusCode": 400, 
                "body": json.dumps({"error": f"{is_valid} not provided"}) }
    
    # If get boolean 
    if not is_valid:
        print(500)
        return {"statusCode": 400, 
                "body": json.dumps({"error": "Invalid email"}) }
    
    # ectract data drom validaed payload
    RECV_EMAIL = payload.get('receiver_email')
    subject = payload.get("subject")
    body = payload.get("body_text")
    
    try:
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT, timeout=10) as smtp:
            smtp.ehlo()
            smtp.starttls()   # Secure the connection
            smtp.ehlo()
            
            smtp.login(SENDER_EMAIL, PASS)  # login using app passwords
            
            # subject  = 'serverless-testing'
            # body = 'hello from python'
            
            msg = f'Subject: {subject}\n\n{body}'
            smtp.sendmail(from_addr=SENDER_EMAIL, to_addrs= RECV_EMAIL, msg= msg)
        
        body = {
            "message": "Email sent successfully!"
        }

        return {"statusCode": 200, "body": json.dumps(body)}
    except Exception as e:
        # Print any error messages
        print(e)

## this function is used to validate email and missing data
def validate_payload(payload):
    
    # find missing data from the payload
    missing = [missed_data for missed_data in ("receiver_email", "subject", "body_text") if not payload.get(missed_data)]
    
    if missing:
        return missing
    
    # validate email and domain name
    try:
        v = validate_email(payload["receiver_email"], check_deliverability=True)
        payload["receiver_email"] = v.email
        
    except Exception as e:
        print("exception in validate_payload:", e)
        return False
    
    return True




# --------------------just for testing without serverless------------------------------------------
# api_event = {"body": json.dumps({
#         "receiver_email": "selinamuskan1@gmail.com",
#         "subject": "hello",
#         "body_text": "hi from test"
#     })}
 
# print("start")
# send_email(api_event)
# print("end")
