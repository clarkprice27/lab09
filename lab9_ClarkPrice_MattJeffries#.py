import random
import re


def convert_file_to_list(file):
    """converts open file into list with tuples"""

    questions = []

    for i, line in enumerate(file):
        if i%3 == 0 or i%3 == 2:
            line = line.split(' \n ')
            line[-1] = line[-1].replace('\n','')
            questions.extend(line)
        if i%3 == 1:
            line = line.split('._')
            line[-1] = line[-1].replace('\n','')
            line = list(line)
            questions.append(line)
        
    file_list = []
    x = 0

    while x < len(questions)-1:
        file_list.append((questions[x],questions[x+1],questions[x+2]))
        x += 3

    print_questions(file_list)
    
    return file_list



def print_questions(file_list):
    """prints the questions formatted for the screen"""
    
    question_num = 1
    for question in file_list:
        print('{}. {}'.format(question_num,question[0]))

        answer_num = 1
        for answer in question[1]:
            print('{:>5}){:3}{:s}'.format(answer_num,'',answer))
            answer_num += 1

        question_num += 1



def create_name_dictionary(names_file):
    """creates dictionary with students names and random questions"""

    assigned_questions = {}

    for name in names_file:
        name = name.replace('\n', '')
        
        rand_set = set()
        
        seed = random.randint(2,27)
        random.seed(seed)
        
        for x in range(0,5):
            rand_set.add(random.randint(1,28))
        assigned_questions[name] = sorted(rand_set)
        
    return assigned_questions



def write_dict_to_file(name_dict):
    """writes the dictionary to file 'togive.txt' """
    
    file = open('togive.txt', 'w')

    for name in name_dict:
        print('{:<10} Questions {}'.format(name, name_dict[name]), file=file)
        print('{:<10} Questions {}'.format(name, name_dict[name]))
            

''' getting name_list question number, and pulling same number from file_list '''
def create_name_list():

    name_list = {}
    
    with open('togive.txt', 'r') as infile, open('newtogive.txt', 'w+') as outfile:
            for line in infile:
                data = infile.read()
                data = data.replace("Questions ", "")
                data = data.replace("[", "")
                data = data.replace("]", "")
                outfile.write(data)

    for line in open('newtogive.txt', 'r'):

            lists = re.split(r'\s{2,}', line)
            key = lists[0]
            value = lists[1]
            name_list[key] = list(value.strip().split(', '))

    return(name_list)

''' gets user name and formats question quiz '''
def assorting_questions(file_list, name_list):

    print("\n\n\n\n\t*****  Welcome to the quiz preparation program. ******\n")

    while True:

        user_name = input("\nPlease input the name of a student who should take a practice quiz (enter EXIT to end the program): ")

        if user_name in name_list:    

            print ("\nHi", user_name, ". Here are your questions\n")
            qcount = 0   #count of Questions being asked (1-5)
            total = 0

            while qcount < len(name_list[user_name]):
            
                question_value = int(name_list[user_name][qcount]) #this will increase incrementally, represents q numbers in name file
                question_str = file_list[question_value-1][0]
                answer = file_list[question_value-1][2]

                print (question_str)            

                for num, choice in enumerate(file_list[question_value-1][1], 1):   #num is the number of the choice
                    answer_choices = ('\t {}. {}'.format(num, choice))    #{} is a place holder for the .format
                    print (answer_choices)
                    
                user_choice = input("\nWhat is your answer?")
                
                if user_choice == answer:
                    #add to score
                    total +=1 
##                elif user_choice < len(num) or user_choice > len(num):
##                    user_choice = input("Not within the number of questions (", len(num),")")
                
                qcount += 1

            print("you made a ", total / len(name_list[user_name])* 100)

        elif user_name == 'EXIT':
            break
        
        else:
            print("\nThat name was not found in the file")
            




def main():
    """executes the program"""

    
    try:
        file = open('Qsand0pts.txt', 'r')
        file_list = convert_file_to_list(file)

        names_file = open('names.txt', 'r')
        name_dict = create_name_dictionary(names_file)
        write_dict_to_file(name_dict)

        name_list = create_name_list()

        assorting_questions(file_list, name_list)

        

        file.close()
        names_file.close()
    except IOError:
        print('One of the files does not exist')
    
    

main()
