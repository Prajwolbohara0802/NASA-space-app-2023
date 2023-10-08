import pandas as pd
import matplotlib.pyplot as plt

# Reading the data from the Excel file
file_path = r'C:\Users\user\Downloads\Book1.xlsx'
magnectic_field = pd.read_excel(file_path, engine='openpyxl')

# Define the range of days you want to include (e.g., days 1 to 30)
start_day = 1
end_day = 30

# Filter the data to include only the specified range of days
filtered_data = magnectic_field[
    (magnectic_field['day'] >= start_day) &
    (magnectic_field['day'] <= end_day) &
    (magnectic_field['Bx'] <= 30) &
    (magnectic_field['By'] <= 13) &
    (magnectic_field['Bz'] <= 13)
]

filtered_data['hrs'] = filtered_data['hrs'].replace(0, 24)

plt.figure(figsize=(30, 6))

plt.subplot(3, 1, 1)
plt.scatter(filtered_data['day'], filtered_data['Bx'], marker='o', color='r', label='Bx vs. day', s=1)
plt.title('Scatter plot of Bx vs. day (Days 1 to 30)')
plt.xlabel('day')
plt.ylabel('Bx')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.scatter(filtered_data['day'], filtered_data['By'], marker='o', color='b', label='By vs. day', s=1)
plt.title('Scatter plot of By vs. day (Days 1 to 30)')
plt.xlabel('day')
plt.ylabel('By')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.scatter(filtered_data['day'], filtered_data['Bz'], marker='o', color='g', label='Bz vs. day', s=1)
plt.title('Scatter plot of Bz vs. day (Days 1 to 30)')
plt.xlabel('day')
plt.ylabel('Bz')
plt.grid(True)

plt.tight_layout()
plt.show()
