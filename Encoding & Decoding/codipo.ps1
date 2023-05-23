#Ana Cecilia Lopez castillo 1996528


Clear-Host
Write-Host "Bienvenido a un ejemplo de codificacion / decodificacion base64 usando powershell" -ForegroundColor Green
Write-Host "Codificando un archivo de texto"
$inputfile ="C:\Users\anace\Downloads\secret.txt"
$fc = get-content $inputfile
$GB = [System.Text.Encoding]::UTF8.Getbytes($fc)
$etext = [System.Convert]::ToBase64String($GB)

Write-Host "El contenido del archivo CODIFICADO es:" $etext -ForegroundColor Green

Write-Host "DECODIFICANDO el texto previo:"
[System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String($etext)) | Out-File -Encoding "ASCII" "C:\Users\anace\Downloads\secret.txt"
$outfile12 = get-content "C:\Users\anace\Downloads\secret.txt"

Write-Host "El texto decodificado es el siguiente:" -ForegroundColor Green
Write-Host "DECODIFICADO:" $outfile12