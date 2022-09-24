def string_to_list_firstformat(input_str):
    temp_str=""
    output_list=[]
    for i in range(len(input_str)):
        temp_str+=str(input_str[i][:-1])+" "
        if ((i+1)%8==0):
            output_list.append(temp_str)
            temp_str=""
    output_list.append(temp_str)
    return output_list
def string_to_list_secondformat(input_string):
    output_list=[]
    temp_str2=""
    temp_str=input_string[0].split(";")
    for i in temp_str:
        temp_str2=i.replace(","," ")
        output_list.append(temp_str2)
    return output_list[:-1]
