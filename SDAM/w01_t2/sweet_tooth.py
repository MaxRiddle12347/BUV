Packet = int(input("Number of candies in packet: "))
Students = int(input("Number of students receive candy: "))

a = Packet % Students
b = (Packet - a) / Students

print("Number of candies student recieve: ", b)
print("Number of candies teacher keep: ", a)