import csv
import random
from datetime import datetime, timedelta

def generate_data(num_rows):
    data = []
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2024, 12, 31)

    for _ in range(num_rows):
        # Generate a random date between start_date and end_date
        random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        # Generate a random amount (integer between 100 and 1000 for example)
        random_amount = random.randint(100, 1000)
        data.append((random_date.strftime('%Y-%m-%d'), random_amount))
    
    return data

def write_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write the header
        csv_writer.writerow(['Date', 'Amount'])
        # Write the data
        csv_writer.writerows(data)

if __name__ == "__main__":
    num_rows = 10000  # Change this to the desired number of rows
    data = generate_data(num_rows)
    filename = 'data.csv'  # Change this to the desired filename
    write_to_csv(data, filename)
    print(f"CSV file '{filename}' generated successfully with {num_rows} rows.")
