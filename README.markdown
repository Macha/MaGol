An implementation of Conway's Game of Life in Python.

Usage
====

Requirements
---

* Python 2.7
* PyGame (for the GUI)

Command Line
---

Run it using consolegol.py. It takes no arguments. When prompted, enter
the size of the board (it is square, and the number you enter is used
for all sides). It will ask you how many turns you wish to run. After
that, you can run it some more, or you can type '0' to exit.

GUI
---

Run it using `pygamegol.py <length of sides>`. Alternatively, you may also
specify a filename to a .rle file of an initial layout as such
`pygamegol.py 100 glider.rle`. However, it will
be rejected if it is larger than the length of sides given in the
command line arguments. 

The controls are as follows:

* Left click a cell to toggle it's state (See the bugs section below)
* Press 's' to toggle slow mode. This slows it down to 1 generation per
  second.
* Press 'r' to reset the grid.
* Press tab to fill the grid randomly.

Known Bugs
----

* If you choose an uneven length, there will be an area around the edge
  of the screen that will crash the simulator if clicked on.
* It is extremely slow for grid sizes > ~150x150 (depending on your
  computer this may go up or down)
