"""Weighted one-cubic regression for each ordered sample trace."""
import numpy as np


def fit_stroke(points, weights=None, regularization=0.1, segment_penalty=0.005):
    points = np.asarray(points, dtype=float)
    weights = np.ones(len(points)) if weights is None else np.asarray(weights, dtype=float)
    t = np.linspace(0.0, 1.0, len(points))
    basis = np.column_stack(((1-t)**3, 3*(1-t)**2*t, 3*(1-t)*t*t, t**3))
    chord = np.asarray([(1-u)*points[0]+u*points[-1] for u in (0, 1/3, 2/3, 1)])
    matrix = np.vstack((np.sqrt(weights)[:, None]*basis,
                        np.sqrt(regularization)*np.eye(4)))
    target = np.vstack((np.sqrt(weights)[:, None]*points,
                        np.sqrt(regularization)*chord))
    controls = np.linalg.lstsq(matrix, target, rcond=None)[0]
    residual = basis@controls-points
    fit = float(np.sum(weights[:, None]*residual**2))
    regularity = float(regularization*np.sum((controls-chord)**2))
    return {'breaks': [0, len(points)-1], 'segments': [controls.tolist()],
            'objective': {'fit': fit, 'regularity': regularity,
                          'penalty': float(segment_penalty),
                          'total': fit+regularity+float(segment_penalty)}}


def fit_sketch(traces, regularization=0.1, segment_penalty=0.005):
    result = {}
    for stroke_id, trace in traces.items():
        result[stroke_id] = fit_stroke(trace['points'], trace.get('weights'),
                                      regularization, segment_penalty)
    return result
