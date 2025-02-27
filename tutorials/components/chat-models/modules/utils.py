from typing import Dict, Any, Optional

def load_env_to_dict(file_path: str) -> Optional[Dict[str, Any]]:
    env_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            # Remove whitespace and ignore comments or empty lines
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            # Split the line into key and value
            key, value = line.split('=', 1)
            env_dict[key.strip()] = value.strip()
    return env_dict