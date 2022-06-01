import json
import re

from bs4 import BeautifulSoup


def main():
    episodes = []

    with open("feed.xml") as f:
        content = f.read()
        soup = BeautifulSoup(content, features="xml")

        for item in soup.find_all("item"):
            if item.find("itunes:episodeType").text == "trailer":
                continue

            guid = item.guid.text
            title = item.title.text
            description = BeautifulSoup(item.description.text, "html.parser").text
            pub_date = item.pubDate.text
            audio_url = item.find("enclosure")["url"]
            duration = item.find("itunes:duration").text
            episode = int(item.find("itunes:episode").text)

            questions = re.findall(r"[^\?]+\?", description, re.DOTALL)

            episodes.append(
                {
                    "guid": guid,
                    "title": title,
                    "description": description,
                    "pubDate": pub_date,
                    "audioUrl": audio_url,
                    "duration": duration,
                    "episode": episode,
                    "questions": [q.strip() for q in questions],
                }
            )

        print(json.dumps(episodes, indent=2))


if __name__ == "__main__":
    main()
