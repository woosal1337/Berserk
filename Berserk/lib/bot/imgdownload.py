from urllib.request import urlretrieve

def downloadImg(url):
	urlretrieve(url, r"D:\GitHub\Berserk\Berserk\qrcodedec\image.png")