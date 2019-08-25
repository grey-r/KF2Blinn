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

    #split mask into components
    maskSplit = mask.split()
    reflectivity = maskSplit[0]
    gloss = maskSplit[1]
    ao = maskSplit[2]

    #composite final textures


    #diffuse=diffuse*ao
    finalDiffuse = PIL.ImageChops.multiply(diffuse.convert(mode="RGB"),ao.convert(mode="RGB"))
    finalDiffuse.save("./dif.tga","TGA")
 
    #envMasks=spec*ao*reflectivity
    env = PIL.ImageChops.multiply(specular.convert(mode="RGB"),ao.convert(mode="RGB"))
    env = PIL.ImageChops.multiply(env,reflectivity.convert(mode="RGB"))
    #split env into channels
    envSplit = env.split()
    envRed = envSplit[0]
    envGreen = envSplit[1]
    envBlue = envSplit[2]
    #save each env channel as rgba
    envRGBTMP=PIL.Image.new("RGBA", (wMax,hMax), color=0)
    #r
    envRGBTMP.putalpha(envRed)
    envRGBTMP.save("./env_r.tga","TGA")
    #g
    envRGBTMP.putalpha(envGreen)
    envRGBTMP.save("./env_g.tga","TGA")
    #b
    envRGBTMP.putalpha(envBlue)
    envRGBTMP.save("./env_b.tga","TGA")





d = Image.open("./samples/WEP_1P_MAC10_TEX/Texture2D/Wep_1stP_Mac10_D.tga")
m = Image.open("./samples/WEP_1P_MAC10_TEX/Texture2D/Wep_1stP_Mac10_M.tga")
n = Image.open("./samples/WEP_1P_MAC10_TEX/Texture2D/Wep_1stP_Mac10_N.tga")
s = Image.open("./samples/WEP_1P_MAC10_TEX/Texture2D/Wep_1stP_Mac10_S.tga")

exec([d,m,n,s])