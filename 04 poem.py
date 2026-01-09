f=open("file.txt")
content=f.read()
if("twinkle" in content.lower()):
    print("The word 'twinkle' is present in the poem.")
    f.close()
else:
    print("The word 'twinkle' is not present in the poem.")
    f.close()
