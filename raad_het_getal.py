import os, sys, io
import M5
from M5 import *
import m5ui
import lvgl as lv
from hardware import Rotary



page0 = None
MAX_GETAL = None
lblGok = None
lblHint = None
rotary = None


import random

gok = None
geheim = None


def setup():
  global page0, lblGok, lblHint, rotary, gok, geheim, pogingen

  M5.begin()
  Widgets.setRotation(0)
  m5ui.init()
  page0 = m5ui.M5Page(bg_c=0xffffff)
  lblGok = m5ui.M5Label("0", x=103, y=89, text_c=0x000000, bg_c=0xffffff, bg_opa=0, font=lv.font_montserrat_48, parent=page0)   # Bij start-up begint je teller op 0
  lblHint = m5ui.M5Label("Draai en druk", x=57, y=154, text_c=0x000000, bg_c=0xffffff, bg_opa=0, font=lv.font_montserrat_18, parent=page0) # Voor de eerste gok, staat de instructie 'draai en druk'

  rotary = Rotary()
  MAX_GETAL = 50
  geheim = random.randint(1, MAX_GETAL)  #Het apparaat kiest een willekeurig getal tussen 1 en 50
  pogingen = 0
  page0.screen_load()
  
  print(f"Geheim: {geheim}")


def loop():
  global page0, lblGok, lblHint, rotary, gok, geheim, pogingen
  M5.update()
  gok = rotary.get_rotary_value()
  lblGok.set_text(str(gok))
  if gok < 1:
    gok = 1
  elif gok > MAX_GETAL:
    gok = MAX_GETAL
  else:
    if BtnA.wasClicked():
      pogingen = pogingen + 1
      print(f"Gok: {gok} en Geheim: {geheim}")
      print(f"Poging: {pogingen}")
      if gok < geheim:
        lblHint.set_text(str('Hoger!'))
      elif gok > geheim:
        lblHint.set_text(str('Lager!'))
      else:
        lblHint.set_text(str('Geraden!'))
        Speaker.tone(5000, 500)
      pogingen = pogingen + 1


if __name__ == '__main__':
  try:
    setup()
    while True:
      loop()
  except (Exception, KeyboardInterrupt) as e:
    try:
      m5ui.deinit()
      from utility import print_error_msg
      print_error_msg(e)
    except ImportError:
      print("please update to latest firmware")
