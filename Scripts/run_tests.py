import subprocess
import os

def run_behave_tests():
    # Ensure the reports directory exists
    reports_dir = 'reports/allure-results'
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)
    
    # Run Behave tests with error handling
    try:
        result = subprocess.run(
            ['behave', '-f', 'allure_behave.formatter:AllureFormatter', '-o', reports_dir, 'features'],
            check=True,  # This will raise an error if the command fails
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        # Print the output of the Behave tests (stdout and stderr)
        print(result.stdout.decode())
        print(result.stderr.decode())
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running Behave tests: {e}")
        print(f"stdout: {e.stdout.decode()}")
        print(f"stderr: {e.stderr.decode()}")

# Run the tests
run_behave_tests()

