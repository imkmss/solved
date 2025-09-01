from datetime import datetime, timedelta, timezone

utc_now = datetime.now(timezone.utc)
seoul_now = utc_now + timedelta(hours=9)

print(seoul_now.strftime("%Y-%m-%d"))