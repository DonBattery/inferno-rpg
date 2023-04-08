import os

def get_config_files(data_folder: str) -> list:
    config_files = []

    for root, _, files in os.walk(data_folder):
        for filename in files:
            if filename.endswith(".yaml") or filename.endswith(".yml"):
                config_files.append(os.path.join(root, filename))

    return config_files
