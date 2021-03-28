<img src="http://pfuscha.cool:3000/" width="120" />

# cc2 — drag and drop it like it's hot.  
cc2 is a easy to use video encoder for Windows and MacOS. This project is aimed primarily at

### How to

```
YourVideo--low--webm--ogv.mp4
```

### Install:

```python
pip install requirements.txt
```


## FFmpeg:
FFmpeg is required

### Installing FFmpeg Windows
Windows

Download FFmpeg [@GitHub](https://github.com/FFmpeg/FFmpeg) or [@FFmpeg](https://www.ffmpeg.org/)

You can follow the Guide from Alejandro de Cabo Garcia on [Medium](https://medium.com/@alejandro.decabo/how-to-record-your-screen-using-ffmpeg-in-windows-10-silently-b82b95f24fc)

### Installing FFmpeg in OS X
The easiest way to install FFmpeg is with the help of [Homebrew](https://brew.sh/)

```
brew install ffmpeg
```


### Settings:

```
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
            "notification": 0,
            "cc2_folder" : "testordner/"
        }
    ]
}
```

Params

| param             | default       |
| -------------     |:-------------:|
| low               | 30%           | 
| medium            | 60%           |   
| high              | 90%           |   

Feel free to change 

* Notification: 0/1 Turn the notifications on or off.
* cc2_folder: Declare the folder you want to be watched over .. 



#### Troubleshooting:
Troubleshooting

