import os
from pathlib import Path
 
def main() -> None:
    data_dir = Path(__file__).resolve().parent / "data"
    os.environ.setdefault("CAREER_AI_DATA_DIR", str(data_dir))
 
    from career_ai_core import main as launch
    launch()
 
if __name__ == "__main__":
    main()
