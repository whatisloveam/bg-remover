from os.path import exists
import pytest
from fastapi.testclient import TestClient


client = TestClient(app)
model_path = './ckpt/u2net.pth'

#import numpy as np


def test_read():
    response = client.post("/change-bg")
    assert response.status_code == 200
   

def test_right_path():
    assert exists('/webapp/images-input')
    assert exists('/webapp/images-output')

