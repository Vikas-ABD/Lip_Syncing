# Lip Syncing with Wav2Lip

## Overview
This repository provides an implementation of Wav2Lip, a lip-syncing model that accurately synchronizes videos with target speech. The model is trained on the LRS2 dataset and offers high accuracy for lip-syncing across various identities, voices, and languages. Additionally, it works for CGI faces and synthetic voices.

## Usage Instructions
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Vikas-ABD/Lip_Syncing.git

   cd Lip_Syncing
   ```

## Prerequisites
- Python 3.11
- Install ffmpeg:
  ```bash
     sudo apt-get install ffmpeg
     ```
## Install Necessary Packages

```bash
   pip install -r requirements.txt
```
## Download Pre-trained Models

Run the following command to download the Wav2Lip + GAN model and the face detection pre-trained model:

```bash
python model_download.py
```

## Input Files

Place your input video file (`input_vid.mp4`) and input audio file (`input_audio.wav`) in the `Data` folder.

## Lip-syncing with Pre-trained Models (Inference)

Use the pre-trained models to lip-sync any video to any audio:

```bash
python inference.py --checkpoint_path <ckpt> --face <input_vid.mp4> --audio <input_audio.wav>
```

After running the above command we will get a output video in the results folder in the current dir

## Tips for Better Results

- Experiment with the `--pads` argument to adjust the detected face bounding box. For example: `--pads 0 20 0 0`.
- If you encounter issues like a dislocated mouth position or artifacts, use the `--nosmooth` argument.
- Experiment with the `--resize_factor` argument to get a lower-resolution video. Lower resolution often provides visually pleasing results.

### Understanding Lip Syncing with Notebooks

To gain a clearer understanding of the lip-syncing process, explore the provided Jupyter notebooks in the repository:

1. ## Wave2Lip Notebook 1 (`wave2lip_notebook1.ipynb`):
   - Open this notebook to learn about the fundamentals of lip-syncing using Wav2Lip.
   - The notebook covers essential concepts and provides step-by-step guidance.

2. ## Wave2Lip Notebook 2 (`wave2lip_notebook2.ipynb`):
   - Explore this notebook for more advanced lip-syncing techniques and scenarios.
   - It may include additional features, use cases, or optimizations.

Feel free to run these notebooks in your colab for a hands-on experience.









