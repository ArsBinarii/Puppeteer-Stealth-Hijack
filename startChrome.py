import subprocess
import re
import json
import argparse

def run_chrome(user_dir):
    # Command to run Google Chrome
    command = ["/usr/bin/google-chrome", "--remote-debugging-port=9222", "--no-first-run", "--no-default-browser-check", f"--user-data-dir={user_dir}"]

    # Run the command and capture the output
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while True:
        line = process.stderr.readline()
        if not line:
            break

        # Decode the line to string and search for the session ID
        decoded_line = line.decode('utf-8')
        match = re.search(r'ws://127.0.0.1:9222/devtools/browser/([a-f0-9\-]+)', decoded_line)
        if match:
            return match.group(1)

    return None

def main():
    # Argument parser for optional userDir
    parser = argparse.ArgumentParser(description='Run Google Chrome and capture session ID.')
    parser.add_argument('--userDir', default='/home/user/Desktop/gprofile/', help='The directory for user data (defaults to /home/user/Desktop/gprofile/)')
    args = parser.parse_args()

    # Run the Chrome browser and get the session ID
    session_id = run_chrome(args.userDir)
    if session_id:
        # Write the session ID to sessionID.json
        with open('sessionID.json', 'w') as file:
            json.dump({'sessionId': session_id}, file)
        print("Session ID written to sessionID.json")
    else:
        print("Could not find the session ID.")

if __name__ == "__main__":
    main()
