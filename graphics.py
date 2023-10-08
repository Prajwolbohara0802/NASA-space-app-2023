import pandas as pd

import matplotlib.pyplot as plt

# Reading the data from the Excel file
file_path = r'C:\Users\user\Downloads\Book1.xlsx'
magnectic_field = pd.read_excel(file_path, engine='openpyxl')

filtered_data = magnectic_field[(magnectic_field['Bx'] <= 30) & (magnectic_field['By'] <= 13) & (magnectic_field['Bz'] <= 13)]

filtered_data['hrs'] = filtered_data['hrs'].replace(0, 24)

plt.figure(figsize=(30, 6))

plt.subplot(3, 1, 1)
plt.plot(filtered_data['day'], filtered_data['Bx'], marker='.', color='r', label='Bx vs. day', linewidth=0.01)
plt.title('Line plot of Bx vs. day (Fine Line)')
plt.xlabel('day')
plt.ylabel('Bx')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(filtered_data['day'], filtered_data['By'], marker='.', color='b', label='By vs. day', linewidth=0.01)
plt.title('Line plot of By vs. day (Fine Line)')
plt.xlabel('day')
plt.ylabel('By')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(filtered_data['day'], filtered_data['Bz'], marker='.', color='g', label='Bz vs. day', linewidth=0.01)
plt.title('Line plot of Bz vs. day (Fine Line)')
plt.xlabel('day')
plt.ylabel('Bz')
plt.grid(True)

plt.tight_layout()
plt.show()
