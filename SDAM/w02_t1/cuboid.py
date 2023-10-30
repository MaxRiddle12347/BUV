def volume( l , h , w ):
    return (l * h * w)
def surface( l , h , w ):
    return (2 * l * w + 2 * w * h + 2 * l * h)

l = int(input("Please inpit the length: "))
h = int(input("Please input the height: "))
w = int(input("Please input the width: "))

print("Volume should be", volume(l, h, w))
print("Surface should be", surface(l, h, w))