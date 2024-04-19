import os
import argparse
import requests
from pytube import Playlist


def is_valid_youtube_playlist_url(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.RequestException:
        return False


def download_playlist(playlist_url, path):
    playlist = Playlist(playlist_url)
    playlist._video_regex = r"\"url\":\"(/watch\?v=[\w-]*)"

    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, "video_descriptions.md"), "w", encoding="utf-8") as md_file:
        print("Downloading " + playlist.title)
        print(f"Downloading {len(playlist.video_urls)} videos from playlist...")
        for video in playlist.videos:
            # Download the video
            video.streams.get_highest_resolution().download(output_path=path)
            print(f"Downloaded {video.title}")
            # Write the title and description to the Markdown file
            md_file.write(f"## {video.title}\n\n{video.description}\n\n")
    print("✅ Done")


def main():
    parser = argparse.ArgumentParser(
        description="Download all videos from a YouTube playlist."
    )
    parser.add_argument(
        "playlist_url", type=str, help="The URL of the YouTube playlist to download."
    )
    parser.add_argument(
        "download_path", type=str, help="The path where the videos will be downloaded."
    )

    args = parser.parse_args()

    # test playlist url
    if not is_valid_youtube_playlist_url(args.playlist_url):
        print("Invalid YouTube playlist URL.")
        return
    else:
        download_playlist(args.playlist_url, args.download_path)


if __name__ == "__main__":
    main()
