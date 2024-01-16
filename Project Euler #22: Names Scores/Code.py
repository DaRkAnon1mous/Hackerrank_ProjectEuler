def calculate_name_score(name):
    # Function to calculate the alphabetical value of a name
    return sum(ord(char) - ord('A') + 1 for char in name)

def name_score_queries(names, queries):
    # Sort the names alphabetically
    sorted_names = sorted(names)

    # Create a dictionary to store the position of each name in the sorted list
    position_dict = {name: i + 1 for i, name in enumerate(sorted_names)}

    # Process each query and print the corresponding score
    for query in queries:
        name = query.strip()
        score = calculate_name_score(name) * position_dict[name]
        print(score)

# Input
n = int(input().strip())
names = [input().strip() for _ in range(n)]

q = int(input().strip())
queries = [input().strip() for _ in range(q)]

# Output
name_score_queries(names, queries)
