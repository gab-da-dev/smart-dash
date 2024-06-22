from litestar.status_codes import HTTP_200_OK
from litestar.testing import AsyncTestClient

import app


async def test_health_check():
    async with AsyncTestClient(app=app) as client:
        response = await client.get("/ingredient/all")
        assert response.status_code == HTTP_200_OK
