import work_with_file as wf
import phone_book as pb
import db

path1="input_format1.txt"
path2="input_format2.txt"

book_list1=db.string_to_list_firstformat(wf.file_to_str(path1))
string1=pb.list_to_first_format(book_list1)
wf.str_to_file(string1,f"{path1[:-4]}_formatted.txt")

book_list2=db.string_to_list_secondformat(wf.file_to_str(path2))
string2=pb.list_to_secondformat(book_list2)
wf.str_to_file(string2,f"{path2[:-4]}_formatted.txt")