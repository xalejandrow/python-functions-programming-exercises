# Your code goes here:
#def render_person(param):
#    return param
def render_person(name, born, eyes, age, gender):
    text =  name +" is a "+ str(age) +" years old "+gender+" born in "+born+" with "+eyes+" eyes"
    return text


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))