student = {}
student["Name"] = str(input('Name of the student: '))
student["Score"]= int(input(f'Score of {student["Name"]}:'))
if student["Score"] >= 7:
    student["Status"]= 'Pass'
elif 5 <= student["Score"]<=7:
    student["Status"]= 'Pending'
else:
    student["Status"]='Failed'

for k,v in student.items():
    print(f'- {k} is Equal to {v}')