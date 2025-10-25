import datetime
from math import degrees, radians, cos, sin
from pysolar.solar import get_altitude, get_azimuth
from geopy.distance import distance

# Function to get the left and right side directions based on bus heading
def side_heading(bus_heading):
    # bus_heading in degrees from North (0-360)
    # Right side is 90° clockwise, Left side is 90° counter-clockwise
    right = (bus_heading + 90) % 360
    left = (bus_heading - 90) % 360
    return left, right

# Estimate sunlight exposure for a side based on sun azimuth
def sunlight_exposure(bus_lat, bus_lon, bus_heading, time_utc):
    # Get current sun azimuth and altitude
    sun_alt = get_altitude(bus_lat, bus_lon, time_utc)
    sun_az = get_azimuth(bus_lat, bus_lon, time_utc)

    # Determine left/right side headings
    left_dir, right_dir = side_heading(bus_heading)
    
    # Calculate angular difference between sun and each side
    diff_left = min(abs(sun_az - left_dir), 360 - abs(sun_az - left_dir))
    diff_right = min(abs(sun_az - right_dir), 360 - abs(sun_az - right_dir))

    # Smaller difference means more sunlight exposure
    if diff_left < diff_right:
        exposure = "Left side exposed more to sunlight"
    elif diff_right < diff_left:
        exposure = "Right side exposed more to sunlight"
    else:
        exposure = "Both sides receive equal sunlight"
    
    return exposure, sun_az, sun_alt
