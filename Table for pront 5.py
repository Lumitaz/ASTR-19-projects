import numpy as np
from astropy.table import Table

# mah computations for the table and uses np.linspace to create an array of x values and np.sin to compute the sine values, then returns an astropy Table with the results
def compute_sin_table(start: float, stop: float, num_entries: int) -> Table:
    x = np.linspace(start, stop, num_entries)
    sin_x = np.sin(x)
    return Table([x, sin_x], names=("x", "sin(x)"))

# prints for collums and describes the table formatting
def print_table(table: Table):
    for col in table.colnames:
        table[col].format = ".10f"
    table.pprint(max_lines=-1)

#def main
def main():
    table = compute_sin_table(0.0, 2.0, 1000)
    print_table(table)


if __name__ == "__main__":
    main()