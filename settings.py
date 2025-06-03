from pathlib import Path
import sys

# Path setup
FILE = Path(__file__).resolve()
ROOT = FILE.parent

if ROOT not in sys.path:
    sys.path.append(str(ROOT))

# Model directory dan model keras (.h5)
MODEL_DIR = ROOT / 'weights'
DETECTION_MODEL = MODEL_DIR / 'dr_cnn_model.keras'  # pastikan file ini ada di folder weights

# Contoh lainnya jika perlu:
IMAGES_DIR = ROOT / 'images'
VIDEOS_DIR = ROOT / 'Videos'

# Webcam
WEBCAM_PATH = 0  # default webcam device id

# Video dictionary (optional)
VIDEOS_DICT = {
    'video_1': VIDEOS_DIR / 'video1.mp4',
    'video_2': VIDEOS_DIR / 'video2.mp4',
}

