def display(latitude, longitude, speed, gpsTime, gpsdate, st_in, st_use, pdop, mode, altitude, course, history):
    global ndata
    global a
    oled.fill(0)
    if mode == 0:
        oled.text("MODE:1", 0, 0)
        oled.text(latitude, 0, 8)
        oled.text(longitude, 0, 16)
        oled.text(speed, 0, 24)
        oled.text(gpsTime, 0, 32)
        oled.text(gpsdate, 0, 40)
        oled.text('sats:' + str(st_in) + '/' + str(st_use), 0, 48)
        oled.text('pdop:' + str(pdop), 0, 56)
        oled.text('svmd:' + str(savespeed), 72, 56)
    elif mode == 1:
        pass
        #Enter your code
    elif mode == 2:
        oled.text("MODE:3", 0, 0)
        oled.text('at:' + str(altitude) + 'm', 0, 8)
        oled.text('cs:' + str(course) + 'o', 0, 16)
        pi(int(course), 16, 48, 16)
        spag = air530z.speed[0] / 110
        meag = 360 * spag
        pi(int(meag), 50, 48, 16)
    elif mode == 3:
        oled.text("MODE:3", 0, 0)
        oled.pixel(64, 32, 1)
        i = len(history)
        lenlist = len(history)
        now_la = history[lenlist - 1][0]
        now_lo = history[lenlist - 1][1]
        oled.pixel(65, 32, 1)
        oled.pixel(63, 32, 1)
        oled.pixel(64, 32, 1)
        oled.pixel(64, 33, 1)
        oled.pixel(64, 31, 1)
        odx = 64
        ody = 32
        while True:
            i = i - 1
            x = now_la - history[i - 1][0]
            y = now_lo - history[i - 1][1]
            dx = 64 + int(x * 120000)
            dy = 32 + int(y * 120000)
            if x < 0 or 128 > x:
                pass
            if y < 0 or 64 > y:
                pass
            draw_line(odx, ody, dx, dy)
            odx = dx
            ody = dy
            if i == 1:
                break
    oled.show()
