from setuptools import find_packages, setup
import os
import platform


def is_rocm_available():
    """Detect if ROCm is available."""
    return "rocm" in platform.system().lower() or any(
        keyword in os.environ.get("PATH", "").lower() for keyword in ["rocm", "hip"]
    )


def parse_requirements(file_path):
    """Parse a requirements file."""
    _install_requires = []
    _dependency_links = []
    with open(file_path, encoding="utf-8") as requirements_file:
        lines = [r.strip() for r in requirements_file.readlines()]
        for line in lines:
            if line.startswith("--extra-index-url"):
                # Handle custom index URLs
                _, url = line.split()
                _dependency_links.append(url)
            elif line and line[0] != "#":
                # Add valid requirements
                _install_requires.append(line)
    return _install_requires, _dependency_links


# Initialize dependencies
install_requires = []
dependency_links = []

# Install ROCm-specific dependencies first if available
if is_rocm_available():
    print("Detected ROCm. Installing requirements from requirements-amd.txt")
    amd_requires, amd_links = parse_requirements("requirements-amd.txt")
    install_requires.extend(amd_requires)
    dependency_links.extend(amd_links)

# Install general dependencies
print("Installing general requirements from requirements.txt")
general_requires, general_links = parse_requirements("requirements.txt")
install_requires.extend(general_requires)
dependency_links.extend(general_links)

# Ensure no duplicate dependencies
install_requires = list(set(install_requires))
dependency_links = list(set(dependency_links))

setup(
    name="axolotl",
    version="0.5.2",
    description="LLM Trainer",
    long_description="Axolotl is a tool designed to streamline the fine-tuning of various AI models, offering support for multiple configurations and architectures.",
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=install_requires,
    dependency_links=dependency_links,
    extras_require={
        "flash-attn": [
            "flash-attn==2.7.0.post2",
        ],
        "deepspeed": [
            "deepspeed==0.15.4",
            "deepspeed-kernels",
        ],
        "mamba-ssm": [
            "mamba-ssm==1.2.0.post1",
            "causal_conv1d",
        ],
        "auto-gptq": [
            "auto-gptq==0.5.1",
        ],
        "mlflow": [
            "mlflow",
        ],
        "lion-pytorch": [
            "lion-pytorch==0.1.2",
        ],
        "galore": [
            "galore_torch",
        ],
        "optimizers": [
            "galore_torch",
            "lion-pytorch==0.1.2",
            "lomo-optim==0.1.1",
            "torch-optimi==0.2.1",
        ],
    },
)
