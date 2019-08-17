import sys

try:
    import PIL
    from PIL import Image
except ImportError:
    sys.exit("""You need PIL!
                install it from http://pypi.python.org/pypi/Pillow
                or run pip install Pillow.""")

def exec(dif, mask, normal, spec):
    wMax = max(dif.width, mask.width, normal.width, spec.width)
    hMax = max(dif.height, mask.height, normal.height, spec.height)

    #do something
    print(str(wMax) + "/" + str(hMax))

d = Image.open("./samples/WEP_1P_MAC10_TEX/Texture2D/Wep_1stP_Mac10_D.tga")
m = Image.open("./samples/WEP_1P_MAC10_TEX/Texture2D/Wep_1stP_Mac10_M.tga")
n = Image.open("./samples/WEP_1P_MAC10_TEX/Texture2D/Wep_1stP_Mac10_N.tga")
s = Image.open("./samples/WEP_1P_MAC10_TEX/Texture2D/Wep_1stP_Mac10_S.tga")

exec(d,m,n,s)