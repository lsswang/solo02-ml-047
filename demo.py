import json
from pathlib import Path
import traces
import plotter


def run(data):
    fitted = traces.fit_sketch(data['traces'], data['regularization'],
                               data['segment_penalty'])
    current_curves = {key: value['segments'] for key, value in fitted.items()}
    drawing = plotter.plan(current_curves, data['start'], data['end'])
    return {'fitted': fitted, 'drawing': drawing}


if __name__ == '__main__':
    fixture = Path(__file__).with_name('fixtures')/'cases.json'
    print(json.dumps(run(json.loads(fixture.read_text())), ensure_ascii=False, indent=2))
