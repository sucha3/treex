import os
import argparse
def get_type(entry, directory):
    if os.path.isdir(os.path.join(directory, entry)):
        return "Directory"
    
    # Dynamically find extensions (up to 2 dots if they look like extensions)
    parts = entry.split('.')
    if len(parts) > 2:
        # Check if the last two parts are short (typical of extensions like .txt.gz)
        if len(parts[-1]) <= 4 and len(parts[-2]) <= 5:
            return "." + ".".join(parts[-2:])
    
    # Fallback to single extension
    ext = os.path.splitext(entry)[1]
    return ext if ext else "no extension"
def print_tree(directory, max_depth=3, max_entries=3, current_depth=0, prefix=""):
    if current_depth >= max_depth: return
    try:
        all_entries = sorted(os.listdir(directory))
    except (PermissionError, FileNotFoundError): return
    # Group entries by type (directory or extension)
    from collections import defaultdict
    groups = defaultdict(list)
    for entry in all_entries:
        groups[get_type(entry, directory)].append(entry)
    # We want to display directories first, then files
    sorted_types = sorted(groups.keys(), key=lambda t: (t != "Directory", t.lower()))
    
    # Flatten the grouped entries into a single list with ellipsis markers
    to_display = []
    for t in sorted_types:
        items = groups[t]
        
        if t == "Directory":
            to_display.extend(items) # Show ALL directories
        else:
            to_display.extend(items[:max_entries])
            if len(items) > max_entries:
                summary_type = f"*{t}" if t.startswith(".") else t
                to_display.append(f"... ({len(items) - max_entries}) {summary_type} files remaining")
    num_visible = len(to_display)
    for i, entry_text in enumerate(to_display):
        is_last = (i == num_visible - 1)
        connector = "└── " if is_last else "├── "
        
        # If it's a summary line, just print it
        if entry_text.startswith("... ("):
            print(f"{prefix}{connector}{entry_text}")
            continue
            
        full_path = os.path.join(directory, entry_text)
        suffix = "/" if os.path.isdir(full_path) else ""
        print(f"{prefix}{connector}{entry_text}{suffix}")
        
        if os.path.isdir(full_path):
            new_prefix = prefix + ("    " if is_last else "│   ")
            print_tree(full_path, max_depth, max_entries, current_depth + 1, new_prefix)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A grouped directory tree utility.")
    parser.add_argument("target", nargs="?", default=".", help="The directory to list (default: .)")
    parser.add_argument("-L", type=int, default=3, help="Max display depth.")
    parser.add_argument("-n", type=int, default=3, help="Max entries per group.")
    
    args = parser.parse_args()
    print(os.path.abspath(args.target))
    print_tree(os.path.abspath(args.target), max_depth=args.L, max_entries=args.n)
