
def list_to_first_format (input_list):
    temp_str=""
    result=""
    for i in input_list:
        temp_str=i.split()
        for j in temp_str:
            result+=j+"\n"+"\n"


    return result

def list_to_secondformat(input_list):
    temp_str=""
    result=""
    for i in input_list:
        temp_str+=i.replace(" ",",")
        temp_str+=";"
    return temp_str