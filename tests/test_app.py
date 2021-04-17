import os
import tempfile

import pytest

from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

def test_index(client):

    rv = client.get('/')
    assert b'Patient Management Portal' in rv.data
