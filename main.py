import azure.cognitiveservices.speech as speechsdk
import os
import requests

def recognize_from_mic():
    while True: 

	    #Find your key and resource region under the 'Keys and Endpoint' tab in your Speech resource in Azure Portal
	    #Remember to delete the brackets <> when pasting your key and region!
        speech_config = speechsdk.SpeechConfig(subscription="key", region="region")
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

        #Asks user for mic input and prints transcription result on screen
        print("Awaiting input...")
        result = speech_recognizer.recognize_once_async().get()
        print(str(result.text).lower())
        #trigger words
        left = "look left"
        bleft = "big left"
        right = "look right"
        bright = "big right"
        up = "look up"
        down = "look down"
        shoot = "shoot"
        jump = "jump"
        exit = "exit"
        crouch = "crouch"
        spray = "spray"
        ads = "aim down sights"
        sads = "stop, aim down sights"
        prone = "prone"
        wforward = "walk forwards"
        wbackward = "walk backwards"
        wleft = "walk left"
        wright = "walk right"
        stop = "stop"
        loot = "loot"
        sprint = "sprint"
        reload = "reload"
        action = "action"
        

        if (left in str(result.text).lower()):
            requests.get("http://192.168.1.9/pythonproject/leftlittle/Mouse%20Moving%20App.exe")
        elif(right in str(result.text).lower()):
            requests.get("http://192.168.1.9/pythonproject/rightlittle/Mouse%20Moving%20App.exe")
        elif(up in str(result.text).lower()):
            requests.get("http://192.168.1.9/pythonproject/upl/Mouse%20Moving%20App.exe")
        elif(down in str(result.text).lower()):
            requests.get("http://192.168.1.9/pythonproject/downlittle/Mouse%20Moving%20App.exe")
        elif(shoot in str(result.text).lower()):
            requests.get("http://192.168.1.9/pythonproject/shoot/Mouse%20Moving%20App.exe")
        elif(loot in str(result.text).lower()):
            requests.get("http://192.168.1.9/pythonproject/loot/Mouse%20Moving%20App.exe")
        elif(exit in str(result.text).lower()):
            requests.get("http://192.168.1.9/pythonproject/exit/Mouse%20Moving%20App.exe")
        elif(crouch in str(result.text).lower()):
            requests.get("http://192.168.1.9/pythonproject/crouch/crouch.py")
        elif(spray in str(result.text).lower()):
            requests.get("http://192.168.1.9/pythonproject/spray/spray.py")
        elif(ads in str(result.text).lower()):
            requests.get("http://192.168.1.9/pythonproject/ads/Mouse%20Moving%20App.exe")
        elif(sads in str(result.text).lower() or "stop, aim down sights." in str(result.text).lower()):
            requests.get("http://192.168.1.9/pythonproject/stopads/Mouse%20Moving%20App.exe")
        elif(prone in str(result.text).lower()):
            requests.get("http://192.168.1.9/pythonproject/prone/prone.py")
        elif(sprint in str(result.text).lower()):
            requests.get("http://192.168.1.9/pythonproject/sprint/spint.py")
        elif(wforward in str(result.text).lower()):
            requests.get("http://192.168.1.9/pythonproject/walkforward/w.py")
        elif(wbackward in str(result.text).lower()):
            requests.get("http://192.168.1.9/pythonproject/walkbackward/S.py")
        elif(wleft in str(result.text).lower()):
            requests.get("http://192.168.1.9/pythonproject/walkleft/a.py")
        elif(wright in str(result.text).lower()):
            requests.get("http://192.168.1.9/pythonproject/walkright/d.py")
        elif(stop in str(result.text).lower()):
            requests.get("http://192.168.1.9/pythonproject/stop/stop.py")
        elif(jump in str(result.text).lower()):
            requests.get("http://192.168.1.9/pythonproject/jump/Mouse%20Moving%20App.exe")
        elif (bright in str(result.text).lower()):
            requests.get("http://192.168.1.9/pythonproject/bigright/letstryitagain.exe")
        elif (bleft in str(result.text).lower()):
            requests.get("http://192.168.1.9/pythonproject/bigleft/letstryitagain.exe")
        elif (reload in str(result.text).lower()):
            requests.get("http://192.168.1.9/pythonproject/reload/reload.py")
        elif (action in str(result.text).lower()):
            requests.get("http://192.168.1.9/pythonproject/action/action.py")              
        elif ("stop application" in str(result.text).lower() or "end application" in str(result.text).lower()):
            exit()

    

recognize_from_mic()
