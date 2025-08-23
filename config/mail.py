"""
Mail/Email configuration settings.
"""

# Default mail driver
default = "smtp"

# Mail drivers configuration
drivers = {
    "smtp": {
        "host": "smtp.gmail.com",
        "port": 587,
        "username": "",
        "password": "",
        "encryption": "tls"
    },
    "sendmail": {
        "path": "/usr/sbin/sendmail -bs"
    },
    "mailgun": {
        "domain": "",
        "secret": "",
        "endpoint": "api.mailgun.net"
    }
}

# Global email settings
from_address = "noreply@example.com"
from_name = "My Application"

# Queue settings for sending emails
queue = {
    "enabled": False,
    "connection": "default"
}