from pathlib import Path


path = Path(__file__).parent / 'alice.txt'
contents = path.read_text(encoding='utf-8')