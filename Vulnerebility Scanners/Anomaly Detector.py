import pandas as pd
from sklearn.ensemble import IsolationForest 
import numpy as np

#Normalizing the data
def generate_network_data(n_samples=1000):
    np.random.seed(42)

    #Normal network behaviour (baseline)
    normal_ports = np.random.choice(range(20, 1024), n_samples)
    normal_traffic = np.random.normal(loc=1000, scale=200, size=n_samples) #in MBs
    normal_response_time = np.random.normal(loc=100, scale=20, size=n_samples) #in ms
    
    normal_data = np.column_stack((normal_ports, normal_traffic, normal_response_time))

    #The crazies
    anomaly_ports = np.random.choice(range(1025, 65535), int(0.05 * n_samples))
    anomaly_traffic = np.random.uniform(low=5000, high=10000, size=int(0.05 * n_samples))
    anomaly_response_time = np.random.uniform(low=500, high=1000, size=int(0.05*n_samples))

    anomaly_data = np.column_stack((anomaly_ports, anomaly_traffic, anomaly_response_time))

    #Combine and shuffle the normal with the crazies
    data = np.vstack([normal_data, anomaly_data])
    np.random.shuffle(data)
    return pd.DataFrame(data, columns=['Ports','ResponseTime','TrafficVolume'])

#Loading the network activity dataset
data = generate_network_data()

#Initialiaze the Isolation Forest model - 100 security cameras
iso_forest = IsolationForest(n_estimators=200, contamination=0.03, random_state=42)

#Fit the model to the data - training the model(guards) on what crazies look like
iso_forest.fit(data)

#Predict anomalies (-1 for anomaly, 1 for normal) - Cameras analyze and tag either as normal 1 or anomaly -1
data['anomaly'] = iso_forest.predict(data)

#flag the crazies - to extract only those rows where the model(guards) flagged as anomaly 
anomalies = data[data['anomaly'] == -1]

print ("Detected Anomalies:")
print(anomalies)

def detect_anomalies_with_isolation_forest(input_data):
    predictions = iso_forest.predict(input_data)
    return predictions

new_data = generate_network_data(100)
new_data['anomaly'] = detect_anomalies_with_isolation_forest(new_data)
print("\nNew Data Anomalies:")
print(new_data[new_data['anomaly'] == -1])