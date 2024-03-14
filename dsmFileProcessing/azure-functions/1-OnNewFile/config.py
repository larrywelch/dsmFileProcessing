import os

settings = {
    'email-notification-enabled' : os.environ.get('email_notification_enabled', True),
    'email-notification-svc-conn-str': os.environ.get('email_notification_svc_conn_str', 'endpoint=https://dsm-agristats-eval-comm-svc.unitedstates.communication.azure.com/;accesskey=wDWYB7Hhr6aWj5BU9bYy524ke14/p9FQtJLTmtia3zU3Ap2/4Yq4k6aeITfG8etS26cu87/CJ1tPwajLnfoo9g=='),
    'email-notification-send-to-list' : os.environ.get('email_notification_send_to_list', 'larry.welch@foundationtek.com'),
    'email-notification-poller-wait-time': os.environ.get('email_notification_poller_wait_time', 10),
    'email-notification-sender-address' : os.environ.get('email_notification_sender_address', 'dsm-agristats-eval@b273432d-8546-476e-a780-0cde12323090.azurecomm.net')
}