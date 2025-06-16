import subprocess
import sys
import os

def run_python_file(file_path):
    """Executes a Python file as a subprocess."""
    if not os.path.isfile(file_path):
        print(f"Error: File not found - {file_path}")
        return
    try:
        subprocess.run([sys.executable, file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Execution failed for {file_path}: {e}")

def run_shell_command(command):
    """Executes a shell command and returns its output."""
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Output:", result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Shell command failed: {e}")

def main():
    print("Running Python files...")
    run_python_file("1.py")
    run_python_file("2.py")
    run_python_file("3.py")
    run_python_file("4.py")
    run_python_file("5.py")
    run_python_file("6.py")

    print("\nRunning shell command...")
    os.chdir("../archive/")
    run_shell_command("type nul > actual_fraudulent_accounts.txt")
    run_shell_command("type nul > fraudulent_accounts.txt")
    run_shell_command("type nul > lr_fraudulent_accounts.txt")
    run_shell_command("type nul > xgb_fraudulent_accounts.txt")
    run_shell_command("type nul > rf_fraudulent_accounts.txt")

    print("Finished.")

if __name__ == "__main__":
    main()
