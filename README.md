
# Bot de Discord para el YouTuber Kema-Mada


Este bot esta diseñado exclusivamente para el servidor de discord de Kema-Mada



![Logo](https://cdn.discordapp.com/attachments/967610797704511569/1090386680663511200/XD_Bot.jpg)


## Links Utiles

 - [Descargar Termux](https://play.google.com/store/apps/details?id=com.termux)
 - [Link al server de Discord](https://discord.gg/3rmVNzrRwf)
 - [Link de descarga del Bot](https://github.com/loonbac/Kema-Bot/releases)


## Preparacion y uso en Termux

Para poder usar este bot con Termux.

Abre la aplicacion Termux y escriba el siguiente codigo:
```bash
pkg update && pkg upgrade
```
Estos comandos actualizarán el paquete y el administrador de paquetes de Termux.


Escriba el siguiente comando para instalar Python:
```bash
pkg install python
```

Asegurese de que Termux tiene permisos para leer los archivos de su dispositivo con este comando:
```bash
termux-setup-storage
```

Navegue por los archivos de su dispositivo con el comando cd. Por ejemplo, si el archivo main.py esta en Descargas/Kema-Bot/main.py entonces ejecutar el siguiente comando:
```bash
cd storage/downloads/Kema-Bot
```

Una vez que estés en el directorio correcto, ejecute el siguiente comando para instalar las dependencias:
```bash
pip install -r kema.txt
```

Una vez que terminada la instalacion, puedes ejecutar el bot de Discord utilizando el siguiente comando:
```bash
python main.py
```

Y con eso deberia funcionar :D.
