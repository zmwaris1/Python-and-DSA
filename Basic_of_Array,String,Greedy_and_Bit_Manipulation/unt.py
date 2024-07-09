import datetime
from dateutil.relativedelta import relativedelta

def get_date_and_duration_from_timestamp(start_date_str, end_date_str):
    """
    :param start_date:
    :param end_date:
    :return:
    """
    start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d %H:%M:%S")
    end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d %H:%M:%S")
    delta = end_date.day - start_date.day
    print("Delta",delta)
    pause_data = []
    for i in range(delta + 1):
        day = start_date + relativedelta(days=i)
        print("Day",day)
        start_of_day = max(day.replace(hour=0, minute=0, second=0), start_date)
        print("SOD",start_of_day)
        end_of_day = min(day.replace(hour=23, minute=59, second=59), end_date)
        print("EOD",end_of_day)
        pause_duration = end_of_day - start_of_day
        pause_result = {
            "pause_date": day.strftime("%Y-%m-%d"),
            "pause_tracking_duration": pause_duration.total_seconds(),
        }
        pause_data.append(pause_result)
    return pause_data

# print(