import requests
import random
import string
import urllib.request
# image.png is the new that you will give the image when you save it
def get_random_string(length, str_for_search):
       
    result_str = ''.join(random.choice(str_for_search) for i in range(length))
    return (result_str)

with open('image.png', 'wb') as handle:
        # pic_url is the link of the image

    
  string.ascii_letters
  '0a1b2c3d4e5f6g78h9ijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  request = get_random_string(6, string.ascii_letters)
  url = 'https://prnt.sc/'+request
  print("url: {}".format(url))
  response = requests.get(url, stream=True)
  while(response.status_code == 520):
    request = get_random_string(6, string.ascii_letters)
    while(response.status_code == 200):
          print (1)
    while(response.status_code == 200):
          urllib.request.urlretrieve(request, "00000001.jpg")

    url = 'https://prnt.sc/'+request
    print("url: {}".format(url))
    response = requests.get(url, stream=True)
  print(response.text)
  if not response.ok:
    print ("reposnse: {}".format(response))

  for block in response.iter_content(1024):
              if not block:
                  break
              # if there is no error write the image to image.png
              handle.write(block)

