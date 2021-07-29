import os


origin = os.getcwd()
def find_titanfall_2():
    spl = os.path.sep
    progs = f"C:{spl}Program Files (x86){spl}Origin Games{spl}Titanfall2{spl}"
    print("Searching for Titanfall 2...")
    try:
        os.chdir(progs)
    except OSError:
        print(f"Tried searching {progs} for Titanfall 2, however could not find it")
        while 1:
            tf2 = input("Where is Titanfall 2 installed: ")
            try:
                os.chdir(tf2)
                if "Titanfall2.exe" not in os.listdir():
                    raise OSError()
                else:
                    break
            except OSError:
                print("Either the directory is invalid or it is not the Titanfall 2 folder")
                continue
        os.chdir(origin)
        with open(".dir", "w") as d:
            d.write(tf2)
