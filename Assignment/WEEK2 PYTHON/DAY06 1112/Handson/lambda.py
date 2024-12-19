is_event_list = [lambda arg=x: arg*10 for x in range(1,4)]
for item in is_event_list:
 print(item())