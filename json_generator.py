import json

dict = {}
strikes = [2000, 2100, 2200, 2250, 2300, 2350, 2375, 2385, 2390, 2395, 2400, 2405, 2410, 2425, 2450, 2475, 2500, 2525, 2550, 2575, 2600]
for strike in strikes:
    dict[strike] = {}
    for j in ["call", "tau", "put"]:
        dict[strike][j] = {}
        for k in ["July", "August", "September", "December", "March", "June"]:
            dict[strike][j][k] = input(f"{strike, k, j} price: ")
        

# Serializing json
json_object = json.dumps(dict, indent=4)
 
# Writing to sample.json
with open("2401_strike.json", "w") as outfile:
    outfile.write(json_object)