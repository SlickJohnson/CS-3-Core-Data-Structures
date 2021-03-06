"""Module to help check the cost for calling a number."""
from strings import find_index


def get_call_cost(number, routes_costs):
    """Return the cost for calling the given number.

    Args:
        number: str -- the number who's cost will be found.
        routes: list -- a list with all the carrier routes

    Complexity:
        Best:
        Worst:

    Returns:
        str: the cost for calling the number.

    """
    cheapest_route = routes_costs[0]
    # loop through each route-cost pair in the list provided.
    # O(e), e is the number of entries in routes_costs
    for route, cost in routes_costs:
        # check if route is usable for calling this number.
        # O(nr), n is the length of the number and r the length of the route.
        if find_index(number, route) == 0:
            # look for the cheapest and longest match
            is_longer_match = len(route) > len(cheapest_route[0])  # O(1)
            is_same_len = len(route) == len(cheapest_route[0])  # O(1)
            is_cheaper_route = float(cost) < float(cheapest_route[1])  # O(1)

            if is_longer_match or (is_same_len and is_cheaper_route):  # O (1)
                cheapest_route = [route, cost]  # O(1)

    return cheapest_route[1]  # O(1)


def get_call_costs(numbers, routes):
    """Return the costs for calling a list of numbers.

    Args:
        number: list -- the numbers who's cost will be found.
        routes: list -- a list with all the carrier routes and costs.

    Complexity:
        Best:
        Worst:

    Returns:
        list: the costs for calling each number.

    """
    call_costs = []
    for number in numbers:
        cost = get_call_cost(number, routes)
        call_costs.append('{},{}'.format(number, cost))

    return call_costs


def __run_scenario_1():
    """Check cost one time.

    100k carrier routes and a single phone number.
    """
    print("""
    Open route-costs-106000.txt, and simply search using `CMD/CTRL + F`
        and find the longest match. Paste the number and cost in
        route-costs-1.txt
    Very fast and simple, but requires manual labour.
    """)


def __run_scenario_2():
    """Check cost for a list of numbers.

    100k routes and 1000 phone numbers
    """
    print('Very, very, very slow, but it\'s operationalized.\nAlmost done....')
    # Get the list of carrier routes.
    with open('input/route-costs/route-costs-106000.txt') as txt_file:
        entries = txt_file.read().rsplit()
        routes_costs = [entry.split(',') for entry in entries]
    # Get the list of phone numbers.
    with open('input/phone-numbers/phone-numbers-1000.txt') as txt_file:
        phone_numbers = txt_file.read().rsplit()
    # Get the costs for each number.
    costs = get_call_costs(phone_numbers, routes_costs)
    with open('output/route-costs-2.txt') as txt_file:
        for cost in costs:
            # Write the costs to the output.
            txt_file.write('{}\n'.format(cost))


def __run_scenario_3():
    """Check cost with multiple long carrier route lists."""
    print("Not yet completed...")


def __run_scenario_4():
    """High-throughput pricing API."""
    print("Not yet completed...")


def __run_scenario_5():
    """Check cost with Changing carrier route lists."""
    print("Not yet completed...")


if __name__ == "__main__":
    import sys
    args = sys.argv
    if len(args) > 1:
        # determines what scenario is going to run.
        scenario_number = int(args[1])
        scnarios = {
            1: __run_scenario_1,
            2: __run_scenario_2,
            3: __run_scenario_3,
            4: __run_scenario_4,
            5: __run_scenario_5
        }.get(scenario_number)()
