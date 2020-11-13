import os

package_dir = os.getcwd() + '/A0183086Y_code/'
trace_address = '/traces/'
path = "/profile"
profilefolderpath = package_dir + path
if not os.path.exists(profilefolderpath):
    try:
        os.mkdir(profilefolderpath)
    except OSError:
        print("directory creation failed")
    else:
        print("directory successfully created")
else:
    print("directory already exists!")
for profile_num in range(1, 9):
    profilespath = profilefolderpath + "/" + str(profile_num)
    if not os.path.exists(profilespath):
        try:
            os.mkdir(profilespath)
        except OSError:
            print("profiles folder creation failed")
        else:
            print("profiles folder successfully created")
    else:
        print("profiles folder already exists!")
    training_address = "profile" + str(profile_num) + "/"
    for url_num in range(1, 36):
        finaltraining_address = package_dir + trace_address + training_address + str(url_num)
        file = open(finaltraining_address, "r")
        counts = dict()
        sequence = ''
        num_lines = 0
        while True:
            line = file.readline()
            if line == "":
                break
            num_lines += 1
            str_line = str(line)
            strList = str_line.split(" ")
            byte = strList[1]
            direction = strList[2]
            direction = direction[:len(direction)-1]
            if direction == "in":
                direction = 1
            else:
                direction = 0
            sequence = sequence + str(direction)
            if byte in counts:
                counts[byte] += 1
            else:
                counts[byte] = 1
        
        finalprofile_address = profilespath + "/" + str(url_num)
        profilefile = open(finalprofile_address, "w")
        profilefile.write(sequence + "\n")
        profilefile.write(str(num_lines) + "\n")
        for key in counts:
            profilefile.write(str(key) + " " + str(counts[key]) + "\n")




