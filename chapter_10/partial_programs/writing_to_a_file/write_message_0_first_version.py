from pathlib import Path


path = Path(__file__).parent / 'programming.txt'
path.write_text("I love programming.")