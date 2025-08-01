# dict = {
#     "name" :"shishir",
#     "age":16,
#     'status':'single',
#     'single':True,
#     's':["hsishir,12"],
# }
# print(dict)
# print(type(dict))

#dictionary is mutable 
#keys can be of primitive only
#dictionary is unoredred
#no duplicate key


# print(dict["name"])
# print(dict["s"])

# dict["name"]="hehehhe"
# dict['surname']=["bhusal","regmi","poudel"]
# print(dict)






#   *** Nested dictionaries ***
# student={
#     'name':"rahul kumar",
#     'subject':{
#         "phy":97,
#         "che":34,
#         "c++":56
#     },
#     "sex":"male"
# }
# print(student["subject"])
# print(student["subject"]["phy"])
# print(list(student.keys()))
# print(len(student.keys()))




#dictionary methods
# print(student.values()) ->ruturns all values
# print(student.items()) -> returns all(key,values)pairs as tuples
# print(student.get('name'))  returns the values and none if DNE in dictionary
#dict.update()
