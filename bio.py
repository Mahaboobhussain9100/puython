class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print('hai:',self.name)
        print('your marks are:',self.marks)
    def grade(self):
        if self.marks>=60:
            print('you got first grade')
        elif self.marks>=50:
            print('you grade second grade')
        elif self.marks>=35:
            print('you got third grade')
        else:
            print('you are failed')
n=int(input('Enter number of students:'))
for i in range(n):
    name=input('enter name:')
    marks=int(input('enter marks:'))
    s=student(name,marks)
    s.display()
    s.grade()
    print()
