import os

GITHUB_FOLDER_RELATIVE_PATH = 'drive/My Drive/Colab Notebooks/Github'


def mount_google_drive(force_remount=True):
    from google.colab import drive
    drive.mount('/content/drive', force_remount=force_remount)
    # Navigate to GitHub folder
    os.chdir(GITHUB_FOLDER_RELATIVE_PATH)
