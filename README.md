# agreg

pyinstaller --onefile    --add-data "structure.yaml;."    --add-data "verb.yaml;."   --collect-all gradio   --collect-all pyyaml   --collect-all numpy --collect-all gradio_client --collect-all safehttpx --collect-all groovy  app.py