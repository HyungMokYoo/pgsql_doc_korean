Get-ChildItem *.html | ForEach-Object {
    $markdownPath = $_.Name -replace '.html$', '.md'
    pandoc -s $_ -o "markdown\$markdownPath"
}
