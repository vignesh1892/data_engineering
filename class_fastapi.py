from fastapi import FastAPI

app =FastAPI()

@app.get("sample/")
def helloeveryone():
    print("Hello guys, how are you?")