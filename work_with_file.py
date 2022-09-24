def file_to_str(path):
    with open (path) as data:
        temp_str=data.readlines()
    return temp_str
def str_to_file(temp_str, path):
    with open (path,"w") as data:
        data.write(temp_str)


