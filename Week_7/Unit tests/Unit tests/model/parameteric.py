from datetime import datetime

def weekday_or_weekend(cob: str) -> str:
    cob = datetime.strptime(cob, "%Y-%m-%d")
    day_from_weeek = cob.weekday()

    if day_from_weeek < 5:
        return 'Weekday'
    else:
        return 'Weekend'
