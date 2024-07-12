from typing import TYPE_CHECKING
import pytest

# from litestar import TestClient
# from app import app  # Assuming `app` is your Litestar application instance
from ..app import app
from litestar.testing import TestClient


@pytest.fixture
def client():
    """Create a TestClient instance for testing."""
    return TestClient(app)


def test_read_main(client: "TestClient"):
    """Test the main endpoint."""
    response = client.get("/ingredient/all")
    assert response.status_code == 200
