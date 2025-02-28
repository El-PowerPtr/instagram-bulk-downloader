import instaloader
from datetime import date
from concurrent.futures import ThreadPoolExecutor


def download_user_reels(
    username: str, start_date: date, end_date: date, output_dir: str
):
    # Configurar Instaloader
    downloader = instaloader.Instaloader(dirname_pattern=output_dir)

    try:
        # Obtener perfil del usuario
        profile = instaloader.Profile.from_username(downloader.context, username)

        # Obtener foto de perfil
        downloader.download_profilepic(profile)
        print(f"foto de perfil de @{username} obtenida 📸")

        # Obtener reels del usuario
        print(
            f"🔍 Buscando reels de @{username} entre {start_date.isoformat()} y {end_date.isoformat()}..."
        )

        downloaded_count = 0
        reels = [
            post
            for post in profile.get_posts()
            if post.is_video
            and post.typename == "Reel"
            and start_date <= post.date <= end_date
        ]

        # Iterar sobre los posts del usuario
        for post in profile.get_posts():
            if downloader.download_post(post, target=f"{output_dir}/{username}_reels"):
                downloaded_count += 1
            print(f"✅ Descargado: {post.date.strftime('%Y-%m-%d')} - {post.title}")

        print(
            f"\n @{username}: Descarga completada. Total de reels descargados: {downloaded_count}/{len(reels)}"
        )

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"❌ Error: El usuario @{username} no existe")
    except Exception as e:
        print(f"❌ Error inesperado: {str(e)}")


def multidownload(
    users: list[str], start_date: date, end_date: date, output_dir: str, limit: int
) -> None:
    # Hago una pool de hilos donde tiro todas las descargaws
    with ThreadPoolExecutor(max_workers=limit) as pool:
        for user in users:
            _ = pool.submit(download_user_reels, user, start_date, end_date, output_dir)

    print("Finalizado con exito ✅")
