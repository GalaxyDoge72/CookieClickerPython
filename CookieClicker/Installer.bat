python -m pip install --upgrade pip
pip freeze --local | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -U
python -m pip install pygame
cd %~dp0
echo ReleaseVersion.py | cmd