Get-ChildItem -Path . -Filter *.m4a | ForEach-Object {
    $inputFile = $_.FullName
    $outputFile = [System.IO.Path]::ChangeExtension($inputFile, ".mp3")
    ffmpeg -i $inputFile -codec:a libmp3lame -qscale:a 2 $outputFile
}