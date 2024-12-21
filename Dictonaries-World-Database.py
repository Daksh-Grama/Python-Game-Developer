Country_DB = {}

while True:
  print("1. Insert")
  print("2. Display all countries")
  print("3. Display all capitals")
  print("4. Get capital")
  print("5. Delete")

  cs = int(input("Enter your choice : "))

  if cs == 1 :
    Country = input("Enter a country : ").upper()
    Capital = input("Enter a capital : ").upper()
    Country_DB[Country] = Capital

  elif cs == 2 :
    countries = list(Country_DB.keys())
    print("The list of countries are : ", countries)

  elif cs == 3 :
    capitals = list (Country_DB.values())
    print("The list of capitals are : ", capitals)

  elif cs == 4 :
    Country = input("Enter a country : ").upper()
    print("The capital name is : ", Country_DB[Country])

  ## Set up option 5 to delete item
  # set up option 6 to exit from program if any other key is pressed apart from 1-5

  elif cs == 5 :
    Country = input("Enter a Country : ").upper()
    del Country_DB[Country]

  else:
    print ("Its an Invalid value please select a correct value.")









 
 


