# -*- coding: utf-8 -*-

import hmac
# delete binascii after all retyping.
import binascii
import Crypto
import Crypto.Random
from Crypto.Cipher import AES


def gen_sha256_hashed_key_salt(key):

	# Hash 중 SHA256 방식을 사용할 경우 이용할 수 있는 코드 이 경우 import hashlib을 상단에 추가해 줘야 한다.
	#  salt1 = hashlib.sha256(key).digest()
	# print "salt1 len : ", str(len(salt1))
	# return hashlib.sha256(salt1+key).digest()

	# HMAC 을 사용하는 코드.
	# SHA256을 사용하는 HMAC을 생성하고 싶은 경우 hmac.new(key, message, hashlib.sha256)과 같이 코드를 작성하면 된다.

	salt1 = hmac.new(key).digest()
	return salt1


def gen_random_iv():
	return Crypto.Random.OSRNG.posix.new().read(AES.block_size)


# 메시지를 복호화하는 부분.
def AES128_HMAC_Decrypt(key, iv, cipher):
	encryptor = AES.new(gen_sha256_hashed_key_salt(key), AES.MODE_CBC, IV=iv)
	plain = encryptor.decrypt(cipher)
	plain = plain[0:-ord(plain[-1])]

	return plain


def AES128_HMAC_Encrypt(key, plain):
	length = AES.block_size - (len(plain) % AES.block_size)
	plain += chr(length)*length
	iv = gen_random_iv()
	encryptor = AES.new(gen_sha256_hashed_key_salt(key), AES.MODE_CBC, IV=iv)

	return "%s%s" %(binascii.hexlify(iv), binascii.hexlify(encryptor.encrypt(plain)))
