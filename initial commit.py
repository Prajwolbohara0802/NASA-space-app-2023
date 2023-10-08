import pandas as pd
import matplotlib.pyplot as plt

# Reading the data from the Excel file
file_path = r'C:\Users\user\Downloads\Book1.xlsx'
magnectic_field = pd.read_excel(file_path, engine='openpyxl')

# Filter out rows where 'Bx', 'By', or 'Bz' is less than or equal to 13
filtered_data = magnectic_field[(magnectic_field['year'] <= 2014)&(magnectic_field['Bx'] <= 13) & (magnectic_field['By'] <= 13) & (magnectic_field['Bz'] <= 13)]

# Replace 'hrs' values equal to 0 with 24
filtered_data['hrs'] = filtered_data['hrs'].replace(0, 24)

# Create line graphs using Matplotlib for 'Bx,' 'By,' and 'Bz' vs. 'hrs' with finer lines
plt.figure(figsize=(18, 6))

# Line graph for 'Bx' vs. 'hrs' with finer line
plt.subplot(3, 1, 1)
plt.plot(filtered_data['hrs'], filtered_data['Bx'], marker='o', linestyle='-', color='b', label='Bx vs. hrs', markersize=1, linewidth=0.5)
plt.title('Line graph of Bx vs. hrs')
plt.xlabel('hrs')
plt.ylabel('Bx')
plt.grid(True)

# Line graph for 'By' vs. 'hrs' with finer line
plt.subplot(3, 1, 2)
plt.plot(filtered_data['hrs'], filtered_data['By'], marker='o', linestyle='-', color='g', label='By vs. hrs', markersize=1, linewidth=0.5)
plt.title('Line graph of By vs. hrs')
plt.xlabel('hrs')
plt.ylabel('By')
plt.grid(True)

# Line graph for 'Bz' vs. 'hrs' with finer line
plt.subplot(3, 1, 3)
plt.plot(filtered_data['hrs'], filtered_data['Bz'], marker='o', linestyle='-', color='r', label='Bz vs. hrs', markersize=1, linewidth=0.5)
plt.title('Line graph of Bz vs. hrs')
plt.xlabel('hrs')
plt.ylabel('Bz')
plt.grid(True)

plt.tight_layout()
plt.show()