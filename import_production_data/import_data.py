import subprocess

# List of Python files to run in order
python_files = [
    "import_movie.py",
    "import_movie_manual.py",
    "import_rental.py",
    "import_review.py",
    "import_user.py"
]

# Run each Python file in order
for file in python_files:
    print(f"Running {file}")
    subprocess.run(["python", file])