
years = int(input("Do you know how old are you ?\n"))

age_in_decades = years // 10 # get integer value
age_in_years = years % 10 # get remainder of division

print("You are:  " + str(age_in_decades) + " decades old")
print("and:  " + str(age_in_years) + " years")
