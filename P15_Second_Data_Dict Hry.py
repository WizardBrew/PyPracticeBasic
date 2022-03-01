my_dict ={
"fast" : " In Quick Manner",
"Harry": "Coding Gineus",
"Markss" : [1,2,5],
"Another" : {'Harry':'Potter'}

}

# print(my_dict['fast'])
# print(my_dict['Harry'])
# print(my_dict['Markss'])                          # Prints List Value As assigned
# print(my_dict['Another']["Harry"])                # Print Nested Dict
# my_dict ["Markss"] = [2,6,8]      
# print(my_dict["Markss"])                          # GIves value of marks only
# print(my_dict.keys())                             # Gives Keys
# print(my_dict.values())                           # Gives Valus of keys
# print(my_dict.items())                            #Prints Keys & Values for all containts
# my_dict.update({"Lovish":"Friend"})               # Updates the dictionary
# print(my_dict.get("Harry"))                       # If its present it will return or gives none
# print(my_dict["Harry"])

op = input("Enter the key\n")
print(my_dict[op])







