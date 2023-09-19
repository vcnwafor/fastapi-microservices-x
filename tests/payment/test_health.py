import httpx
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

import os, sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..."))
sys.path.insert(0, project_root)

from payment.main import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.mark.asyncio
async def test_health(client):
    resp = client.get('/health')
    assert 200 == resp.status_code