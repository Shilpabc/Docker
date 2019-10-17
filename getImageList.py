import docker
from flask import render_template, request, jsonify
import connexion
import json

# Create the application instance
app = connexion.App(__name__, specification_dir='./')


@app.route('/imagelist', methods=['GET'])
def imagelist():

    if 'imagename' in request.args:
        imagename = request.args['imagename']
        print(imagename)
        client = docker.from_env()
        images = client.images.search(imagename)
        iList = jsonify(images)
    else:
        iList = jsonify("No Image name for processing")
    
    return iList

if __name__ == '__main__':
    app.run(host='localhost', port=5000)