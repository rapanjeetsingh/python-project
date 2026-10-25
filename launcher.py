import os
import sys
from pathlib import Path

if getattr(sys, "frozen", False):
    app_dir = Path(sys._MEIPASS)
else:
    app_dir = Path(__file__).resolve().parent

os.chdir(app_dir)

os.environ["STREAMLIT_SERVER_HEADLESS"] = "true"
os.environ["STREAMLIT_BROWSER_GATHER_USAGE_STATS"] = "false"

from streamlit.web import cli as stcli

sys.argv = [
    "streamlit",
    "run",
    str(app_dir / "app.py"),
    "--server.headless=true",
]

stcli.main()