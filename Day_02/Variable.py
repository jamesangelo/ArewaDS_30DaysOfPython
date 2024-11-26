#Day 2: 30 Days of python programming

#Exercise Level 1
first_name = 'James' 
Last_name = 'Williams' 
full_name = 'James Williams'
country = 'Sweden'
city = 'Vienna' 
age = 16   
year = 2024 
is_married = True
is_true = True
is_light_on = True
x, y, z = 2, 'man', 3.89

#Exercise Level 2
#1
print('first_name: ', type(first_name))
print('last_name: ', type(last_name))
print('full_name: ', type(full_name))
print('country: ', type(country))
print('city: ',type(city))
print('age: ',type(age))
print('year: ', type(year))
print('is_married: ', type(is_married))
print('is_true: ',type(is_true))
print(type(is_light_on))
print('x: ',type(x), 'y: ', type(y), 'z: ', type(z))

#2
print(len(first_name))

#3
ln_lenght = len(last_name)
fn_lenght = len(first_name)
if(ln_lenght > fn_lenght):
  print(f'last_name length: {ln_lenght} is greater than first_name lenght: {fn_lenght}')
elif(ln_lenght < fn_lenght):
  print(f'last_name length: {ln_lenght} is less than first_name lenght: {fn_lenght}')
else:
  print(f'last_name length: {ln_lenght} is equal than first_name lenght: {fn_lenght}')

#4
num_one = 5
num_two = 4

#5
total = num_one + num_two

#6
diff = num_two - num_one

#7
product = num_two * num_one

#8
division = num_two / num_one

#9
reminder = num_two % num_one

#10
exp = num_one ** num_two

#11
floor_division = num_one//num_two

#12
#i
radius = 30 
PI = 3.14
area_of_circle = PI * (radius ** 2)
print(area_of_circle)
#ii
circum_of_circle = 2 * PI * radius
print(circum_of_circle)
#iii
radius = input('Enter radius Val: ',)
area_of_circle = PI * (radius ** 2)
print(area_of_circle)

#13
first_name = input('Enter first name: ',)
last_name = input('Enter last name: ',)
country = input('Enter country: ',)
age = input('Enter age: ',)

#14
print(help('keywords'))





