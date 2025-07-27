# Smart Sensor Monitoring

This project demonstrates a full-stack IoT application using ESP32, MicroPython, a Flask REST API, and Python scripts for data logging and visualization.

## Project Structure

- `esp32_firmware/`: MicroPython script to read sensor data and send to server
- `api_server/`: Flask API to receive and store data
- `data_logger/`: Scripts to process and visualize stored sensor data
- `screenshots/`: Folder to store any images or plots for the README

## Getting Started

1. Flash MicroPython to ESP32.
2. Connect ESP32 to Wi-Fi and run `main.py`.
3. Run Flask server: `python api_server/app.py`
4. View or log data in CSV, visualize using `visualize.py`.

## Hardware Used

- ESP32 board
- DHT22 or BME280 sensor
- Wi-Fi connection

