#Ana Cecilia Lopez castillo
#1996528


$tare= New-ScheduledTaskAction -Execute 'send_sysinfo.ps1' -WorkingDirectory  "C:\Users\anace\Desktop\pia\tareas"

$trigger= New-ScheduledTaskTrigger -Once -At 1:08pm



Register-ScheduledTask SENDDSYSINFO1 -Trigger $trigger -Action $tarea -TaskPath "Mis_Tareas" -Description "Envio de informacion del sistema"