from PIL import Image

s_h = 600
s_w = 600

complex = Image.new("RGB",(s_w,s_h),(255,255,255))
count = 0

for x in range(s_w):
    for y in range(s_h):
        z = (s_w/2-x)/(s_h/2) + (y-s_h/2)*1j/(s_h/2)
        c = 0
        count = 0
        for q in range(1000):
            c = c**2- z
            count += 1
            if c.real > 2 or c.imag >2:
                complex.putpixel((x,y),(count,127,(255-count)))
                break
        if count == 1000:
            complex.putpixel((x,y),(0,0,0))

#complex.save("mandlebrot.png")
complex.show()
    
