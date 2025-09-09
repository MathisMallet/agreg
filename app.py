print("Starting the Gradio app...")

import os
# print("Current working directory:", os.getcwd())
# print("Files in directory:", os.listdir())
# print("Does structure.yaml exist?", os.path.exists("structure.yaml"))
# print("Does verb.yaml exist?", os.path.exists("verb.yaml"))

import yaml
import numpy as np
import gradio as gr

def draft_random_1D(list_obj):
    # print("len", len(list_obj))
    index = np.random.randint(len(list_obj))
    # print("index", index)
    return list_obj[index]

def draft_random(structure):
    _ , modes = list(structure.items())[0]
    mode = draft_random_1D(modes)
    mode , temps = list(mode.items())[0]
    result = {"mode" : mode}
    temp = draft_random_1D(temps)
    temp , voix = list(temp.items())[0]
    result["temp"] = temp
    voie = draft_random_1D(voix)
    voie , personnes = list(voie.items())[0]
    result["voie"] = voie
    personne = draft_random_1D(personnes)
    result["personne"] = personne
    return result

# with open('structure.yaml', 'r') as file:
#     structure = yaml.safe_load(file)

# with open('verb.yaml', 'r') as file:
#     verbs = yaml.safe_load(file)

def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

with open(resource_path('structure.yaml'), 'r') as file:
    structure = yaml.safe_load(file)
with open(resource_path('verb.yaml'), 'r') as file:
    verbs = yaml.safe_load(file)


def generate_once():
    result = draft_random(structure)
    verb = draft_random_1D(verbs["verbs"])
    return verb, result["mode"], result["temp"], result["voie"], result["personne"]

with gr.Blocks() as demo:
    gr.Markdown("## Générateur de combinaisons")
    with gr.Row():
        verb = gr.Textbox(label="Verbe", interactive=False)
    with gr.Row():
        mode = gr.Textbox(label="mode", interactive=False)
        temp = gr.Textbox(label="temp", interactive=False)
    with gr.Row():
        voie = gr.Textbox(label="voie", interactive=False)
        personne = gr.Textbox(label="personne", interactive=False)

    gen_btn = gr.Button("Générer")
    gen_btn.click(fn=generate_once, outputs=[verb, mode, temp, voie, personne])

    demo.load(fn=generate_once, outputs=[verb, mode, temp, voie, personne])

    demo.launch(inbrowser=True)

print("UI lancée. Cliquez sur 'Générer'.")