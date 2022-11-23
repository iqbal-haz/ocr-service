import sys
from setuptools import setup

mainscript = "app.py"

if sys.platform == "darwin":
    extra_options = dict(
        setup_requires=['py2app'],
        app=[mainscript],
        options=dict(
            py2app=dict(
                argv_emulation=True,
                includes=['pip', 'ssl']
            )
        ),
    )
elif sys.platform == 'win32':
    extra_options = dict(
        setup_requires=['py2exe'],
        app=[mainscript],
    )
else:
    extra_options = dict(
        scripts=[mainscript],
    )

setup(
    name="ocr-app",
    **extra_options,
)