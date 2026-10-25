# Data sources

- Station readings: CPCB stations via the WAQI feed (token required; data are unvalidated and may have gaps).
- Forecast shape: Open-Meteo air-quality API (CAMS global model). Good for when, not where inside a city. Attribute CAMS and Open-Meteo.
- Road network: OpenStreetMap (informal roads may be missing).
- AQI is not concentration: prefer raw PM2.5, and check which AQI breakpoints a feed uses before converting.
