import sys

def count_stats(file):
    """Counts the number of lines, words, and bytes in a file or stdin."""
    lines = words = bytes_count = 0
    
    for line in file:
        lines += 1
        words += len(line.split())
        bytes_count += len(line.encode('utf-8'))
    
    return lines, words, bytes_count

def print_stats(stats, filename=None, width=1):
    """Displays statistics in wc format with correct indentation."""
    lines, words, bytes_count = stats
    line_format = f"{{:>{width}}} {{:>{width}}} {{:>{width}}}"
    output = line_format.format(lines, words, bytes_count)
    
    if filename:
        print(f" {output} {filename}")
    else:
        print(f" {output}")

if __name__ == "__main__":
    stats_list = []
    total_lines = total_words = total_bytes = 0

    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            try:
                with open(filename, 'r', encoding='utf-8') as file:
                    stats = count_stats(file)
                    stats_list.append((stats, filename))
                    total_lines += stats[0]
                    total_words += stats[1]
                    total_bytes += stats[2]
            except FileNotFoundError:
                print(f"wc: {filename}: No such file or directory", file=sys.stderr)
                sys.exit(1)

        max_num = max([total_lines, total_words, total_bytes] +
                      [num for stats, _ in stats_list for num in stats], default=0)
        width = max(1, len(str(max_num)))

        for stats, filename in stats_list:
            print_stats(stats, filename, width)

        if len(stats_list) > 1:
            print_stats((total_lines, total_words, total_bytes), "total", width)
    else:
        stats = count_stats(sys.stdin)
        width = max(1, len(str(max(stats))))
        print_stats(stats, width=width)