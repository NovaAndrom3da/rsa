import random, math, zlib

def newkeys():
  a = random.SystemRandom().randint(2, 9999)
  b = random.SystemRandom().randint(2, 9999)
  a1 = random.SystemRandom().randint(2, 9999)
  b1 = random.SystemRandom().randint(2, 9999)
  M = (a * b) - 1
  e = (a1 * M) + a
  d = (b1 * M) + b
  n = ((e * d) - 1) / M

  pub = f"{str(int(n))},{str(int(e))}"
  priv = f"{str(int(n))},{str(int(d))}"

  print(pub)
  print(priv)
  
  pub_chars = ""
  for i in pub:
    pub_chars += str(ord(i))+"-"

  priv_chars = ""
  for i in priv:
    priv_chars += str(ord(i))+"-"

  priv_out = priv_chars.rstrip("-")
  pub_out = pub_chars.rstrip("-")
  
  return priv_out, pub_out

priv, pub = newkeys()

def get_key(key):
  out = ""
  for i in key.split("-"):
    out += chr(int(i))

  out = out.split(",")
  return (int(out[0]), int(out[1]))


def encode(pub, msg=""):
  pub = get_key(pub)
  to_char = list(msg)
  out = ""
  for char in to_char:
    out += str(int((pub[1] * ord(char)) % pub[0])) + ";"
  return out.rstrip(';')
  #return zlib.compress(out.rstrip(";").encode("utf-32"), level=9)

def decode(priv, msg=""):
  priv = get_key(priv)
  #charslist = zlib.decompress(msg).decode("utf-32").split(";")
  charslist = msg.split(';')
  out = ""
  
  for char in charslist:
    out += chr(int((int(char) * priv[1]) % priv[0]))

  return out