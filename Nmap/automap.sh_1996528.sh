#!/bin/bash
#Ana Cecilia Lopez Castillo
#1996528

date

echo "| Menu |"
echo "|1° Escaneo de red |"
echo "|2° Escaneo individual |"
echo "|3° Escaneo de udp |"
echo "|4° Escaneo de script |"
echo "|5° Salida |"

read -p "Escriba la opción que prefiera (1-5)" c
case $c in
	1)read -p "Escriba la subred a escanear" red
	nmap -sn $red -oN scan_red;;
	2)read -p "Escriba la red que requiere escanear" individual
	nmap -v -A $individual -oN scan_individual;;
	3)read -p "Escriba la red en la que desea hacer un escaneo udp" udp  
	nmap -sU $udp -T5 -oN scan_udp;;
	4)read -p "Escriba el script a escanear" script
	 read -p "Proporcionenos la direccion de ip que se escaneará" ip
	nmap --script $script $ip -oN scan_script;;
	5) echo "Hasta luego (:"; exit 0;;
esac

