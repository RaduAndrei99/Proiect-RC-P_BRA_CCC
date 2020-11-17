"""
	Clasa folosita pentru a defini un pachet. 
	Format: 24 de octeti
		- primul octet: 0x1 - pachet de initializare
						0x0 - pachet ce contine date

		- urmatorii trei octeti: indexul pachetului (pot fi maxim 16.777.216 de pachete pentru un fisier)
		- ultimii 20 de octeti: 
								daca pachetul este de tip initializare, va contine numele fisierului
								daca pachetul este de tip data, va contine date efective 
"""
class SWPacket:
	def __init__(self, size, data_packet: bool):
		self.__byte_array = bytearray(size)

		if(data_packet):
			self.__byte_array[0] = 0x0
		else:
			self.__byte_array[0] = 0x1

	def get_data(self):
		return self.__byte_array

	def store_data(self, data_array_in_bytes):
		self.__byte_array[4:24] = data_array_in_bytes

	def set_packet_number(self, pk_number):
		if(pk_number < pow(2, 24)):
			self.__byte_array[1:4] = pk_number.to_bytes(3, byteorder="big")