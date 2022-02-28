# We have a string which contains grocery items. Print these items in a comma-separated sequence after sorting them alphabetically.
grocery_items = 'Grated Cheese, Coffee Powder, Pickles White Chocolate, Dark Chocolate, Eggs, Breads, Milk, Sugar, Salt, Cat Food, Fries'
lst_grocery = [word for word in grocery_items.split(', ')]
lst_grocery.sort()
str_grocery = ','.join(lst_grocery)
print(str_grocery)
