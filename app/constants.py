from pathlib import Path

BASE_DIR =  Path(__file__).resolve(strict=True).parent
STATIC_DIR = BASE_DIR / "static"
FILES_DIR = STATIC_DIR / "files"