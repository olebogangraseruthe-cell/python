from pathlib import Path
import json


numbers = [5, 7, 3, 7, 2, 1, 9, 4, 6, 8]

# path = Path('numbers.json')
path = Path(__file__).parent / 'numbers.json'
contents = json.dumps(numbers)
path.write_text(contents)