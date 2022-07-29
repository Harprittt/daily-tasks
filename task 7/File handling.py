file = open("txt.txt","w")
L = [" Child Labour occurs when children are forced to take up work.\n at an age they need to study and enjoy the phase of innocence. "]
file.write("Government should take strict actions on child labour.\n tfytfyugt879.")
file.writelines(L)


file1 = open("txt.txt","r")
print("output of the function is:")
print(file1.read())
print()
file1.seek(0)

print("output of the readline is:")
print(file1.readline(78))
print()
file.seek(0)

print("output of the read(9) function is:")
print(file1.read(9))
print()
file.seek(0)

print("output of the readlines function is:")
print(file1.readlines())
print()
