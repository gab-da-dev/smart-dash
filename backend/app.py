from litestar import Litestar, get
from pyd

@get("/")
async def hello_world() -> str:
 return "Hello, world!"


app = Litestar([hello_world])