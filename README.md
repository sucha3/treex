# treex
extended bash tree that groups files by extension and summarizes each group with truncated output

```bash
# setup
echo "alias treex='python3 tree_limited.py'" >> ~/.zshrc

treex .
# Custom depth and limit
treex . -L 2 -n 5
```


## Usage

```
positional arguments:
  target      The directory to list (default: .)

optional arguments:
  -h, --help  show this help message and exit
  -L L        Max display depth.
  -n N        Max entries per group.
```
