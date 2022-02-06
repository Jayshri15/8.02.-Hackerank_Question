def nested_dictionary(l1, l2, l3):
     result = [{x: {y: z}} for (x, y, z) in zip(l1, l2, l3)]
     return result
student_id = ["S001", "S002", "S003", "S004"] 
student_name = ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] 
student_grade = [85, 98, 89, 92]
print("Original strings:")
print(student_id)
print(student_name)
print(student_grade)

#before

print("\nNested dictionary:")
ch='a'
print(nested_dictionary(student_id, student_name, student_grade))





def sum(list_of_dicts):
    for d in list_of_dicts:
        var = d.pop('V')
        num = d.pop('VI')
        d['V+VI'] = (var + num)/2
    return list_of_dicts 
student_details= [
  {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
  {'id' : 2, 'subject' : 'english', 'V' : 73, 'VI' : 74},
  {'id' : 3, 'subject' : 'history', 'V' : 75, 'VI' : 86}
]
print(sum(student_details))






