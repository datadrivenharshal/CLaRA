import os

PROJECT_STRUCTURE = {
    "CLaRA": [
        "main.py",
        "tools.py",
        "planner.py",
        "requirements.txt",
        "README.md",
        "config/.env",
        "data/input_images/",
        "data/output/",
        "models/",
        "inference/__init__.py",
        "inference/sam_wrapper.py",
        "inference/dino_wrapper.py",
        "inference/keypoints.py",
        "coco_utils/coco_format.py",
        "coco_utils/evaluator.py",
        "config/prompts/"
    ]
}

def create_structure(base_path, structure):
    for folder, items in structure.items():
        folder_path = os.path.join(base_path, folder)
        for item in items:
            item_path = os.path.join(folder_path, item)
            if item.endswith("/"):  # directory
                os.makedirs(item_path, exist_ok=True)
            else:  # file
                os.makedirs(os.path.dirname(item_path), exist_ok=True)
                if not os.path.exists(item_path):
                    with open(item_path, "w") as f:
                        if item.endswith(".py"):
                            f.write(f"# {os.path.basename(item)}\n")
                        elif item.endswith(".env"):
                            f.write("# Add your API keys and config here\n")
                        elif item.endswith("README.md"):
                            f.write("# CLaRA: A Contextual Labelling and Rapid Annotation Framework Using Large Language Models\n")
                        elif item.endswith("requirements.txt"):
                            f.write("python-dotenv\ntransformers\ntorch\nopencv-python\n")

if __name__ == "__main__":
    create_structure(".", PROJECT_STRUCTURE)
    print("Project structure created under 'CLaRA/'")
