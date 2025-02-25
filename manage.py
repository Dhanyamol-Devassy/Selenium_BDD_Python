import sys
import os
import subprocess
import argparse
import shutil
from dotenv import load_dotenv  # Optional for loading .env files

# Define the root directory of the project
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# Define paths for reports and results
ALLURE_RESULTS_DIR = os.path.join(PROJECT_ROOT, 'reports', 'allure-results')
ALLURE_REPORT_DIR = os.path.join(PROJECT_ROOT, 'reports', 'allure-report')
SCREENSHOTS_DIR = os.path.join(PROJECT_ROOT, 'reports', 'screenshots')

def run_command(command):
    """Runs a shell command and handles errors."""
    try:
        subprocess.run(command, cwd=PROJECT_ROOT, check=True)
    except FileNotFoundError:
        print(f"Error: Command '{command[0]}' not found. Make sure it is installed and accessible.")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Error: Command '{' '.join(command)}' failed with exit code {e.returncode}")
        sys.exit(e.returncode)

def ensure_directory_exists(directory):
    """Creates a directory if it does not exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def run_behave(feature_file=None):
    """Runs Behave BDD tests."""
    print("Running Behave tests...")
    command = ['behave']
    if feature_file:
        command.append(feature_file)
    run_command(command)

def generate_allure_report():
    """Generates the Allure report from the test results."""
    print("Generating Allure report...")
    ensure_directory_exists(ALLURE_RESULTS_DIR)
    run_command(['allure', 'serve', ALLURE_RESULTS_DIR])

def clean_reports():
    """Cleans up old Allure results and screenshots."""
    print("Cleaning up reports...")
    for directory in [ALLURE_RESULTS_DIR, SCREENSHOTS_DIR]:
        if os.path.exists(directory):
            shutil.rmtree(directory)
            print(f"Deleted: {directory}")
        else:
            print(f"Directory not found, skipping: {directory}")

def run_tests():
    """Runs unit tests using pytest."""
    print("Running unit tests...")
    run_command(['pytest'])

def setup_environment():
    """Sets up the environment for the tests."""
    print("Setting up environment...")
    env_path = os.path.join(PROJECT_ROOT, '.env')
    if os.path.exists(env_path):
        load_dotenv(env_path)
        print("Loaded environment variables from .env file")
    else:
        print(".env file not found, skipping...")

def main():
    """Main function to handle command-line commands."""
    parser = argparse.ArgumentParser(description="Manage the BDD project")
    parser.add_argument('command', nargs="?", help="Command to run (e.g., run, test, report, clean, setup)")
    parser.add_argument('--feature', help="Run a specific feature file")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    commands = {
        'run': lambda: run_behave(args.feature),
        'test': run_tests,
        'report': generate_allure_report,
        'clean': clean_reports,
        'setup': setup_environment
    }

    if args.command in commands:
        commands[args.command]()
    else:
        print(f"Unknown command: {args.command}")
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()
