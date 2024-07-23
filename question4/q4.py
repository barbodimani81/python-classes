import jdatetime

# Get the Gregorian date from the user
date_str = input("Enter a date in the format YYYY-MM-DD: ")

# Split the input string into year, month, and day components
year, month, day = map(int, date_str.split('-'))

# Create a jdatetime.datetime object representing the Gregorian date
gregorian_datetime = jdatetime.datetime(year, month, day)

# Convert the Gregorian datetime to a Jalali (Persian) datetime
jalali_datetime = gregorian_datetime.togregorian()

# Print the converted Jalali datetime
print(f"Jalali date and time: {jalali_datetime.strftime('%Y-%m-%d %H:%M:%S')}")