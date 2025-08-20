from fastapi import FastAPI

app =FastAPI()

@app.get("/hello")
def helloeveryone():
    print("Hello guys, how are you?")
    return {"msg":"Hello guys"}

##passing param
@app.get("/hello/{name}")
def helloeveryone(name):
    print(f"Hello {name}, how are you?")
    return {"msg":f"Hello {name}"}

@app.get("/addnum/{a}/{b}")
def addnum(a:int,b:int):
    return {"msg": f"sum of {a} and {b} is {a+b}"}

##post method

# call from command