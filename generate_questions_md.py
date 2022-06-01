import datetime
import json
from email.utils import parsedate_to_datetime


def main():
    with open("episodes.json") as f:
        episodes = json.load(f)

    output = "# Dear Hank & John Questions!\n\n"

    for episode in episodes:
        dt = parsedate_to_datetime(episode["pubDate"])
        output += f"## [{episode['title']}]({episode['audioUrl']})\n"
        output += f"{dt.strftime('%B %-d, %Y')} — {episode['duration']}\n\n"

        if len(episode["questions"]) > 0:
            for question in episode["questions"]:
                output += f"- {question}\n"
        else:
            output += "*Question detection failed! :( Here's the description...*\n\n"
            output += episode["description"]

    ts = (
        datetime.datetime.utcnow()
        .replace(tzinfo=datetime.timezone.utc, microsecond=0)
        .isoformat()
    )
    output += (
        f"\n\n---\nGenerated on {ts}. Please let me know if you find any problems."
    )
    print(output)


if __name__ == "__main__":
    main()
