# Install dependencies:
pip install pyserial scikit-learn

# Python code:
import serial
from sklearn.tree import DecisionTreeClassifier

# Training dataset (Signal Strength Classification):
X = [[0], [100], [200], [300], [400], [500], [600], [700], [800], [900], [1023]]
y = ["Weak", "Weak", "Weak", "Medium", "Medium", "Medium", "Strong", "Strong", "Strong", "Strong", "Strong"]

# Train model:
model = DecisionTreeClassifier()
model.fit(X, y)

# Serial connection (change COM port):
arduino = serial.Serial('COM3', 9600)

print("Reading Signal Strength...\n")

while True:
    data = arduino.readline().decode().strip()

    if data.isdigit():
        value = int(data)
        prediction = model.predict([[value]])

        print(f"Signal Value: {value} → Strength: {prediction[0]}")
