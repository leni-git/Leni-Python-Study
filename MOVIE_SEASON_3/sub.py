# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import threading
import time, os
import json

class Paho_Mqtt() :

	__topic = None

	# 클라이언트가 서버에게서 Connect 응답을 받을 때 호출 되는 콜백.
	def on_connect(self, client, userdata, flags, rc) :
		#print "Connected with result cod", str(rc)
		client.subscribe(self.__topic)

	# 서버에게서 publish 메시지를 받을 때 호출 되는 콜백.
	def on_message(self, client, userdata, msg) :
		# 동작을 구현해야 한다.
		#print "\n", msg.topic, " ", str(msg.payload)
		movie = json.loads(msg.payload)

		html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>hi, I am LENI</title>

    <style type="text/css">
    body { margin-left: 0px; margin-top: 0px; margin-right: 0px; margin-bottom: 0px; }

    #center { position:absolute; top:50%; left:50%; width:50%; height:200px;
        overflow:hidden; margin-top:-150px; margin-left:-5px;}
    </style>
</head>
<body>
    <div id="center">
        <p><span style="color: #ff0e36; font-size: 35px">♡</span>"""+movie['name'].decode('utf-8').encode('ascii')+"""<span style="color: #ff0e36; font-size: 35px">♡</span></p>
        <p>"""+str(movie['times']).decode('utf-8').encode('ascii')+"""</p><p>YOU CAN SEE ALL FILE ON <b><a href="https://github.com/poppy-Leni/DoitCode" target=_blank" style="color: #27c057">
            GIT-HUB</a></b> "</p>
        <p>" AND ALSO YOU CAN READ SOME INFORMATION ONLINE
            <b><a href="http://poppy-leni.tistory.com/" target=_blank" style="color: #fa11b3">LENI-TISTORY</a></b> "</p>
    </div>
</body>
</html>"""

		with open("documents/NEW_MOVIE.html", "w") as f : 
			f.write(html)

		os.system("chrome documents/NEW_MOVIE.html")

	#broker로 부터 메시지 받음.
	def mosquitto_start(self, client_topic, interval = 1) :
		#client = mqtt.Client("", True, None, mqtt.MQTTv31) # MQTT client object creat

		self.interval = interval
		self.__topic = client_topic

		thread = threading.Thread(target=self.run, args=())
		thread.daemon = True
		print "start Thread"
		thread.start()

	def run(self) :
		while  True :
			client = mqtt.Client()
			client.on_connect = self.on_connect
			client.on_message =  self.on_message # on_message callback set

			client.connect("test.mosquitto.org", 1883, 60) # MQTT server connect

			time.sleep(self.interval)
			client.loop_forever()

	 # 네트워크 트래픽을 처리, 콜백 디스패치, 재접속 등을 수행하는 블러킹 함수.
	 # 멀티스레드 인터페이스나 수동 인터페이스를 위한 다른 loop* () 함수도 있음.
	 #client.loop_forever(100)
