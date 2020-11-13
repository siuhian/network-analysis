import os
import sys

def tie_breaker(obs_seq, match_rate_seq, cur_seq):
    val1 = min(len(obs_seq), len(match_rate_seq))
    num_char_matched1 = 0
    for i in range(0, val1):
        if obs_seq[i] == match_rate_seq[i]:
            num_char_matched1 += 1

    val2 = min(len(obs_seq), len(cur_seq))
    num_char_matched2 = 0
    for i in range(0, val2):
        if obs_seq[i] == cur_seq[i]:
            num_char_matched2 += 1

    if int(num_char_matched1) >= int(num_char_matched2):
        return 1
    else:
        return 0

package_dir = os.getcwd() + '/A0183086Y_code/'
package_dir1 = os.getcwd()
profile_address = "/profile/"
obs_addr1 = "/" + sys.argv[1] + "/"
obs_addr2 = "/" + sys.argv[2] + "/"
anon_keyword = '-anon'
predictions1 = [0] * 35
predictions2 = [0] * 35
print("Classifying in progress...")
for ind in range(1, 36):
    final_address = package_dir1 + obs_addr1 + str(ind) + anon_keyword
    file = open(final_address, "r")
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
    
    prediction = ""
    max_match_rate = 0
    prediction_sequence = ""
    for profile_num in range(1, 9):
        profile_address = package_dir + "/profile/" + str(profile_num) + "/"
        for url_num in range(1, 36):
            finalprofile_address = profile_address + str(url_num)
            file = open(finalprofile_address, "r")
            line = file.readline()
            profile_sequence = line
            line = file.readline()
            profile_num_lines = line
            profile_counts = dict()
            num_match = 0
            match_rate = 0
            while True:
                line = file.readline()
                if line == "":
                    break
                str_line = str(line)
                strList = str_line.split(" ")
                byte = strList[0]
                num = strList[1]
                num = num[0:len(num)-1]
                profile_counts[byte] = num
            for key in counts:
                if key in profile_counts:
                    val1 = int(counts[key])
                    val2 = int(profile_counts[key])
                    match = min(val1,val2)
                    num_match += match
            if int(profile_num_lines) == 0:
                match_rate = 0
            else:
                match_rate = int(num_match) * 1.0 / int(num_lines)
            if match_rate > max_match_rate:
                max_match_rate = match_rate
                prediction_sequence = profile_sequence
                prediction = url_num
            elif match_rate == max_match_rate:
                ret_val = tie_breaker(sequence, prediction_sequence, profile_sequence)
                ret_val = int(ret_val)
                if ret_val == 0:
                    prediction_sequence = profile_sequence
                    prediction = url_num
    
    predictions1[prediction-1] = ind


for ind1 in range(1, 36):
    final_address = package_dir1 + obs_addr2 + str(ind1) + anon_keyword
    file = open(final_address, "r")
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

    prediction = ""
    max_match_rate = 0
    prediction_sequence = ""
    for profile_num in range(1, 9):
        profile_address = package_dir + "/profile/" + str(profile_num) + "/"
        for url_num in range(1, 36):
            finalprofile_address = profile_address + str(url_num)
            file = open(finalprofile_address, "r")
            line = file.readline()
            profile_sequence = line
            line = file.readline()
            profile_num_lines = line
            profile_counts = dict()
            num_match = 0
            match_rate = 0
            while True:
                line = file.readline()
                if line == "":
                    break
                str_line = str(line)
                strList = str_line.split(" ")
                byte = strList[0]
                num = strList[1]
                num = num[0:len(num)-1]
                profile_counts[byte] = num
            for key in counts:
                if key in profile_counts:
                    val1 = int(counts[key])
                    val2 = int(profile_counts[key])
                    match = min(val1,val2)
                    num_match += match            
            if int(profile_num_lines) == 0:
                match_rate = 0
            else:
                match_rate = int(num_match) * 1.0 / int(num_lines)
            if match_rate > max_match_rate:
                max_match_rate = match_rate
                prediction_sequence = profile_sequence
                prediction = url_num
            elif match_rate == max_match_rate:
                ret_val = tie_breaker(sequence, prediction_sequence, profile_sequence)
                ret_val = int(ret_val)
                if ret_val == 0:
                    prediction_sequence = profile_sequence
                    prediction = url_num

    predictions2[prediction-1] = ind1

print("Writing to result.txt...")
f = open("result.txt", "w")
for j in range(0, 35):
    result_line = str(predictions1[j]) + " " + str(predictions2[j]) + "\n"
    f.write(result_line)
f.close()
print("Done")



