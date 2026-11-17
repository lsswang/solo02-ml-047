"""Nearest-entry forward plotting of already fitted cubic strokes."""
import math


def _distance(a, b):
    return math.hypot(a[0]-b[0], a[1]-b[1])


def plan(strokes, start, end):
    remaining = set(strokes)
    position = list(start)
    order = []
    commands = []
    travel = 0.0
    while remaining:
        stroke_id = min(remaining, key=lambda key:
                        (_distance(position, strokes[key][0][0]), key))
        pieces = strokes[stroke_id]
        entry = pieces[0][0]
        travel += _distance(position, entry)
        commands.append({'op': 'move', 'to': list(entry)})
        for controls in pieces:
            commands.append({'op': 'cubic', 'stroke': stroke_id,
                             'controls': [list(point) for point in controls]})
        position = list(pieces[-1][-1])
        order.append({'stroke': stroke_id, 'direction': 'forward'})
        remaining.remove(stroke_id)
    travel += _distance(position, end)
    commands.append({'op': 'move', 'to': list(end)})
    return {'order': order, 'pen_up_distance': travel, 'commands': commands}
