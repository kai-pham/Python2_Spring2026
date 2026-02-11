#Program: Sort and count a bag of coins
#Author: Pham Huy Thang (Kai)
#Date: 02/09/2026

#The diameters of US coins
QUARTER_SIZE = 24
DIME_SIZE = 18
NICKEL_SIZE = 21
PENNY_SIZE = 19

#Value of US coins
QUARTER_VALUE = 0.25
DIME_VALUE = 0.10
NICKEL_VALUE = 0.05
PENNY_VALUE = 0.01

def tally_coin(coin_bag):
    """
    Tally the coins by its denomination using a for loop.
    Returns: q, d, n, p, f - the count of quarters, dimes, nickels, pennies, and foreign coins respectively. 
    """
    q = d = n = p = f = 0
    for coin in coin_bag:
        if coin == QUARTER_SIZE:
            q += 1
        elif coin == DIME_SIZE:
            d += 1
        elif coin == NICKEL_SIZE:
            n += 1
        elif coin == PENNY_SIZE:
            p += 1
        else:
            f += 1
    return q, d, n, p, f

def calculate_bag_value(q_count, d_count, n_count, p_count):
    """
    Calculate and return total value of the bag (float).
    Note: Foreign coins are NOT included in the value.
    """
    total_value = 0.0
    total_value += q_count * QUARTER_VALUE
    total_value += d_count * DIME_VALUE
    total_value += n_count * NICKEL_VALUE
    total_value += p_count * PENNY_VALUE
    return total_value

def display_coin_count(q, d, n, p, f):
    """
    Display each coin tally.
    """
    print(f"  {'Quarter:':<9}{q}")
    print(f"  {'Dime:':<9}{d}")
    print(f"  {'Nickel:':<9}{n}")
    print(f"  {'Penny:':<9}{p}")
    print(f"  {'Foreign:':<9}{f}")
    
def main():
    """
    Main function to execute the program logic.
    """
    bag_coin = [24, 32, 21, 18, 21, 24, 18, 24, 25, 18, 24, 18, 23, 21, 19, 24, 19, 20, 19, 20, 21, 19]
    q, d, n, p, f = tally_coin(bag_coin)
    total_value = calculate_bag_value(q, d, n, p)
    display_coin_count(q, d, n, p, f)
    print(f"Total value of the bag: ${total_value:.2f}")

if __name__ == "__main__":
    main()

