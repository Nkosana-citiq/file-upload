# rest.py

import os
import uuid

import falcon
from falcon_cors import CORS
from falcon_multipart.middleware import MultipartMiddleware


class UploadResource(object):
    def on_post(self, req, resp):
        """Handles POST requests"""

        pdf = req.get_param('thumbnail')

        filename = "{name}.{ext}".format(name=uuid.uuid4(), ext='pdf')

        pdf_path = os.path.join(os.getcwd(), filename)
        with open(pdf_path, "wb") as pdf_file:
            while True:
                chunk = pdf.file.read()
                pdf_file.write(chunk)
                if not chunk:
                    break
        resp.status = falcon.HTTP_200
        resp.body = '\nUpload was successful. \n\n'


cors = CORS(
    allow_all_origins=True,
    allow_all_methods=True,
    allow_all_headers=True)

api = application = falcon.API(
    middleware=[cors.middleware,
                MultipartMiddleware()]
)

api.add_route('/upload', UploadResource())
