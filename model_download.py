import requests
from tqdm import tqdm

def download_file(url, destination):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 Kibibyte

    with open(destination, 'wb') as file, tqdm(
        desc=destination,
        total=total_size,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(block_size):
            bar.update(len(data))
            file.write(data)

if __name__ == "__main__":
    # Download the first model
    model_url_1 = 'https://github.com/justinjohn0306/Wav2Lip/releases/download/models/wav2lip_gan.pth'
    destination_path_1 = 'checkpoints/wav2lip_gan.pth'

    print(f"Downloading model from {model_url_1}")
    download_file(model_url_1, destination_path_1)
    print("Download complete!")

    # Download the second model
    model_url_2 = 'https://www.adrianbulat.com/downloads/python-fan/s3fd-619a316812.pth'
    destination_path_2 = 'face_detection/detection/sfd/s3fd.pth'

    print(f"Downloading model from {model_url_2}")
    download_file(model_url_2, destination_path_2)
    print("Download complete!")
