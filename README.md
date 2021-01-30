# dht11-display
A python executable for displaying in a terminal temperature and humidity values measured by a DHT11 sensor

## Install device dependencies
```
sudo apt update
sudo apt-get install virtualenv python3-pip
pip3 --version
```

## Clone this repository
Navigate to add-on application folder
```
cd /opt
```
Clone repository
```
sudo git clone https://github.com/aidan-parkinson/dht11-display.git
```

## Create virtual environment and install project dependencies
Navigate to project folder
```
cd /opt/dht11-display/
```
Create a virtual environment
```
sudo virtualenv venv
```
Activate it
```
source venv/bin/activate
```
Install project dependencies
```
pip3 install -r requirements.txt
```
Deactivate the virtual environment
```
deactivate
```

## To run the bridge (start at this point if you have completed this process before on your device)
Navigate to project folder
```
cd /opt/dht11-display/
```
Activate the virtual evironment with pre-installed dependencies
```
source venv/bin/activate
```
Run the `dht11-display.py` controller
```
python3 dht11-display.py
```
