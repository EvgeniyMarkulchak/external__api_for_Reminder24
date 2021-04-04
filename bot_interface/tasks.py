import datetime

from user_profile.models import SheduledMessage


def clear_stale_records():
    # python run.py bot_interface.tasks "clear_stale_records()"
    now_minus_day = datetime.datetime.now() - datetime.timedelta(days=1)
    SheduledMessage.objects.filter(schedule_time__lte=now_minus_day).delete()
