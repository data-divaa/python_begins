'''
Date - 7-july-2024
Authur - Data -Divaa
question -
        show current date and time
'''



from datetime import datetime
date_time = datetime.now()
new = date_time.strftime("%d-%m-%Y" " " "%H:%M")
print("current date and time ", new)
