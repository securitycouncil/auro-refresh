#pip install pyautogui to make the code work
import pyautogui
import time 
print("code körs 73 gånger den ska vara uppe i 24 timmar sen starta den om sig själv igen") 
print("börjar om 10 sec")

def auto_start():
	for i in range(5):
	    print("20 min och 10 sec till nästa f5")
	    time.sleep(10)
	    pyautogui.hotkey("f5")
	    print("f5")
		print("click")
		pyautogui.leftClick(x=moveToX, y=moveToY)
	    time.sleep(1200)


while True:
	auto_start()

