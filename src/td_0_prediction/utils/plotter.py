import matplotlib.pyplot as plt

def plot_state_values(states, true_values, estimated_values):
    """
    Plots the true values and estimated values for each state.

    :param states: List of state names (e.g., ['A', 'B', 'C', ...])
    :param true_values: List of true values corresponding to the states
    :param estimated_values: List of lists containing estimated values for each state over iterations
    """
    
    # Create a figure and axis
    plt.figure(figsize=(10, 6))
    
    # Plot the true values (these will be constant across all iterations)
    plt.plot(states, true_values, label='True Values', color='black', linestyle='--', marker='o')
    
    # Plot estimated values over iterations
    for i, estimate in enumerate(estimated_values):
        plt.plot(states, estimate, label=f'Iteration {i+1}', linestyle='-', marker='x')
    
    # Adding labels and title
    plt.xlabel('States')
    plt.ylabel('Values')
    plt.title('True vs Estimated Values of States')
    plt.legend()
    plt.grid(True)
    
    # Show plot
    plt.tight_layout()
    plt.savefig("True vs Estimated Values of States.png")
    plt.show()

if __name__ == "__main__":
    # Example usage
    states = ['A', 'B', 'C', 'D']
    true_values = [0.8, 0.6, 0.4, 0.2]
    estimated_values = [
        [0.5, 0.4, 0.3, 0.2],
        [0.7, 0.5, 0.35, 0.25],
        [0.75, 0.55, 0.4, 0.3]
    ]

    plot_state_values(states, true_values, estimated_values)
