'''
If the Board root node instantiates each tile then we could have each touch action change a nested list containing the info of each tile via var[file][rank].

The arguments of each Tile will be used in its __init__ to create its appearance.

The current arguments I have in mind for Tile will be
 - Coordinates on board - (f, r)
 - Colour/Type of piece - {"side": s, "type": t} (This could be two arguments)
 - Light - Boolean - Will decide if a square is selected or a possible move of a selected square

Can a touch action in a class change a variable in another file?
'''
