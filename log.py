path = "/gps.txt" ###full path
savespeed = 10 #defalt
def wr(data):
    #led.value(1) confirm
    with open(path, 'a') as f:
        f.write(str(data) + '\n')
    #led.value(0)
while True:
  if time.time() - ti >= savespeed:
    wr(temp)
    ti = time.time()
