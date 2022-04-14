if [ "$(basename $0)" == "set-up-venv.bash" ]; then
    echo "Please source this script, like:"
    echo "source $(basename $0)"
    exit 1
fi

deactivate || true
rm -fr ./.venv3.9
python3.9 -m venv ./.venv3.9
. ./.venv3.9/bin/activate
pip install -r requirements.txt
