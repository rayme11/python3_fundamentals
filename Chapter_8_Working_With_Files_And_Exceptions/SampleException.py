menus = {'Breakfast': ['eggs', 'bagel', 'orange juice'],
         'Lunch': ['eggs', 'coffee', 'chicken'],
         'Dinner': ['tea', 'bagel', 'turnkey']}

try:
    definition = menus['soup']

except:
    print("The key doesn't exist")
finally:
    print('this will always execute... thank you')

print('Program execution continues')
