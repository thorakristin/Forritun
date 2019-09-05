secs_str = input("Input seconds: ")

secs_int = int(secs_str)

hours = secs_int // 3600
hours_rest = secs_int % 3600

minutes = hours_rest // 60
minutes_rest = hours_rest % 60

seconds = minutes_rest

print(hours,":",minutes,":",seconds)
