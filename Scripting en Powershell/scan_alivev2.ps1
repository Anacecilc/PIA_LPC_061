#Nombre: Ana Cecilia Lopez castillo
#Matrícula: 1996528


#Escaneo de equipos activos en la subred
#
# Determinando gateway
$subred = (Get-NetRoute -DestinationPrefix 0.0.0.0/0).NextHop
Write-Host "== Determinando tu gateway ..."
Write-Host "Tu gateway: $subred"
#
# Determinando rango de subred
#
$rango = $subred.Substring(0,$subred.IndexOf('.') + 1 + $subred.Substring($subred.IndexOf('.') + 1).IndexOf('.') + 4)
Write-Host "== Determinando tu rango de subred ..."
echo $rango
#
## Determinando si $rango termina en "."
## En ocasiones el rango de subred no termina en punto, necesitamos forzarlo.
#
$punto = $rango.EndsWith('.')
if ( $punto -like "False" )
{
    $rango = $rango + '.' #agregamos el punto en caso de que no estuviera.
}
#
## Creamos un array con 254 numeros ( 1 a 254) y se almacenan
## en una variable que se llamara $rango_ip
#
#
## Definimos un array con puertos a escanear:
#
Write-Host "Dirección ip a escanear: " -NoNewline
$direccion = Read-Host
#
## Generamos bucle foreach para evaluar cada puerto en $portstoscan
#
foreach ( $p in $portstoscan )
{
    $TCPObject = New-Object System.Net.Sockets.TcpClient
        try{ $resultado = $TCPObject.ConnectAsync($direccion,$p).Wait($waittime)}catch{}
        if ( $resultado -eq "True")
        {
            Write-Host "Puerto abierto: " -NoNewline; Write-Host $p -ForegroundColor Green
        }

}
$rango_ip = @(1..254)
#
## Generamos bucle foreach para validar hosts activos en nuestra subred
#
Write-Output ""
Write-Host "--Subred actual:"
Write-Host "Escaneando: " -NoNewLine ; Write-Host $rango -NoNewLine; Write-Host "0/24" -ForegroundColor Red
Write-Output ""
foreach ( $r in $rango_ip ) 
{
    $actual = $rango + $r #se genera direccion ip
    $responde = Test-Connection $actual -Quiet -Count 1 # Validamos conexión contra ip en $actual
    if ( $responde -eq "True" )
    {
        Write-Output ""
        Write-Host " Host responde: " -NoNewline ; Write-Host $actual -ForegroundColor Green
    }
}
#
## Fin del script 
#