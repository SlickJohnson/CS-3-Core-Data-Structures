"""Module to help check the cost for calling a number."""


def get_route_cost(number, routes):
    """Return the cost for calling the given number.

    Args:
        number: str -- the number who's cost will be found.
        routes: list -- a list with all the carrier routes and costs.

    Complexity:
        Best:
        Worst:

    Returns:
        str: the cost for calling the number.

    """


def __run_scenario_1():
    """Check cost one time.

    100k carrier routes and a single phone number.
    """
    print("""
    Open route-costs-106000.txt, and simply search using `CMD/CTRL + F`
        and find the longest match.
    Very fast and simple, but requires manual labour.
    """)


def __run_scenario_2():
    """Check cost for a list of numbers."""
    print("Not yet completed...")


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
