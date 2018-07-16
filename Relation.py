def names():
    '''
        This function takes two names and strip them returns without spaces inbetween single names.
        This function takes zero arguments 
    '''
    first_name = str(input("Enter first name(Boy) : ")).strip()
    second_name = str(input("Enter second name(Sister) : ")).strip()
    for letter in first_name:
        if letter is " ":
            first_name = first_name.replace(letter,'')
    for letter in second_name:
        if letter is " ":
            second_name = second_name.replace(letter, '')
    return [first_name, second_name]





def names_checking(names_list):
    '''
        Pass two names as a list.
        Returns true if names are valid otherwise false
    '''
    import string
    name = names_list[0].upper() + names_list[1].upper()
    alphabets = string.ascii_uppercase
    result = False
    for x in name:
        if x in alphabets:
            continue
        else:
            break
    else:
        result = True
    return result




def difference(names_list):
    '''
        Pass two names as a list.
        Returns a number 
    '''
    first_name = names_list[0].upper()
    second_name = names_list[1].upper()
    names_length = len(first_name) + len(second_name)
    count = 0
    if first_name == second_name:
        return 0
    else:
        for x in first_name:
            for y in second_name:
                if x is y:
                    second_name = second_name.replace(y, '*')
                    count += 1
                    break
        return names_length - 2*count

    
    
    
def find_relation(length=0):
    '''
        Pass a number.
        Return first letter of relation
    '''
    relation = [ 'F', 'L', 'A', 'M', 'E', 'S' ]
    size = 6
    for x in range(6):
        if len(relation) is 1:
            return relation[0]
        else:
            temp = length % (size-x)
            if temp is 0:
                relation.pop()
            elif temp is 1:
                relation.pop(0)
            else:
                lst01 = relation[:temp-1]
                lst02 = relation[temp:]
                relation = lst02 + lst01 
                
                
                
def print_relation(relation, names_list):
    '''
        Takes two parameters 1.First letter of relation and names list
    '''
    name01 = names_list[0]
    name02 = names_list[1]
    if relation is 'F':
        print(f"\n\nFriends\n\n")
    elif relation is 'L':
        print(f"\n\nLovers\n\n")
    elif relation is 'A':
        print("\n\nAffection\n\n")
    elif relation is 'M':
        print(f"\n\nMarriage\n\n")
    elif relation is 'E':
        print(f"\n\nEnemies\n\n")
    elif relation is 'S':
        print(f"\n\nSister\n\n")
    else:
        print('\n\nError in finding relation\n\n')
                   

class Flames():
    '''
        This class helps to find relation between two people
    '''
    print('Instructions:-')
    print('1.Enter unique names.')
    print('2.Enter male name first.')
    print('3.Enter female name second.')
    print("4.Don't use special characters like(! ,@ ,#, .......)")
    '''names_list stores two names as a list'''
    names_list = names()
    '''check02 stores a boolen value'''
    check = names_checking(names_list)
    if check:
        result = difference(names_list)
        if result is 0:
            print("\n\nEnter Unique names.\n\n")
        else:
            relation = find_relation(result)
            print_relation(relation, names_list)
    else:
        print("\n\nEnter valid names.\n\n")            