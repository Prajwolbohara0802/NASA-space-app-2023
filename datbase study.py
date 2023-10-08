import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


file_path = r'C:\Users\user\Downloads\wind2.xlsx'
file_path1 = r'C:\Users\user\Downloads\ACE2.xlsx'


magnectic_field = pd.read_excel(file_path, engine='openpyxl')
magnectic_field1 = pd.read_excel(file_path1, engine='openpyxl')


filtered_data = magnectic_field[(magnectic_field['Bx'] <= 30) & (magnectic_field['By'] <= 13) & (magnectic_field['Bz'] <= 13)]
filtered_data1 = magnectic_field1[(magnectic_field1['Bx'] <= 30) & (magnectic_field1['By'] <= 13) & (magnectic_field1['Bz'] <= 13)]


lr = LinearRegression()
lr2=LinearRegression()
lr3=LinearRegression()

X = magnectic_field[['day']]  
Y = magnectic_field[['Bx']] 
Y1=magnectic_field[['By']]
Y2=magnectic_field[['Bz']] 

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)
X_train, X_test, Y1_train, Y1_test = train_test_split(X, Y1, test_size=0.2, random_state=2)
X_train, X_test, Y2_train, Y2_test = train_test_split(X, Y1, test_size=0.2, random_state=2)

lr.fit(X_train, Y_train)
lr2.fit(X_train,Y1_train)
lr3.fit(X_train,Y2_train)


prediction = lr.predict(X_test)
prediction2 = lr2.predict(X_test)
prediction3 = lr3.predict(X_test)

plt.figure(figsize=(30, 6))

plt.subplot(3, 1, 1)
plt.plot(filtered_data['day'], filtered_data['Bx'], marker='.', linestyle='-', color='r', label='Bx vs. day', linewidth=2.0)
plt.scatter(X_test, prediction, color='b', marker='o', label='Predicted Bx')
plt.grid(True)


plt.subplot(3, 1, 1)
plt.plot(filtered_data1['day'], filtered_data1['Bx'], marker='.', linestyle='-', color='k', label='Bx vs. day', linewidth=2.0)
plt.title('Line plot of Bx vs. day (WIND VS ACE)')
plt.xlabel('day')
plt.ylabel('Bx')
plt.grid(True)

###
plt.subplot(3, 1, 2)
plt.plot(filtered_data['day'], filtered_data['By'], marker='.', linestyle='-', color='r', label='By vs. day', linewidth=2.0)
plt.scatter(X_test, prediction2, color='b', marker='o', label='Predicted By')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(filtered_data1['day'], filtered_data1['By'], marker='.', linestyle='-', color='k', label='By vs. day', linewidth=2.0)
plt.title('Line plot of By vs. day (WIND VS ACE)')
plt.xlabel('day')
plt.ylabel('By')
plt.grid(True)

#########


plt.subplot(3, 1, 3)
plt.plot(filtered_data['day'], filtered_data['Bz'], marker='.', linestyle='-', color='r', label='Bz vs. day', linewidth=2.0)
plt.scatter(X_test, prediction2, color='b', marker='o', label='Predicted Bz')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(filtered_data1['day'], filtered_data1['Bz'], marker='.', linestyle='-', color='k', label='Bz vs. day', linewidth=2.0)
plt.title('Line plot of Bz vs. day (WIND VS ACE)')
plt.xlabel('day')
plt.ylabel('Bz')
plt.grid(True)




plt.tight_layout()
plt.show()

#print("Test Data:")
#print(X_test)
#print("Predicted Bx:")
#print(prediction)
