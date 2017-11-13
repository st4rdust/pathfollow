def txt_to_array(path):
    infile = open(path)
    file_arr = infile.readlines()
    string_arr = []
    for i in range (0, len(file_arr)):
        strs = (file_arr[i].split("\t"))
        for i in range(0, len(strs)):
            strs[i] = str.strip(strs[i])
        string_arr.append(strs)
    return string_arr
