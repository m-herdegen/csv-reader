import csv

def csv_reader():


    ## USER INPUT
    user_input = input("Please type in either cats or dogs: \n>>")
    file_test = 'data/' + user_input + ".csv"
    
    ## OPEN THE FILE (and handle bad input)
    try:
        open(file_test)
    except:
        print(f"Sorry, we don't have any {user_input} here.")

    ## PARSE TO DATA STRUCTURE  
    with open(file_test, newline='') as csvfile:
        our_reader = csv.reader(csvfile, delimiter=',', quotechar = '|')
        animal_list = []
        for row in our_reader:
            animal_list.append(row)


    dictionary = dict.fromkeys(animal_list[0])
    # final_list = []
    # output_list = []

    # for each animal in the list
    for x in range(1, len(animal_list)):
        # for each piece of information about the animal
        for i in range(len(animal_list[0])):
            # assign that information to the corresponding label in the dictionary
            dictionary[animal_list[0][i].strip()] = animal_list[x][i].strip()
        
        # output strings for each animal
        print(f"{animal_list[x][0].strip()} is a {animal_list[x][1].strip()} year old {animal_list[x][2].strip()}.")
        #print(dictionary)
        #output_list.append(f"{animal_list[x][0]} is a {(animal_list[x][1])} year old {animal_list[x][2]}.")
        #final_list.append(dictionary)

    # display information about the animal
    # print(output_list)

    csvfile.close()


csv_reader()