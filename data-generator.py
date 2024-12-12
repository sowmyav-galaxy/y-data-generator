import pandas as pd
import numpy as np

# Load the input CSV file
input_file = "falcon9_data.csv"  
data = pd.read_csv(input_file)

# Parameters for yaw motion
yaw_amplitude = 0.05  
yaw_frequency = 0.1  
yaw_error_percentage = 5  

# Generate time array based on the length of the input data
time = np.linspace(0, len(data) - 1, len(data))

# Calculate intended yaw as a sinusoidal function
yaw_intended = yaw_amplitude * np.sin(2 * np.pi * yaw_frequency * time)

# Introduce random error within the ±5% range
yaw_error = np.random.uniform(
    -yaw_error_percentage / 100 * yaw_amplitude,
    yaw_error_percentage / 100 * yaw_amplitude,
    len(time)
)
yaw_actual = yaw_intended + yaw_error

# Calculate y-axis motion based on yaw
# Assuming downrange (x-axis) motion is significant compared to y-axis
crossrange_motion = data['downrange'] * np.tan(yaw_actual)

# Add the new data to the DataFrame
data['yaw_intended'] = yaw_intended
data['yaw_actual'] = yaw_actual
data['crossrange'] = crossrange_motion

# Save the updated DataFrame back to the original file
output_file = "output_data1.csv"  
data.to_csv(output_file, index=False)
