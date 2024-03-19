import itertools

def evaluate(expression):
    for assignment in itertools.product([False, True], repeat=2):
        result = eval(expression, {"p": assignment[0], "q": assignment[1]})
        print("{:^5} | {:^5} | {:^5} ".format(str(assignment[0]), str(assignment[1]), str(result)))

def truth_table(expression):
    header = "{:^5} | {:^5} | {:^5}".format("p", "q", expression)
    separator = "-" * len(header)
    print(header)
    print(separator)
    evaluate(expression)

# Example usage:
truth_table("p and q")

