import sys

try:
    import PIL
    from PIL import Image
except ImportError:
    sys.exit("""You need PIL!
                install it from http://pypi.python.org/pypi/Pillow
                or run pip install Pillow.""")

def exec(imageAr):
    #get maximum sizes
    wMax = 0
    hMax = 0
    for im in imageAr:
        wMax = max(im.width,wMax)
        hMax = max(im.height,hMax)
    
    #scale all to maximum size
    for im in imageAr:
        if (im.width<wMax or im.height<hMax):
            im.resize((wMax,hMax), resample = PIL.Image.LANCZOS)
    
    #extract channels
    diffuse = imageAr[0]
    mask = imageAr[1]
    normal = imageAr[2]
    specular = imageAr[3]

    maskSplit = mask.split()
    print(len(maskSplit))




d = Image.open("./samples/WEP_1P_MAC10_TEX/Texture2D/Wep_1stP_Mac10_D.tga")
m = Image.open("./samples/WEP_1P_MAC10_TEX/Texture2D/Wep_1stP_Mac10_M.tga")
n = Image.open("./samples/WEP_1P_MAC10_TEX/Texture2D/Wep_1stP_Mac10_N.tga")
s = Image.open("./samples/WEP_1P_MAC10_TEX/Texture2D/Wep_1stP_Mac10_S.tga")

exec([d,m,n,s])