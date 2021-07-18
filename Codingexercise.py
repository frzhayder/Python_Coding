# display requirement data of what you need to display in userin
userin=input('enter from kg to lb   ')
# you can use numbin=float(userin) or numbin=int(userin) to run the userin info
numbin=float(userin);
# variable explained as whatever the number added by the user would be multily with the unit you would like to change userin data.
conversion_kg_lb= numbin* 2.205
# for command you need to add strings and the variable. 
print('the conversion of kg to lb', 'is', conversion_kg_lb)
