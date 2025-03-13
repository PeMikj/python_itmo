import sys

def number_lines(input_file=None):
    """Prints numbered lines from a file or stdin."""
    if input_file:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    else:
        lines = sys.stdin.readlines()
    
    for i, line in enumerate(lines, start=1):
        print(f"{i}\t{line.rstrip()}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        number_lines(sys.argv[1])
    else:
        number_lines()
