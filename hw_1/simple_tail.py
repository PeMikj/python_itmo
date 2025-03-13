import sys

def tail(filename, num_lines=10, add_newline=False):
    """Prints the last num_lines lines of a file with correct formatting."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"tail: cannot open '{filename}' for reading: No such file or directory", file=sys.stderr)
        return
    except PermissionError:
        print(f"tail: cannot open '{filename}' for reading: Permission denied", file=sys.stderr)
        return
    
    if add_newline:
        print()

    print(f"==> {filename} <==")
    for line in lines[-num_lines:]:
        print(line, end='')

def tail_stdin(num_lines=17):
    """Reads last num_lines lines from stdin."""
    lines = sys.stdin.readlines()
    for line in lines[-num_lines:]:
        print(line, end='')

if __name__ == "__main__":
    files = sys.argv[1:]
    for i, file in enumerate(files):
        tail(file, add_newline=(i > 0))

    if not files:
        tail_stdin()
