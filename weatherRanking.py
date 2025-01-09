
# Basic Temperature

# ranges
REALLY_COLD = (-100, -5) # cold pant + cold shirt + coat
COLD = (-5, 10) # cold pant + cold shirt
MEDIUM = (10, 20) # cold pant + hot shirt
HOT = (20, 100)   # hot pant + hot shirt

# Basic Conditions
RAIN = "raining"
WIND = "windy"

# clothing 
COLD_PANTS = "jeans", "pants", "snow pants", "leggings", "sweat pants"
COLD_TOPS = "sweater", "hoodie", "long sleeve"
COATS = "coat", "jacket", "puffer"
HOT_PANTS = "shorts", "skirt", "cargo shorts", "swim trunks"
HOT_SHIRTS = "tee shirt", "tee", "tank top", "crop top", "polo"
RAIN_CLOTH = "rain coat", "rain jacket", "hat", "rain pant"
WIND_CLOTH = "rain coat", "coat"

def find_conditions(temp, rain, wind):
    # windy = is_windy(wind)
    # rainy = is_raining(rain)

    really_cold = is_reallycold(temp)
    cold = is_reallycold(temp)
    medium = is_medium(temp)

    if really_cold:
        return "really cold", (COLD_PANTS, COLD_TOPS)
    elif cold:
        return "cold", (COLD_PANTS, COLD_TOPS)
    elif medium: 
        return "medium", (COLD_PANTS, HOT_SHIRTS)
    else:
        return "hot", (HOT_PANTS, HOT_SHIRTS)



# methods to find out temp ranking
def is_reallycold(temp):
    return temp in REALLY_COLD

def is_medium(temp):
    return temp in MEDIUM

def is_cold(temp):
    return temp in COLD

def is_hot(temp): 
    return temp in HOT

# def is_raining(rain):
#     return rain in RAIN

# def is_windy(wind):
#     return wind in WIND
