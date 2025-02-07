import json
import downloader

if __name__ == "__main__":
    settings = json.load("settings.json")
    downloader.download_user_reels(
        username=args.username,
        start_date=args.start_date,
        end_date=args.end_date,
        output_dir=args.output,
    )
