# input_handler/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import LogEntry
from .forms import UserInputForm
from urllib.parse import unquote
import os
import logging
import cloudmersive_security_api_client
from cloudmersive_security_api_client.rest import ApiException
from geo_ip_track.utils import fetch_and_log_geolocation
from sqlalchemy.exc import IntegrityError

# Configure API key authorization
API_KEY = os.getenv('SQL_API_KEY')
configuration = cloudmersive_security_api_client.Configuration()
configuration.api_key['Apikey'] = API_KEY
api_instance = cloudmersive_security_api_client.ContentThreatDetectionApi(cloudmersive_security_api_client.ApiClient(configuration))

# Define a list of suspicious characters
suspicious_chars = ["'", '"', "`", ";", "--", "#", "/*", "*/"]

def index(request):
    warning = None
    input_disabled = False
    is_sql_injection = False  # Initialize to False

    if not os.getenv('SQL_API_KEY'):
        logging.warning('Warning: SQL_API_KEY IS NOT SET')
        warning = "Input is currently blocked due to missing API key. Please contact the administrator."
        input_disabled = True

    if request.method == 'POST' and not input_disabled:
        form = UserInputForm(request.POST, disabled=input_disabled)
        if form.is_valid():
            user_input = form.cleaned_data['input_text']
            client_ip = request.META.get('REMOTE_ADDR', '')

            decoded_input = unquote(user_input)
            contains_suspicious_chars = any(char in decoded_input for char in suspicious_chars)

            if contains_suspicious_chars:
                response = check_sql_injection(decoded_input)
                if response in [-12, -13, -14]:
                    warning = "Unable to perform security check at this time. Please try again later."
                    logging.error(f"SQL injection check failed. Error code: {response}")
                elif response is not None:
                    is_sql_injection = response.contained_sql_injection_attack
                else:
                    warning = "An unexpected error occurred. Please try again later."
                    logging.error("Unexpected None response from check_sql_injection")

                if is_sql_injection:
                    warning = "Your input cannot be processed at this time. Please try again later."
                    logging.warning(f'Potential SQL Injection detected: {decoded_input}')
                    
                    geo_location = fetch_and_log_geolocation(client_ip)
                    if geo_location:
                        logging.warning(f"Geolocation of potential attacker: {geo_location}")
                else:
                    logging.info(f'Input passed security check: {decoded_input}')

            LogEntry.objects.create(
                client_ip=client_ip,
                user_input=decoded_input,
                is_sql_injection=is_sql_injection  # Always pass this value
            )
    else:
        form = UserInputForm(disabled=input_disabled)

    return render(request, 'input_handler/index.html', {
        'form': form, 
        'warning': warning, 
        'input_disabled': input_disabled
    })
def check_sql_injection(input_text):
    try:
        api_response = api_instance.content_threat_detection_check_sql_injection_string(input_text)
        return api_response
    except ApiException as e:
        if e.status == 401:
            logging.error(f"Unauthorized: Invalid API key for SQL injection check")
            return -14  # Custom error code for unauthorized access
        logging.error(f"Exception when calling ContentThreatDetectionApi->content_threat_detection_check_sql_injection_string: {e}")
        return -13
        return None