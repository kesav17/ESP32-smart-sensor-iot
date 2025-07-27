import pandas as pd
import matplotlib.pyplot as plt

def plot_data(csv_file='../api_server/data.csv'):
    try:
        df = pd.read_csv(csv_file)
        df['timestamp'] = pd.to_datetime(df['timestamp'])

        plt.figure(figsize=(10, 5))
        plt.plot(df['timestamp'], df['temperature'], label='Temperature (°C)', marker='o')
        plt.plot(df['timestamp'], df['humidity'], label='Humidity (%)', marker='x')
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.title('ESP32 Sensor Data')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.xticks(rotation=45)
        plt.show()
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    plot_data()
