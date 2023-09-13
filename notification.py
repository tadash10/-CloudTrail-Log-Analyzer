
# cloudtrail_log_analyzer/notification.py

import boto3
import json

def send_alert(event_data, channels=['sns']):
    # Initialize notification clients
    sns_client = boto3.client('sns')
    slack_client = None  # Initialize Slack client if needed (uncomment and set up)

    # Prepare alert message with event data
    alert_message = json.dumps(event_data, indent=2)

    # Send alerts to specified channels
    for channel in channels:
        if channel == 'sns':
            sns_client.publish(
                TopicArn='your-sns-topic-arn',
                Subject='Suspicious Activity Detected',
                Message=alert_message
            )
        elif channel == 'slack' and slack_client:
            # Send to Slack channel here (add your Slack integration logic)

    # Return True if at least one notification channel was successful
    return True
