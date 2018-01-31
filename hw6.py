




student_list=[]
student_string=[]
temp_list=[]
another_string=''
count=0

def numbers(input):
    return any(char.isdigit() for char in input)

class Student:

    def __init__(self, id, fn, ln, sc, e):
        self.id=id
        self.fn=fn
        self.ln=ln
        self.sc=sc
        self.e=e

    def toString(self):
        return (self.id + ' ' + self.fn + ' ' + self.ln + ' ' + self.sc)



def sortByGrade(input):
    local=input

    for i, elem in enumerate(local):
        for j, elem in enumerate(local):

            if (int(local[i].sc) < int(local[j].sc)):
                # switch the two positions in list and switch i and j values
                local[i], local[j] = local[j], local[i]

            if (int(local[i].sc) == int(local[j].sc)):
                # compare eagerness
                if local[j].id==local[i].id:
                    #do nothing. same value
                    continue

                if (local[j].e == 'E'):
                    # input j goes first
                    local[i], local[j] = local[j], local[i]
    return list(reversed(local))


##do stuff here
def sortByName(input):
    local=input

    local=sorted(local, key= lambda x: x.ln, reverse=False)

    return local



def calcG(input):
    temp=input
    top_down=0
    bottom_up_lim= (len(temp)-1) - int(count/10)

    if int(count/10)==0 and count/10 != 0:
        bottom_up_lim = (len(temp)) - 1

    else:
        bottom_lim=int(count/10)


    while top_down < int(count/3):
        temp[top_down].sc='A'
        top_down+=1

    while top_down +1  <= (2 * int(count/3)):
        temp[top_down].sc='B'
        top_down+=1

    while top_down< bottom_up_lim:
        if temp[top_down].e == 'E':
            temp[top_down].sc= 'C'
        if temp[top_down].e == 'L':
            temp[top_down].sc = 'D'

        top_down+=1

    while bottom_up_lim < len(temp):
        temp[bottom_up_lim].sc='F'
        bottom_up_lim +=1




    return temp


def table(input):
    html_file = open("Output.html", "w")

    html_file.write('<table border="1">' + '\n')
    for x, Student in enumerate(input):
        html_file.write('  <tr>')
        html_file.write(' <td>' + Student.id + '\n')
        html_file.write( '   </td><td>' + Student.fn +'\n')
        html_file.write( '    </td><td>' + Student.ln +'\n')
        html_file.write( '    </td><td>' + Student.sc + '\n')
        html_file.write( '    </td></tr>' + '\n')
    html_file.write( '</table>')
    html_file.close()


for line in open("input.txt", "r"):
   temp_string=''
   temp_string += line.rstrip('\n')
   temp_string += ' '
   temp_list.append(temp_string)


i=0
while i < 5:
    another_string += temp_list[i]
    i+=1
#print(another_string)

temp_list=another_string.split()
#print(temp_list)

#parsing
for place, elem in enumerate(temp_list):
    if numbers(elem) ==True and len(elem)==9 :
        student=Student(temp_list[place], temp_list[place+1], temp_list[place+2], temp_list[place+3], temp_list[place+4])
        student_list.append(student)
        student_string.append(student.toString())
        count+=1






student_list=sortByName(calcG(sortByGrade(student_list)))

table(student_list)




