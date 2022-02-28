#pip install pyautogui to make the code work
import pyautogui
import time 
print("code körs 73 gånger den ska vara uppe i 24 timmar sen starta den om sig själv igen") 
print("börjar om 10 sec")

def auto_start():
	for i in range(5):
	    print("20 min och 10 sec till nästa f5")
		print("click")
		pyautogui.leftClick(x=moveToX, y=moveToY)# moveToX ska du ändra med x positionen för datormusen och moveToY ska du ändra med y positionen för datormusen
	    time.sleep(10)
	    pyautogui.hotkey("f5")
	    print("f5")
		time.sleep(45)
		print("click")
		pyautogui.leftClick(x=moveToX, y=moveToY)# moveToX ska du ändra med x positionen för datormusen och moveToY ska du ändra med y positionen för datormusen
	    time.sleep(2100)
	    print("5 min till nästa click/refresh")
	    time.sleep(2400)


while True:
	auto_start()
