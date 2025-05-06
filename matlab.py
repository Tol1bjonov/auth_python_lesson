import numpy as np
import matplotlib.pyplot as plt
# print(np.empty(3))
# print(np.array([3.14, 42. ]))
#
# print(np.arrange(5))
# print(np.array([0,1,2,3]))


x = np.array([[1,2],[3,4]])
y =  np.array([[5,6]])
print(np.concatenate((x,y), axis=0))

import matplotlib.pyplot as plt
import numpy as np

# 1. Basic Line Plot
time = [0, 1, 2, 3, 4, 5]
temperature = [22, 24, 25, 28, 30, 32]
plt.figure(figsize=(6,4))
plt.plot(time, temperature, marker='o')
plt.title('Time vs Temperature')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.grid(True)
plt.show()

# 2. Bar Chart
genres = ['Fiction', 'Non-Fiction', 'Sci-Fi', 'Fantasy']
books_sold = [50, 40, 35, 25]
plt.figure(figsize=(6,4))
plt.bar(genres, books_sold, color='skyblue')
plt.title('Books Sold by Genre')
plt.xlabel('Genre')
plt.ylabel('Books Sold')
plt.show()

# 3. Histogram
ages = [25, 32, 40, 60, 22, 35, 27, 29, 52, 45]
plt.figure(figsize=(6,4))
plt.hist(ages, bins=5, color='green', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# 4. Pie Chart
market_share = {'Apple': 45, 'Samsung': 30, 'Huawei': 15, 'Others': 10}
labels = list(market_share.keys())
sizes = list(market_share.values())
plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['gold', 'lightblue', 'lightgreen', 'grey'])
plt.title('Market Share of Tech Companies')
plt.show()

# 5. Scatter Plot
x_values = [1, 2, 3, 4, 5, 6, 7]
y_values = [3, 5, 7, 2, 6, 8, 9]
plt.figure(figsize=(6,4))
plt.scatter(x_values, y_values, color='red')
plt.title('Scatter Plot')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.grid(True)
plt.show()
