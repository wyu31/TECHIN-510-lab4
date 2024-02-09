import streamlit as st
import time
import datetime
import zoneinfo
import freecurrencyapi

# Initialize the client with your API key
client = freecurrencyapi.Client('fca_live_6wQ9YxGc6LVK2qXk7raszT4tlNg6Tfm8lTP8oNpH')

# App layout and navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page:", ["World Clock", "World Currency"])

if page == "World Clock":
    st.title("World Clock")

    # List of available time zones
    zone_list = zoneinfo.available_timezones()

    # Multiselect for users to choose time zones
    selected_zones = st.multiselect(
        'Which time zones do you want to see?',
        zone_list,
        default=['America/Los_Angeles'],
        max_selections=4
    )

    # Creating tabs for different functionalities
    tab1, tab2, tab3 = st.tabs(["Standard Format", "UNIX Format", "UNIX Timestamp Converter"])

    # Placeholders for time in standard and UNIX formats
    time_placeholders_1 = [tab1.empty() for _ in selected_zones]
    time_placeholders_2 = [tab2.empty() for _ in selected_zones]

    # Divider for better UI organization
    st.divider()

    # Handling UNIX Timestamp Converter in tab3
    with tab3:
        st.write("UNIX Timestamp Converter")
        unix_input = st.number_input("Enter UNIX Timestamp:", step=1, format="%d", key="unix_timestamp_input")
        convert_button = st.button("Convert to Human-Readable Time", key="convert")

        if convert_button and unix_input:
            # Convert UNIX timestamp to human-readable format
            human_time = datetime.datetime.fromtimestamp(unix_input).strftime('%Y-%m-%d %H:%M:%S')
            st.write(f"Human-readable time: {human_time}")
        elif convert_button:
            # Show error if the button is pressed but no input is provided
            st.error("Please enter a valid UNIX timestamp.")

    # Loop to update the time displays
    cnt = 0
    while True:
        for i, zone in enumerate(selected_zones):
            # Getting the current time in the selected time zone
            current_time = datetime.datetime.now(tz=zoneinfo.ZoneInfo(zone))
            # Displaying the time in standard format
            time_placeholders_1[i].metric(label=f"{zone}: ", value=f"{current_time.strftime('%Y-%m-%d %H:%M:%S')}")
            # Displaying the time in UNIX format
            time_placeholders_2[i].metric(label=f"{zone}: ", value=f"{int(current_time.timestamp())}")
    
        # Wait for 1 second before updating again
        time.sleep(1)

elif page == "Currency":
    st.title('Currency Converter')

# Initialize variables for exchange rate to display it before the conversion is performed.
exchange_rate_displayed = False
exchange_rate = None

# Directly fetch and prepare currency options for selection.
currency_data = client.currencies(currencies=[
    "EUR", "USD", "JPY", "BGN", "CZK", "DKK", "GBP", "HUF", "PLN", "RON", "SEK", "CHF", 
    "ISK", "NOK", "HRK", "RUB", "TRY", "AUD", "BRL", "CAD", "CNY", "HKD", "IDR", "ILS", 
    "INR", "KRW", "MXN", "MYR", "NZD", "PHP", "SGD", "THB", "ZAR"
])
currency_options = [f"{code} - {info['name']}" for code, info in currency_data['data'].items()]

# UI for selecting base and target currencies.
col1, col2 = st.columns(2)

with col1:
    option1 = st.selectbox('Select base currency', currency_options, index=1)
    base_currency = option1.split(' - ')[0]  # Extracting the currency code

with col2:
    option2 = st.selectbox('Select the currency you want to convert to', currency_options, index=0)
    target_currency = option2.split(' - ')[0]  # Extracting the currency code

# Immediately fetch the exchange rate upon currency selection and display it near the title.
if not exchange_rate_displayed:
    exchange_rate = client.latest(base_currency=base_currency, currencies=[target_currency])['data'][target_currency]
    st.subheader(f"Real-time exchange rate: 1 {base_currency} = {exchange_rate} {target_currency}")
    exchange_rate_displayed = True

# Currency Converter Section
st.header("Currency Converter")

# Input for the amount to convert.
number = st.number_input('Enter amount to convert', min_value=0.0, value=1.0)

# Button to perform conversion. This could also be done automatically without a button.
if st.button('Convert'):
    if not exchange_rate:  # Fetch the rate again if not already done (for safety, but can be optimized)
        exchange_rate = client.latest(base_currency=base_currency, currencies=[target_currency])['data'][target_currency]
    converted_value = exchange_rate * number
    
    # Display the conversion result
    st.write(f"{number} {base_currency} is approximately {converted_value} {target_currency}")