'''
The plan is to have the scene register a first touch and loop through each child to find if touch.location is contained in any tile's frame attribute.

Taking that tile's (if there is one) coordinate attribute, we can use the board info and the is_selected boolean to decide what should change on the board.
'''
