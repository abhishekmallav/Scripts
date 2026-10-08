# --- CONFIGURATION ---
# Replace with the path to the folder containing your MP3s or M4As.
# TODO: Set this to your local source folder before running.
$SourceFolder = "<SOURCE_AUDIO_FOLDER>"

# Replace with the path where you want the game-ready WAV files to go.
# TODO: Set this to your local output folder before running.
$OutputFolder = "<OUTPUT_WAV_FOLDER>"
# ---------------------

if (!(Test-Path $OutputFolder)) { New-Item -ItemType Directory -Path $OutputFolder }

Get-ChildItem -Path $SourceFolder -Include *.mp3, *.m4a, *.wav -Recurse | ForEach-Object {
    $OutputFile = Join-Path $OutputFolder "$($_.BaseName).wav"
    Write-Host "Processing: $($_.Name)" -ForegroundColor Cyan
    
    # FFmpeg flags: -ac 1 (Mono channel), -ar 48000 (48kHz sample rate)
    ffmpeg -y -i $_.FullName -ac 1 -ar 48000 $OutputFile 2>$null
}

Write-Host "Batch conversion complete! Your files are ready in: $OutputFolder" -ForegroundColor Green
