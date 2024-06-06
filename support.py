#!/usr/bin/env python3
import datetime
import os
import sys

def get_work_details():
    """Prompts user for URL and notes (optional)."""
    url = input("URL: ")
    notes = input("Notes (optional): ")
    return url, notes

def append_to_markdown(url, notes):
    """Appends entry to the appropriate Markdown file."""
    today = datetime.date.today().isoformat()
    filepath = os.path.expanduser(f"~/work/support/{today}.md")

    now = datetime.datetime.now()
    formatted_time = now.strftime("%I:%M:%S %p")
    entry = f"""
{formatted_time}
-----------
Context: {url}

Notes:
{notes}

----------------------------------------

"""
    with open(filepath, "a") as file:
        file.write(entry)

def show_work_log(all_entries=False):
    """Prints the contents of the work log file(s)."""
    work_dir = os.path.expanduser("~/work/support")
    if all_entries:
        files = sorted(os.listdir(work_dir))  # Get all files and sort
    else:
        today = datetime.date.today().isoformat()
        files = [f"{today}.md"]  # Only today's file

    for filename in files:
        if filename.endswith(".md"):
            filepath = os.path.join(work_dir, filename)
            try:
                with open(filepath, "r") as file:
                    print(f"\n### {filename}:\n")
                    print(file.read())
            except FileNotFoundError:
                print(f"No work log found for {filename}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "show":
        show_work_log("all" in sys.argv)  # Show all if "all" is present
    else:
        url, notes = get_work_details()
        append_to_markdown(url, notes)
