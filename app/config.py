from pathlib import Path

# If local model folder
MODEL_DIR = "mhd15865/t5_finetuned_on_kit_dataset"

# If loading from Hugging Face Hub
# MODEL_DIR = "mhd15865/t5_finetuned_on_kit_dataset"

KB_FILE = Path(__file__).resolve().parent / "data" / "dataRag.json"

SIMILARITY_THRESHOLD = 0.88
TOP_K = 3
