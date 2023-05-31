from os.path import exists
import pytest
from fastapi.testclient import TestClient


client = TestClient(app)
model_path = './ckpt/u2net.pth'

#import numpy as np


def test_read():
    response = client.post("/change-bg")
    assert response.status_code == 200
    assert response.json() ==  JSONResponse(
            status_code=200,
            content={
                'img_with_bk': output_image,
                'img_no_bk': img_no_bk,})


def test_right_path():
    assert exists('/webapp/images-input')
    assert exists('/webapp/images-output')

