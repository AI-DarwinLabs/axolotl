# Installer Flash-Attention
git clone --recursive https://github.com/ROCm/flash-attention.git
cd flash-attention
GPU_ARCHS=gfx942 python setup.py install
cd ..

# Installer DeepSpeed stable fork
pip uninstall deepspeed -y
git clone https://github.com/AI-DarwinLabs/deepspeed-stable-mi300.git tmp_deepspeed
cd tmp_deepspeed
pip install -r requirements/requirements.txt
pip install --verbose --no-cache-dir --no-build-isolation ./
cd ..
