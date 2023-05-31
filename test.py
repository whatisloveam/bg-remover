from os.path import exists
import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)
model_path = './ckpt/u2net.pth'

#import numpy as np


def test_homepage():
    response = client.post("/")
    assert response.status_code == 200


def test_read():
    response = client.post("/replace")
    assert response.status_code == 200


   

def test_right_path():
    assert exists('./images-input')
    assert exists('./images-output')

