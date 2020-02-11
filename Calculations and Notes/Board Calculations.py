'''
So we'll have an initial w and h.

Chess board should be about 60% of screen height.

Space above should equal space below etc.

so h * 0.6 is our board length.

tile length is lth = (h * 0.6) / 8

we have tile indices (a, b) with 0 <= a, b <= 7

suppose we have a map f: I -> Pos

f(a,b) = (x_0 + a * lth, y_0 + b * lth)

Can get (0, 0) pixel of the board by size / 2 - (h * 0.3, h * 0.3)

(x_0, y_0) = size / 2 - (h * 0.3, h * 0.3) + (lth / 2, lth / 2)

so paths should be Path.rect()
'''
