from amadeus import Client, ResponseError

# Replace with your API key and secret
#API_KEY = "H3iIn3ADdf0UxsLWeqVWhHu7XuISK5kZ"
#API_SECRET = "jQJIEIxIwWarKF4G"

# Initialize the Amadeus client
amadeus = Client(
    client_id="
)

try:
    response = amadeus.shopping.flight_offers_search.get(
        originLocationCode='MAD',
        destinationLocationCode='ATH',
        departureDate='2024-12-01',
        adults=1
    )
    print(response.data)
except ResponseError as error:
    print(f"An error occurred: {error}")
