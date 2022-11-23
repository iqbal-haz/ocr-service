# ocr-service

## Installation

1. Clone repository
2. Create virutal environment <br>
Python setup <br>
`python3 -m venv env` <br>
Virtualenv <br>
`virtualenv env`
3. Activate virtual environment <br>
Windows <br>
`env\Scripts\activate` <br>
MacOS / Linux <br>
`source env/bin/activate`
4. Install requirements <br>
`pip install -r requirements.txt`
5. Run the app <br>
`flask run`

## Endpoint(s)

`POST /`

```
curl --location --request POST 'http://127.0.0.1:5000/' \
--form 'image=@"/path/to/image/file"
```

## Creating Executable

This application uses py2app module to create .app executable. (equivalent with py2exe for windows) <br>
To create executable, you need to first __activate the virtual environment__, and then run this command on terminal
```
python3 setup.py py2app
```
> **Note**: you dont need to activate virtual environment if py2app already installed as global package in your system.

To run the executable, you can do __one__ of the following steps: <br>
1. go to dist directory and double click on the ocr-app, or 
2. run the command below on terminal <br>
`
./dist/ocr-app.app/Contents/MacOS/ocr-app
`