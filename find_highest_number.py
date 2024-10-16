#define the method
def find_the_highest_number(first_num, second_num, third_num, fourth_num, fifth_num):
    #assume that the first number is the highest number
    highest_number = first_num
    #using if statement to determine highest number
    if second_num > highest_number:
        highest_number = second_num
    if third_num > highest_number:
        highest_number = third_num
    if fourth_num > highest_number:
        highest_number = fourth_num
    if fifth_num > highest_number:
        highest_number = fifth_num
    return highest_number
