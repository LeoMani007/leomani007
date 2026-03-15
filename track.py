import phonenumbers
from phonenumbers import geocoder, carrier, timezone

number_to_track = input("enter the phone number : ")

try:
    parsed_number = phonenumbers.parse(number_to_track)
    is_valid = phonenumbers.is_valid_number(parsed_number)
    print(f"Tracking Number: {number_to_track}")
    print(f"Is Valid: {is_valid}")

    if is_valid:
        # Get geographical location
        location = geocoder.description_for_number(parsed_number, "en")
        print(f"Location: {location}")

        # Get service provider (carrier)
        service_provider = carrier.name_for_number(parsed_number, "en")
        print(f"Carrier: {service_provider}")

        # Get Timezone
        tz = timezone.time_zones_for_number(parsed_number)
        print(f"Timezone: {tz}")

except phonenumbers.NumberParseException as e:
    print(f"Error parsing number: {e}")