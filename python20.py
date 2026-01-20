from sys import argv
script,length,width,height = argv
length = float(length)
width = float(width)
height = float(height)
area = 2*(length*width+length*height+width*height)
volume = length*width*height
print(f"该长方体面积area为:{area:.2f},体积volume为:{volume:.2f}")