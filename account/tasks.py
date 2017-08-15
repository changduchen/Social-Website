from celery.decorators import task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@task(name="send_password_reset_email_task")
def send_password_reset_email_task(email_message):
    """sends an email when post form is filled successfully"""
    logger.info("Sent password reset email")
    return email_message.send()
