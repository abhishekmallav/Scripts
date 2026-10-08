import os
import subprocess

# --- CONFIGURATION ---
# TODO: Replace these placeholders with local paths before running.
SOURCE_FOLDER = r"<SOURCE_WAV_FOLDER>"
OUTPUT_FOLDER = r"<OUTPUT_WEM_FOLDER>"
SCRIPT_PATH   = r"<SOUND2WEM_COMMAND_PATH>"
# ---------------------

def convert_tracks_one_by_one():
    # 1. Ensure the destination directory exists
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    # 2. Find all WAV tracks
    working_dir = os.path.dirname(SCRIPT_PATH)
    tracks = [f for f in os.listdir(SOURCE_FOLDER) if f.lower().endswith('.wav')]
    
    print(f"Found {len(tracks)} WAV files. Starting one-by-one conversion...")

    # 3. Execution Loop
    for index, track_name in enumerate(tracks, 1):
        full_track_path = os.path.join(SOURCE_FOLDER, track_name)
        print(f" -> [{index}/{len(tracks)}] Processing: {track_name}")

        # Construct individual arguments exactly to match the official repo specifications
        cmd_arguments = [
            "cmd.exe", "/c", SCRIPT_PATH,
            "--samplerate:48000",
            "--channels:1",
            f"--out:{OUTPUT_FOLDER}",
            full_track_path
        ]

        # Trigger clean subprocess tracking to ensure background memory isolate closures
        subprocess.run(cmd_arguments, cwd=working_dir, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print(f"\nAll files converted one-by-one! Saved here: {OUTPUT_FOLDER}")

if __name__ == "__main__":
    convert_tracks_one_by_one()
