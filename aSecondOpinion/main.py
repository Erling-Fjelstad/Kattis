seconds_input = int(input())

hours = seconds_input // 3600
minutes = (seconds_input - hours * 3600) // 60
seconds = seconds_input - hours * 3600 - minutes * 60

print(f"{hours} : {minutes} : {seconds}")