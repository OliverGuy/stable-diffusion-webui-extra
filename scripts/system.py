import gradio as gr

from modules import script_callbacks, shared


def _stop():
    shared.state.server_command = "stop"


def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as ui_component:
        with gr.Row():
            stop_button = gr.Button("Shutdown WebUI")
            stop_button.style(variant="primary")
            stop_button.click(_stop)
        return [(ui_component, "System", "system_tab")]


script_callbacks.on_ui_tabs(on_ui_tabs)
