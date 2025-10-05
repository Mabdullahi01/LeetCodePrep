"""
The main idea here is to imagine every currency as a node in a graph

We will then traverse the graph starting from the original currency to the target currency
Any intermediate currency's rate that we encountered will be multiplied with the current rate to get the new fx rate

Our task is basically to find all path from original currency vertex to the target currency vertex, but really we don't
need all the paths, we need to evaluate the maximum rate encountered so far

I made the solution extensible by using a map to store all max rate from original currency to all currencies, this means
 we can get any max rate in constant time


"""

from collections import defaultdict, deque
import sys
import re


def validate_input(rates, original_currency, target_currency):
    # Validate rate format
    rate_pattern = re.compile(r'^[A-Z]{3},[A-Z]{3},\d+(\.\d+)?$')
    for rate in rates:
        if not rate_pattern.match(rate):
            raise ValueError(f"Invalid rate format: {rate}")

    # Validate currency format
    currency_pattern = re.compile(r'^[A-Z]{3}$')
    if not currency_pattern.match(original_currency):
        raise ValueError(f"Invalid original currency format: {original_currency}")
    if not currency_pattern.match(target_currency):
        raise ValueError(f"Invalid target currency format: {target_currency}")

# Time complexity: O(V + E), where V is the number of currencies (vertices) and E is the number of exchange rates (edges).
# Space complexity: O(V) for storing the queue.
def max_currency_exchange(rates, original_currency, target_currency):
    # Validate input
    try:
        validate_input(rates, original_currency, target_currency)
    except ValueError as e:
        # print(f"Input validation error: {e}")
        return -1.0

    # Build the graph as an adjacency list
    graph = defaultdict(list)

    # Parse the rates and build the graph
    for rate in rates:
        try:
            from_currency, to_currency, rate_value = rate.split(',')
            rate_value = float(rate_value)
            if rate_value <= 0:
                raise ValueError(f"Exchange rate must be positive: {rate}")
            graph[from_currency].append((to_currency, rate_value))
        except ValueError as e:
            # print(f"Error parsing rate: {e}")
            return -1.0

    # Check if original and target currencies exist in the graph
    if original_currency not in graph and original_currency not in {to for rates in graph.values() for to, _ in rates}:
        # print(f"Original currency {original_currency} not found in exchange rates")
        return -1.0
    if target_currency not in graph and target_currency not in {to for rates in graph.values() for to, _ in rates}:
        # print(f"Target currency {target_currency} not found in exchange rates")
        return -1.0

    # Perform BFS to find the maximum exchange rate
    queue = deque([(original_currency, 1.0)])
    max_values = defaultdict(float)
    max_values[original_currency] = 1.0

    while queue:
        currency, current_value = queue.popleft()

        # Explore all adjacent currencies
        for next_currency, rate in graph[currency]:
            new_value = current_value * rate
            if new_value > max_values[next_currency]:
                max_values[next_currency] = new_value
                queue.append((next_currency, new_value))

    # Return the maximum value for the target currency, or -1.0 if not reachable
    return max_values[target_currency] if max_values[target_currency] > 0 else -1.0


if __name__ == "__main__":
    try:
        input_data = []
        for line in sys.stdin:
            input_data.append(line.strip())
        # Validate length of input
        if len(input_data) != 3:
            raise ValueError("Invalid input format. Expected 3 lines of input.")

        fx_rates = input_data[0].split(';')
        original_currency = input_data[1]
        target_currency = input_data[2]

        # Calculate maximum currency exchange value
        result = max_currency_exchange(fx_rates, original_currency, target_currency)
        print(f"{result:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

