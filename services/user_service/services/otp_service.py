import os
import random
import smtplib

from email.message import EmailMessage
from fastapi import HTTPException


EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
EMAIL_USERNAME = os.getenv("EMAIL_USERNAME")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_FROM = os.getenv("EMAIL_FROM")


class OTPService:

    @staticmethod
    def generate_otp():
        return str(random.randint(100000, 999999))

    @staticmethod
    def send_email_otp(email: str, otp: str):

        try:
            message = EmailMessage()

            message["Subject"] = "Your E-Commerce Verification OTP"
            message["From"] = EMAIL_FROM
            message["To"] = email

            message.set_content(
                f"""
Hello,

Your OTP for Scalable E-Commerce registration is:

{otp}

This OTP is valid for 5 minutes.

If you did not request this OTP, please ignore this email.

Regards,
Scalable E-Commerce Team
"""
            )

            with smtplib.SMTP(
                EMAIL_HOST,
                EMAIL_PORT
            ) as server:

                server.starttls()

                server.login(
                    EMAIL_USERNAME,
                    EMAIL_PASSWORD
                )

                server.send_message(message)

            return {
                "message": "OTP sent successfully"
            }

        except Exception as e:

            raise HTTPException(
                status_code=500,
                detail=f"Unable to send email OTP: {str(e)}"
            )