import random
import sys
import json

def main():
    strategies = ["Call", "Put", "Straddle", "Strangle", "Call Spread", "Put Spread"]
    # Additional: "call time fly", "put time fly", "stupid",  "Butterfly", "Call time spread", "Put time spread"
    tied_to = [0, 1]
    strikes = [2000, 2100, 2200, 2250, 2300, 2350, 2375, 2385, 2390, 2395, 2400, 2405, 2410, 2425, 2450, 2475, 2500, 2525, 2550, 2575, 2600]
    months = ["July", "August", "September", "December", "March", "June"]
    strategy = strategies[random.randint(0, 5)]
    underlying = tied_to[random.randint(0, 1)]

    if strategy == "Call" or strategy == "Put" or strategy == "Straddle":
        strike = strikes[random.randint(0, len(strikes) - 1)]
        month = months[random.randint(0, len(months) - 1)]
        print(f"Tied to {underlying} price the {month} {strike} {strategy}")

    elif strategy == "Strangle" or strategy == "Put Spread" or strategy == "Call Spread":
        strike_one = strikes[random.randint(0, len(strikes) - 1)]
        strike_two = strikes[random.randint(0, len(strikes) - 1)]
        while strike_one == strike_two:
            strike_two = strikes[random.randint(0, len(strikes))]
        month = months[random.randint(0, len(months) - 1)]
        print(f"Tied to {underlying} price the {month} {min(strike_one, strike_two)} {max(strike_one, strike_two)} {strategy}")
        # TODO: Add in gut strangles
    
    file = "2400_strikes.json" if underlying == 0 else "2401_strikes.json"
    input()

    with open(file) as f:
        strikes_info_2400 = json.load(f)
    
    if strategy == "Call" or strategy == "Put":
        tv = round(float(strikes_info_2400[f"{strike}"][strategy.lower()][month]), 2)
        tau = float(strikes_info_2400[f"{strike}"]["tau"][month]) * .1
        print(tv)
        plus = round(tv + tau, 2)
        minus = round(tv - tau, 2)

    elif strategy in ["Call Spread", "Put Spread"]:
        tv = round(abs(float(strikes_info_2400[f"{strike_one}"][strategy.split()[0].lower()][month]) - float(strikes_info_2400[f"{strike_two}"][strategy.split()[0].lower()][month])), 2)
        print(float(strikes_info_2400[f"{strike_one}"][strategy.split()[0].lower()][month]))
        print(float(strikes_info_2400[f"{strike_two}"][strategy.split()[0].lower()][month]))
        plus = round(tv + .1, 2)
        minus = round(tv - .1, 2)
 
    elif strategy == "Straddle":
        tv = round(abs(float(strikes_info_2400[f"{strike}"]["put"][month]) + float(strikes_info_2400[f"{strike}"]["call"][month])), 2)
        print(float(strikes_info_2400[f"{strike}"]["call"][month]))
        print(abs(float(strikes_info_2400[f"{strike}"]["put"][month])))
        tau = float(strikes_info_2400[f"{strike}"]["tau"][month]) * 2 / 10
        plus = round(tv + tau, 2)
        minus = round(tv - tau, 2)

    
    elif strategy == "Strangle":
        tv = round(abs(float(strikes_info_2400[f"{min(strike_one, strike_two)}"]["put"][month]) + float(strikes_info_2400[f"{max(strike_one, strike_two)}"]["call"][month])), 2)
        print(float(strikes_info_2400[f"{min(strike_one, strike_two)}"]["put"][month]))
        print(float(strikes_info_2400[f"{max(strike_one, strike_two)}"]["call"][month]))
        tau = (float(strikes_info_2400[f"{strike_one}"]["tau"][month]) + float(strikes_info_2400[f"{strike_two}"]["tau"][month])) * .1
        plus = round(tv + tau, 2)
        minus = round(tv - tau, 2)
        
    print(f"TV: {tv}")
    print(f"Spread: {minus} at {plus}")
    input()
if __name__ == "__main__":
    print("Price the following options: ")
    for i in range(10):
        main()





