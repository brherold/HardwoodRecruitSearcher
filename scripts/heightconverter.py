import math
#Converts String height in feet and inches to inches (float/int type)
#6'11" -> 83.0
def convert_to_inches(height):
    parts = height.split("'")
    if len(parts) == 2:
        feet = int(parts[0])
        inches_str = parts[1].rstrip('"').strip()  # Removing leading/trailing whitespace
        if inches_str:  # Check if inches part is not empty
            if '½' in inches_str:
                inches_str = inches_str.replace('½', '.5')
            elif '¼' in inches_str:
                inches_str = inches_str.replace('¼', '.25')
            inches = float(inches_str)
        else:
            inches = 0
    elif len(parts) == 1:
        feet = int(parts[0])
        inches = 0
    else:
        return None
    return (feet * 12) + inches
#Converts Float/Int inches to String feet and inches (remove any fractional inches)
#83.0 -> 6'11"
def convert_to_feet(height):
    #find inches by doing mod 12
    feet = int(height // 12)
    inches = math.floor(height % 12)
    heightString = str(feet) + "'" + str(inches)
    return heightString
