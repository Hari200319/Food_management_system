import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


import math

def calculate_distance(coord1, coord2):
    """
    Calculate the distance (in kilometers) between two geographic coordinates using the Haversine formula.
    
    Parameters:
    coord1 (tuple): Latitude and longitude of the first point (lat1, lon1).
    coord2 (tuple): Latitude and longitude of the second point (lat2, lon2).
    
    Returns:
    distance (float): The distance between the two points in kilometers.
    """
    # Radius of the Earth in kilometers
    R = 6371.0
    
    # Convert latitude and longitude from degrees to radians
    lat1, lon1 = math.radians(coord1[0]), math.radians(coord1[1])
    lat2, lon2 = math.radians(coord2[0]), math.radians(coord2[1])
    
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    
    return distance



# Load NGO data (latitude, longitude)
ngo_data = pd.read_csv('Mini project/ngo_locations.csv')

# User's location (latitude, longitude)
user_location = (75.7558,67.6176)

# Calculate distances from user's location to NGO locations
ngo_data['distance'] = ngo_data.apply(lambda row: calculate_distance(user_location, (row['latitude'], row['longitude'])), axis=1)

# # Select features and target variable
# X = ngo_data[['latitude', 'longitude']]
# y = ngo_data['distance']

# # Split data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Train KNN model
# k = 5  # Number of neighbors
# knn_model = KNeighborsRegressor(n_neighbors=k)
# knn_model.fit(X_train, y_train)

# # Make predictions
# predicted_distance = knn_model.predict([[75.7558,67.6176]])

# # Find nearest NGO based on predicted distance
# nearest_ngo = ngo_data.iloc[(ngo_data['distance'] - predicted_distance).abs().argsort()[:1]]

# # Output nearest NGO information
# print("Nearest NGO:")
# print(nearest_ngo)

sorted_ngos = ngo_data.sort_values(by='distance')

# Output nearest NGOs in ascending order
print("Nearest NGOs:")
for index, ngo in sorted_ngos.iterrows():
    print(ngo['name'], ":", ngo['distance'], "km")
