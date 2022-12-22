
import sys

width = 0
height = 0

for line in sys.stdin:
    ln_copy = None
    if '1' in line:
        ln_copy = line.strip()
        ln_copy = ln_copy.replace(' ', '')
        height = ln_copy.index('1')
        break
    width += 1

print(abs(width - 2) + abs(height - 2))
