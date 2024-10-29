import random

# You can run this file using the following command:
# python -m homework03


def first_entree_time_of_rolling_six():
    """
    Simulates rolling a six-sided die until a six is rolled and returns the number of attempts taken.
    This function uses a while loop to repeatedly roll a six-sided die (with values from 1 to 6) 
    until a six is rolled. It counts the number of attempts taken to roll a six and returns this count.
    Returns:
        int: The number of attempts taken to roll a six.
    """
    # Counter for execution of line 3 of the algorithm
    counter = 0
    ### YOUR CODE HERE ###
    ...
    ### END OF YOUR CODE ###  
    print(f"Counted execusions: {counter}")      
    return X

def simulate_n_draws(n):
    """
    Simulates n independent and identically distributed (iid) draws of the first_entree_time_of_rolling_six function.
    
    Args:
        n (int): The number of iid draws to simulate.
    
    Returns:
        list: A list containing the results of the n iid draws.
    """
    results = []
    ### YOUR CODE HERE ###
    ...
    ### END OF YOUR CODE ### 
    return results

if __name__ == "__main__":
    print("Simulating the first entree time of rolling a six:")
    first_attempts = first_entree_time_of_rolling_six()
    print(f"First entree time of rolling a six: {first_attempts}")

    print("\nSimulating 10 draws of the first entree time of rolling a six:")
    draws = simulate_n_draws(10)
    print(f"Results of 10 draws: {draws}")