# from langchain.pydantic_v1 import BaseModel

def func(fun):
    def func1():
        print("this is the super function ")
        fun()
    return func1


@func
def newfunc():
    print("i am the derived function")

print("what is happening")
