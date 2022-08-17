"""
File: my.drawing.py
Name: Sue Lin
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLine, GArc, GLabel
from campy.graphics.gwindow import GWindow

size = 10

def main():
    """
    Title: Lady M Mille Crêpes
    Mille crêpes with perfect irresistible twenty layers.
    """
    window = GWindow(width=1500, height=1500)

    background = GRect(1500,1500)
    background.filled= True
    background.fill_color = 'darksage'
    window.add(background)

    cake_body = GPolygon()
    cake_body.add_vertex((873, 153))
    cake_body.add_vertex((272, 521))
    cake_body.add_vertex((1178, 312))
    cake_body.filled= True
    cake_body.fill_color = 'lemonchiffon'
    cake_body.color = 'lemonchiffon'
    window.add(cake_body)

    cake_body2 = GRect(509,189,x=272,y=521)
    cake_body2.filled= True
    cake_body2.fill_color = 'crimson'
    cake_body2.color = 'crimson'
    window.add(cake_body2)

    cake_body2 = GRect(1178-(272+509),189,x=272+509,y=521)
    cake_body2.filled= True
    cake_body2.fill_color = 'crimson'
    cake_body2.color = 'crimson'
    window.add(cake_body2)

    cake_top_round = GArc((1178-873)*4, (312-153)*4, 0, 90, x=873-((1178-873)), y=153)
    cake_top_round.filled= True
    cake_top_round.fill_color = 'lemonchiffon'
    cake_top_round.color = 'lemonchiffon'
    window.add(cake_top_round)

    cake_face1 = GLine(1178, 312, 1178, 653)
    cake_face2 = GLine(272, 521, 272, 807)
    cake_face3 = GLine(1178, 653, 272, 807)
    cake_face1.color = 'lemonchiffon'
    cake_face2.color = 'lemonchiffon'
    cake_face3.color = 'honeydew'
    window.add(cake_face1)
    window.add(cake_face2)
    window.add(cake_face3)

    layer_scale = (653 - 342) / 20

    for i in range(19):
        cake_layer = GLine(272, 521+layer_scale*i, 1178, 312+layer_scale*i)
        cake_layer.color = 'blanchedalmond'
        window.add(cake_layer)


    brand = GLabel("LADY", x=1055, y=314+layer_scale*22)
    brand.font='SansSerif-38'
    #brand.filled= True
    brand.color = 'indianred'
    window.add(brand)

    brand2= GLabel("           M", x=1055, y=314+layer_scale*22)
    brand2.font='SansSerif-38-BOLD'
    brand2.color = 'indigo'
    window.add(brand2)




if __name__ == '__main__':
    main()
