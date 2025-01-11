
# Basic Temperature

# # ranges
# REALLY_COLD = (-100, -5) # cold pant + cold shirt + coat
# COLD = (-5, 10) # cold pant + cold shirt
# MEDIUM = (10, 20) # cold pant + hot shirt
# HOT = (20, 100)   # hot pant + hot shirt

# Basic Conditions
RAIN = "rain", "drizzle", "thunderstorm"
WIND = "windy"

# clothing !!todo edit the tagging options to be more specific!!
COLD_PANTS = "pants", "pants"
COLD_TOPS = "sweater", "shirt", "coat"
COATS = "coat" ,"coat"
HOT_PANTS = "shorts", "skirt", "dress",
HOT_SHIRTS = "shirt", "shirt"
RAIN_CLOTH = "raincoat","raincoat"
WIND_CLOTH = "rain coat", "coat"

def find_conditions(temp, rain, wind):
    # windy = is_windy(wind)
    # rainy = is_raining(rain)

    really_cold = is_reallycold(temp)
    cold = is_cold(temp)
    medium = is_medium(temp)

    if really_cold:
        if is_raining(rain):
            return "really cold", (COLD_PANTS, COLD_TOPS, RAIN_CLOTH)
        else:
            return "really cold", (COLD_PANTS, COLD_TOPS)
    elif cold:
        if is_raining(rain):
            return "cold", (COLD_PANTS, COLD_TOPS, RAIN_CLOTH)
        else:
            return "cold", (COLD_PANTS, COLD_TOPS)
    elif medium: 
        if is_raining(rain):
            return "medium", (COLD_PANTS, HOT_SHIRTS, RAIN_CLOTH)
        else:
            return "medium", (COLD_PANTS, HOT_SHIRTS)
    else:
        if is_raining(rain):
            return "hot", (HOT_PANTS, HOT_SHIRTS, RAIN_CLOTH)
        else:
            return "hot", (HOT_PANTS, HOT_SHIRTS)



# methods to find out temp ranking
def is_reallycold(temp):
    return -100 <= temp < -5

def is_medium(temp):
    return -5 <= temp < 10

def is_cold(temp):
    return 10 <= temp < 20

def is_hot(temp): 
    return 20 <= temp <= 100

def is_raining(rain):
    return any(keyword in rain for keyword in RAIN)

# def is_windy(wind):
#     return wind in WIND
