from datetime import datetime


def main() -> None:
    """Print current local time as YYYY-MM-DD HH:MM:SS."""
    now = datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == "__main__":
    main()
