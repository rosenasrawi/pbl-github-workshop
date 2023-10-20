from datetime import datetime

time = int(datetime.now().strftime('%H'))

if time > 9 and time < 17:
    print('Hello, world!')
else:
    print('Goodbye, world!')