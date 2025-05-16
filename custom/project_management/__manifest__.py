{
"name": "Odoo 18 Development",
"image": "odoo:18",
"forwardPorts": [8069, 5432],
"postCreateCommand": "pip install -r /usr/lib/python3/dist-packages/odoo/requirements.txt && pip install odoo",
"customizations": {
"vscode": {
"extensions": [
"ms-python.python",
"ms-vscode-remote.remote-containers"
]
}
}
}