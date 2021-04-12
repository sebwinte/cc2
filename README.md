<img src="http://pfuscha.cool:3000/" width="120"/>

cc2 — drag and drop it like it's hot.
-------------------------------------
cc2 is a easy to use video encoder for Windows and MacOS. Let's say you need your ```.mp4``` video as a ```.webm``` and ```.ogv```? In a small file size, without quality loss? Just drag and drop your video into your predefined folder and see magic happens.


Installation and requirements
-----------------------------
Clone this repo and start installing all requirements. For this simply run:
```python
pip install -r requirements.txt
```
> Note: cc2 uses the [@FFmpeg](https://www.ffmpeg.org/) framework to compress and convert the videos. So make sure ffmpeg is already installed on your system. 

Quickstart
----------
Open the ```cc2``` folder in your terminal and run:
```
python main.py
```

<img src="https://raw.githubusercontent.com/sebwinte/cc2/main/doc/cc2.gif" />

Add custom 'cc2-flags' to your video and drag it into your 'cc2-folder'. By default this folder is named 'your_folder_name':
```
my-cool-video--low--webm--ogv.mp4
```
After the process has finished, your .mp4 video is now available in a .webm and .ovg format with a low compression rate. Choose at least one container flag in order to start the process. The default compression rate then will be medium.

cc2-flags
---------
As shown in the quickstart example, cc2 works with custom flags which can be easily added to the filename. Each flag starts with a double hyphen. :

| container         | flag              |
| :------------     | :------------     |
| mp4               | --mp4             | 
| webm              | --webm            |   
| ogv               | --ogv             |   

| compression       | flag              |        
| :------------     | :------------     |
| low               | --low             | 
| medium            | --medium          |   
| high              | --high            |   

Preferences
-----------
Have a quick look at the ```settings.json``` and define your 'cc2_folder'. Initially its named 'your_folder_name', but you can name it as you want. You can either create a folder directly in the root directory like ```your_folder_name``` or you can define an absolute path like ```C:\\Users\\Default\\Documents\\your_folder_name\\```. During use, you're going to drag and drop your videos into this folder and automatically start the encoding process.

```json
{   
    "compression":[
        {
            "low":30,
            "medium": 60,
            "high": 90
        }
    ],
    "settings":[
        {
            "notification": true,
            "cc2_folder" : "C:\\Users\\Default\\Documents\\your_folder_name\\" 
        }
    ]
}
```
Supported container formats and codecs
--------------------------------------
cc2 is focusing on container formats mostly used for the web.  

| container         | codec         |
| :------------     |:------------  |
| mp4               | libx264       | 
| webm              | libvpx-vp9    |   
| ogv               | libtheora     |   

Autostart cc2
-------------
For a better experience during the use of cc2, you can easily create  a ```.bat``` file for Windows or a ```.command``` file if you're running cc2 on a Mac. By using this method, cc2 automatically starts after your system is booted.
#### Windows (.bat):
Save this file and move it into the Windows 'startup' folder. 
```bat
"C:\Users\your\path\to\python.exe" "C:\Users\your\path\to\cc2\main.py"
pause
```
#### MacOS (.command):
Save this file and make it executable with ```chmod +x filename.command```. Afterwards go to 'System Preferences' -> 'Users & Groups' -> 'Login Items' and add your file to the list.
```command
#!/bin/bash
python /Users/your/path/to/cc2/main.py
```

Troubleshooting
---------------
<details>
<summary>"Error directory not found"</summary>
<p>Make sure your 'cc2_folder' exists. Double check the path in the settings.json</p>  
</details>
<details>
<summary>"ImportError: No module named utils.helper"</summary>
<p>Python has to be at least version 3.6</p>  
</details>
