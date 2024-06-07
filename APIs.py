import os
import time
from io import BytesIO
from zipfile import ZipFile

import httpx
from dotenv import load_dotenv

load_dotenv()


class QualtricsAPI:
    def __init__(self):
        self.DC = os.getenv("QUALTRICS_DC")
        api_key = os.getenv("QUALTRICS_API_KEY")
        self.client = httpx.Client(
            headers={"Accept": "application/octet-stream, application/json", "Content-Type": "application/json", "X-API-TOKEN": api_key}
        )

    def get(self, path):
        return self.client.get(f"https://{self.DC}.qualtrics.com/API/v3/{path}")

    def put(self, path, json):
        return self.client.put(f"https://{self.DC}.qualtrics.com/API/v3/{path}", json=json)

    def post(self, path, json):
        return self.client.post(f"https://{self.DC}.qualtrics.com/API/v3/{path}", json=json)

    def getData(self, surveyID, dataFolder):
        # Todo: this should probably use streaming rather than downloading the whole file into memory.
        res = self.post(f"surveys/{surveyID}/export-responses", {"format": "csv", "useLabels": True})
        assert res.status_code == 200
        progressId = res.json()["result"]["progressId"]
        while res.json()["result"]["status"] == "inProgress":
            print("\rDownload is being prepared... %.2f%% " % res.json()["result"]["percentComplete"], end="")
            time.sleep(1)
            res = self.get(f"surveys/{surveyID}/export-responses/{progressId}")
            assert res.status_code == 200
        print("Done.\nDownloading file... ", end="")
        file = self.get(f"surveys/{surveyID}/export-responses/{res.json()['result']['fileId']}/file")
        assert file.status_code == 200
        assert file.headers["content-type"] == "application/zip"
        print("extracting... ", end="")
        myzip = ZipFile(BytesIO(file.read()))
        myzip.extractall(dataFolder)
        print("done.")


class ProlificAPI:
    def __init__(self):
        api_key = os.getenv("PROLIFIC_API_KEY")
        self.client = httpx.Client(
            headers={"Accept": "application/json", "Content-Type": "application/json", "Authorization": "Token " + api_key}, timeout=180
        )

    def get(self, path):
        return self.client.get(f"https://api.prolific.com/api/v1/{path}")

    def put(self, path, json):
        return self.client.put(f"https://api.prolific.com/api/v1/{path}", json=json)

    def post(self, path, json):
        return self.client.post(f"https://api.prolific.com/api/v1/{path}", json=json)

    def patch(self, path, json):
        return self.client.patch(f"https://api.prolific.com/api/v1/{path}", json=json)

    def delete(self, path):
        return self.client.delete(f"https://api.prolific.com/api/v1/{path}")
