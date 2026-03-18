# dt = {"name": "rocky", "subject": "Math", "age": 25}
# print(dt)
# print(type(dt))

dt2 = {"names" : ["rocky", "jack", "claude"],
       "subjects": ["math", "physics", "cs"],
       "age" :[14,12,16]
       }
# print(dt2)
# print(type(dt2))
# print(dt2["names"], dt2["age"])
# print(dt2["names"][0],"\n", dt2["age"])
# print(dt2["names"][0],"\n", dt2["subjects"][0], "\n", dt2["age"][0])
# print(dt2.keys()) # to access only keys
# print(dt2.values()) # to access only values


#to insert other one pair into dictionary
# dt2[key] = value
# dt2['marks'] = [25,36,41]
# print(dt2)


student_data = {"names" : ["rocky", "jack", "claude"],
       "subjects": ["math", "physics", "cs"],
       "age" :[14,12,16],
       "marks": [25,36,41]
       }
student_data["names"].append('Lovely')
student_data["subjects"].append('math')
student_data["age"].append(9)
student_data["marks"].append(23)
print(student_data)
