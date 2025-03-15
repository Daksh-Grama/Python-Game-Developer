# In your class, there are five groups that participated and got prizes in different competitions held in various schools. Your class teacher asks your help to record all the details. Write a program and use a tuple data structure to store each record. The program should ask the user to enter details like groupname, Sizeofthegroup, dateofthecompetition, venue, typeofthemedal. Store it as a tuple.

# Define an empty list to store tuples
competition_records = []

# Number of groups
num_groups = 5

# Collecting input from the user
for i in range(num_groups):
    print(f"\nEnter details for Group {i+1}:")
    group_name = input("Enter Group Name: ")
    size_of_group = int(input("Enter Size of the Group: "))
    date_of_competition = input("Enter Date of Competition (YYYY-MM-DD): ")
    venue = input("Enter Venue of Competition: ")
    type_of_medal = input("Enter Type of Medal Won (Gold/Silver/Bronze/None): ")

    # Storing data in tuple
    record = (group_name, size_of_group, date_of_competition, venue, type_of_medal)

    # Adding the tuple to the list
    competition_records.append(record)

# Displaying the stored data
print("\nRecorded Competition Details:")
for i, record in enumerate(competition_records, 1):
    print(f"\nGroup {i}:")
    print(f"  Group Name          : {record[0]}")
    print(f"  Size of Group       : {record[1]}")
    print(f"  Date of Competition : {record[2]}")
    print(f"  Venue              : {record[3]}")
    print(f"  Type of Medal Won   : {record[4]}")
