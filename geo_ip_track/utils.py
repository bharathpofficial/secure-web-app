import os
import requests
import logging
from .models import IPGeoLocation

IPGEO_API_KEY = os.getenv('IPGEO_API_KEY')
logger = logging.getLogger(__name__)

def fetch_and_log_geolocation(ip_address):
    if not IPGEO_API_KEY:
        logger.error("IPGEO_API_KEY is not set")
        return None

    if ip_address == '127.0.0.1':
        ip_address = '1.1.1.1'
    url = f'https://api.ipgeolocation.io/ipgeo?apiKey={IPGEO_API_KEY}&ip={ip_address}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            ip_geo_location = IPGeoLocation.objects.create(
                ip_address=ip_address,
                country_name=data.get('country_name', 'Unknown'),
                city=data.get('city', 'Unknown'),
                latitude=data.get('latitude'),
                longitude=data.get('longitude')
            )
            logger.info(f"Geolocation data fetched and logged for IP: {ip_address}")
            return ip_geo_location
        elif response.status_code == 401:
            logger.error(f"Invalid IPGEO_API_KEY provided")
        elif response.status_code == 423:
            logger.warning(f"Resource is locked. Status code: {response.status_code}")
        else:
            logger.error(f"Unexpected status code: {response.status_code}")

    except requests.RequestException as e:
        logger.error(f"Error fetching geolocation data: {e}")
    except Exception as e:
        logger.exception(f"Unexpected error in fetch_and_log_geolocation: {e}")
    return None