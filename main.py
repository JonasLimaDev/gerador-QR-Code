import flet as ft
from gerador_qr_code import create_qr_code, save_image

def main(page: ft.Page):
    page.spacing = 20
    page.window.width = 400       
    page.window.height = 200
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    text_url = ft.TextField(label="Insira a URL")

    async def handle_save_file(e: ft.Event[ft.Button]):
        file_name = "qr_code.png"
        img_qr_code = create_qr_code(text_url.value)
        file_path = await ft.FilePicker().save_file(file_name=file_name,
            file_type=ft.FilePickerFileType.CUSTOM,
            allowed_extensions=["png"],
        )
        save_image(img_qr_code,file_path)

    page.add(
        ft.Row(
            controls=[
                text_url
            ]
        ),
        ft.Row(
            controls=[
                ft.Button(
                    content="Save file",
                    icon=ft.Icons.SAVE,
                    on_click=handle_save_file,
                    disabled=page.web,  # disable this button in web mode
                )
            ]
        ),
        )


ft.run(main)