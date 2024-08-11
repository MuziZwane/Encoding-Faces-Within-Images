from pathlib import Path

default_encoding_path = Path("output/encoding.pkl")

Path("training").mkdir(exist_ok=True)
Path("output").mkdir(exist_ok=True)
Path("output").mkdir(exist_ok=True)

"""

"""
def encode_known_faces(
  model: str = "hog", encoding_location: Path = default_encoding_path
) -> None:
  names  = []
  encodings = []
  for filepath in Path("training").glob("*.jpg"):
    name = filepath.parent.name
    image = face_recognition.load_image_file(str(filepath))  