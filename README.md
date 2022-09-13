# qilisensors
Code managing the collection, storage and monitoring of the data coming from the sensors in the lab

## Usage

1. Connect Shelly sensor to local network
2. Configure mqtt protocol and server IP from Shelly's configuration GUI (https://shelly-api-docs.shelly.cloud/gen1/#mqtt-configuration)
3. Deploy docker services:
`docker-compose up -d`
4. Connect to graphana on `localhost:3000`
5. Configure data source to InfluxDB `emeter` 
6. Upload json configuration of the dashboard

![](dash.png)

