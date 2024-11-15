from amadeus import Client, ResponseError


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
