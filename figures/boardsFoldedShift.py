#!/usr/bin/env python

import sys
sys.path.append("/home/jonathan/Programing/Python/SpiNNer")

import diagram

from model import board
from model import coordinates
from model import transforms
from model import topology

d = diagram.Diagram()

# Create a small system of boards on a hexagonal coordinate system
boards = board.create_torus(4,4)
boards = transforms.hex_to_cartesian(boards)
boards_rect = transforms.rhombus_to_rect(boards)
#boards = transforms.compress(boards)
#boards = transforms.fold(boards, (2,1))

# Create a dictionary which maps boards to coordinates to use for labelling
# boards in the diagram.
board2coord = dict(boards)

# Draw the boards on the diagram as a hexagons
for b, coords in boards:
	if coords not in (c for (b,c) in boards_rect):
		d.add_board_hexagon(b, coords, ["help lines"])

# Draw the boards on the diagram as a hexagons
for b, coords in boards_rect:
	if coords not in (c for (b,c) in boards):
		d.add_board_hexagon(b, coords, ["ultra thick"])
	else:
		d.add_board_hexagon(b, coords)
	
	for direction, colour in ( (topology.NORTH,      "red")
	                         , (topology.NORTH_EAST, "green")
	                         , (topology.EAST,       "blue")):
		if sum(map(abs, board2coord[b.follow_wire(direction)] - board2coord[b])) > 2:
			d.add_wire(b, direction, [colour])

# Add some invisible nodes so the image is centred on the rectangular block
for x in range(8,8+3):
	b = board.Board()
	d.add_board_hexagon(b, coordinates.Cartesian2D(x,0), ["opacity=0"])


# Output the TikZ code for the diagram
print r"\begin{tikzpicture}[thick,scale=0.9]"
print d.get_tikz()
print r"\end{tikzpicture}"
