# Description

Grafana & InfluxDB in Docker containers for body meassurments tracking and analytics. Based on these measurments the service calculates the following

- BMI
- Body Density
- Percentage of Muscle/Fat mass
- Kg of Muscle/Fat mass

After calculations the data is stored in the DB an displayed in the Grafana Dashboard. The Dashboard contains indicators and thresholds that can be configured for every person needs.

# How to run

From the project folder add the body measurements in the `data/body_data.csv` file. Start Docker and then from the command line:

```bash
docker-compose build
docker-compose up
```

The Grafana service should be available at [localhost:3000](http://127.0.0.1:3000) with user and password set to `admin`
