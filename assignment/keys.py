import csv

# Sample list
my_list = [['Name', 'Age', 'City'],
           ['John', 28, 'New York'],
           ['Jane', 22, 'San Francisco'],
           ['Bob', 35, 'Los Angeles']]

# Specify the file name
csv_file = 'my_data.csv'

# Open the file in write mode
with open(csv_file, 'w', newline='') as file:
    # Create a CSV writer object
    writer = csv.writer(file)

    # Write the data to the CSV file
    writer.writerows(my_list)

print(f'The data has been written to {csv_file}.')
