import subprocess

# List of Python files to run in order
python_files = [
    "import_movie.py",
    "import_user.py",
    "import_rental.py",
    "import_review.py",
]

# Run each Python file in order
for file in python_files:
    print(f"Running {file}")
    subprocess.run(["python3", file])