import json
from downloader import download_user_reels, multidownload

if __name__ == "__main__":
    settings = {}
    with open("settings.json") as settings_file:
        print("Escaneando archivo de configutación")
        settings = json.load(settings_file)
    print("Comenzando descargas 🚀")
    multidownload(
        settings["users"],
        settings["start_date"],
        settings["end_date"],
        settings["output_dir"],
        settings["limit"],
    )
    print("Finalizado con exito ✅")
