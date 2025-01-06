from machine import Pin, UART
if rp2.bootsel_button() == 1:
      mode = mode + 1
      while rp2.bootsel_button() == 1:
          pass
      if mode == 4:
          mode = 0
