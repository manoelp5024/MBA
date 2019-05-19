import dht
import machine
from time import sleep

d = dht.DHT22(machine.Pin(18))

while True:
  m = d.measure()
  t = d.temperature()
  h = d.humidity()
  
   
   
  if t>=24:
    print("Alta temperatura:",t)
    led.value(1)
  else:
    print("Temperatura ok:")
    led.value(0)
  sleep(1.0)
