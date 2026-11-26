"""
Case Study 2: Progressive Electricity Billing
Slab arithmetic with loops; fixed charge, cess and rebate with conditionals.
"""

SLABS = [(100, 5.0), (300, 7.0), (500, 9.0), (10000000, 12.0)]
FIXED_CHARGE = 50.0
CESS_RATE = 0.02
REBATE_RATE = 0.05
UNUSUAL_LIMIT = 0.30

# Month records are tuples: (month name, units consumed)
MONTHS = [("Jun", 180), ("Jul", 245), ("Aug", 390), ("Sep", 310), ("Oct", 268)]


def slab_charge(units):
    charge = 0.0
    lower = 0
    remaining = units
    for upper, rate in SLABS:
        if remaining <= 0:
            break
        in_slab = remaining
        if upper - lower < in_slab:
            in_slab = upper - lower
        charge = charge + in_slab * rate
        remaining = remaining - in_slab
        lower = upper
    return charge


def compute_bill(units, previous_units):
    energy = slab_charge(units)
    cess = energy * CESS_RATE
    rebate = 0.0
    if previous_units != -1 and units < previous_units:
        rebate = energy * REBATE_RATE
    total = energy + FIXED_CHARGE + cess - rebate
    return (units, round(energy, 2), round(cess, 2), round(rebate, 2), round(total, 2))


def main():
    bills = []
    previous = -1
    for month, units in MONTHS:
        bills.append((month, compute_bill(units, previous)))
        previous = units

    print("=" * 76)
    print("PROGRESSIVE ELECTRICITY BILL")
    print("=" * 76)
    print("%-6s %7s %9s %8s %8s %10s" %
          ("Month", "Units", "Energy", "Cess", "Rebate", "Total"))
    for month, bill in bills:
        print("%-6s %7d %9.2f %8.2f %8.2f %10.2f" %
              (month, bill[0], bill[1], bill[2], bill[3], bill[4]))

    print("\nMONTH ON MONTH COMPARISON")
    for i in range(1, len(bills)):
        old_month, old = bills[i - 1]
        new_month, new = bills[i]
        change = (new[0] - old[0]) / old[0]
        note = ""
        if change > UNUSUAL_LIMIT:
            note = "  UNUSUAL INCREASE"
        elif change < 0:
            note = "  rebate applied"
        print("%s to %s: %+.1f%%%s" %
              (old_month, new_month, change * 100, note))


if __name__ == "__main__":
    main()
