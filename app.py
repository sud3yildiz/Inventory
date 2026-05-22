# app.py - Cafe Nova Inventory and Cost Calculator

def calculate_revenue(portions, price_per_portion):
    """Calculates the total revenue based on portions sold."""
    return portions * price_per_portion

def ingredient_cost(flour_kg, oil_liters):
    """Calculates the basic cost based on the amount of flour and oil."""
    # Assume flour is 3 PLN per kg, oil is 8 PLN per liter
    return (flour_kg * 3.0) + (oil_liters * 8.0)

if __name__ == "__main__":
    print(f"Revenue for 100 portions (15 PLN per portion): {calculate_revenue(100, 15)}")
    print(f"Cost of 5 kg flour and 10 liters of oil: {ingredient_cost(5, 10)}")

def bulk_discount(total_price):
    """Applies a 10% discount for orders above 1000 PLN."""
    if total_price > 1000:
        return total_price * 0.90
    return total_price