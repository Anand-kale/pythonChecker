import sys

# Print 'Hello World'
print('Hello World')

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: python main.py <env_variable_value>")
    sys.exit(1)

# Retrieve the environment variable value from the command-line arguments
env_variable_value = sys.argv[1]

# Print the value of the environment variable
print(f'Environment Variable Value: {env_variable_value}')
