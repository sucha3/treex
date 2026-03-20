# treex
extended bash tree that groups files by extension and summarizes each group with truncated output

```bash
# setup
echo "alias treex='python3 tree_limited.py'" >> ~/.zshrc
```

## example output
```
$ treex .
~/repo
├── test1.tar.gz
├── test10.tar.gz
├── ... (8) *.tar.gz files remaining
├── test1.txt
├── test2.txt
├── ... (3) *.txt files remaining
├── test1.md
├── test10.md
└── ... (8) *.md files remaining
```


## usage

```
positional arguments:
  target      The directory to list (default: .)

optional arguments:
  -h, --help  show this help message and exit
  -L L        Max display depth (default: 3).
  -n N        Max entries per group (default: 3).
```
