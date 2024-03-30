import csv
import matplotlib.pyplot as plt

print('------------------read from csv and make bar chart-------------------')

with open('C:\\MY_FILES\\people.csv', 'r') as file:
    read_from_csv = csv.reader(file)
    read_from_csv.__next__()  # ignore header
    x = []
    y = []
    for row in read_from_csv:
        x.append(row[0])
        y.append(float(row[1]))
    plt.bar(x, y)
    plt.xlabel('Name')
    plt.ylabel('Age')
    plt.title('Read Data from csv Name vs Age')
    plt.xticks(rotation=45)
    plt.show()

