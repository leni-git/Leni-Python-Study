# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import json

class Paho_Mqtt() :

	def mosquitto_start(self, topic, new_movie) :

		mqttc = mqtt.Client("python_pub") # MQTT client object creat
		mqttc.connect("test.mosquitto.org", 1883) # MQTT server connect
		# Jason 형식으로 message 전달하기.
		print "'"+new_movie.get_movie_name()+"'"
		print "'"+str(new_movie.get_movie_times())+"'"
		print "'"+str(new_movie.get_movie_room())+"'"

		message = { 'name' : new_movie.get_movie_name(), 'times' : str(new_movie.get_movie_times()), 'room' : str(new_movie.get_movie_room()) }

		json_message = json.dumps(message)
		mqttc.publish(topic, json_message) # message send
		#mqttc.loop(2) # timeout = 2 seconds


# mqttc = mqtt.Client("python_pub") # MQTT client object creat
# mqttc.connect("test.mosquitto.org", 1883) # MQTT server connect
# mqttc.publish("ad/yes", "hello world!!!!!!!!!!!!!!!!!!!!!!!!!!!!") # message send
#mqttc.loop(2) # timeout = 2 seconds