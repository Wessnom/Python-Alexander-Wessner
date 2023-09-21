import os
import math
import matplotlib.pyplot as plt

# functions

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

    # källa som hjälpte med lambda sortering, https://sparkbyexamples.com/python/sort-using-lambda-in-python/
def find_k_nearest_point(test_point, training_points, k=10):
    # beräkna avstånd från testpunkter till alla träningspunkter
    distances = [(euclidean_distance(test_point, (width, height)), width, height, label) for (width, height, label) in training_points]
    sorted_distances = sorted(distances, key=lambda x: x[0])
    return sorted_distances[:k]

def classify_test_point(test_point, training_points, k=10):
    k_nearest_point = find_k_nearest_point(test_point, training_points, k)
    pichu_count = sum([1 for _, _, _, label in k_nearest_point if label == 0])
    pikachu_count = k - pichu_count
    return "Pichu" if pichu_count > pikachu_count else "Pikachu"

data_points = []
with open("labs\lab_2\datapoints.txt", "r") as file:
    next(file) # Skippa första raden.
    for line in file:
        parts = line.strip().split(",") # Strippa mellanslag och splitta på "," varje rad blir egen tuple
#        print(parts)
        width, height, label = float(parts[0]), float(parts[1]), int(parts[2])
        data_points.append((width, height, label)) # varje tuple appendad till den tomma data_points listan
#       print(data_points)

while True:
    user_input = input("Enter a test point as 'width,height' or type 'quit' to exit: ")

    if user_input.lower() == 'quit':
        break

    try:
        # Map(float) applicerar en given funktion, mitt fall float på user_inputs, returnerar ny iterable med transformerade element.
        width, height = map(float, user_input.split(",")) 
        if width < 0 or height < 0:
            print("Both width and height should be positive numbers.")
            continue
        test_point = (width, height)
        classification = classify_test_point(test_point, data_points, k=10)
        print(f"Sample with (width, height): {test_point} classified as {classification}")

    except ValueError:
        print("Invalid input format. Please enter the point as 'width,height', both positive.")
        




#test_points = [(25, 32), (24.2, 31.5), (22, 34), (20.5, 34)]
#for test_point in test_points:
#    classification = classify_test_point(test_point, data_points)
#    print(f"Sample with (width, height): {test_point} classified as {classification}")

x0, y0, x1, y1 = [], [], [], []

for (width, height, label) in data_points:
    if label == 0:
        x0.append(width)
        y0.append(height)
    else:
        x1.append(width)
        y1.append(height)

fig, ax = plt.subplots()


ax.scatter(x0, y0, label='Pichu', color='orange')
ax.scatter(x1, y1, label='Pikachu', color='yellow')
ax.set_xlabel('Width (cm)')
ax.set_ylabel('Height (cm)')
ax.legend()
ax.set_title('Pichu and Pikachu Data Points')
ax.set_facecolor('lightgray')

fig.patch.set_facecolor('lightblue')

plt.show()