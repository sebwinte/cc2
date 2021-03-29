<img src="http://pfuscha.cool:3000/" width="120" />

# cc2 — drag and drop it like it's hot.  
cc2 is a easy to use video encoder for Windows and MacOS. Let's say you need your ```.mp4``` video as a ```.webm``` and ```.ogv```? In a small file size, without quality loss? Just drag and drop your video into your predefined folder and see magic happens.

### How to start:
The easiest way to get started is to clone this repo and to start with installing all requirements. For this simply run:
```python
pip install -r requirements.txt
```
> Note: cc2 uses the [@FFmpeg](https://www.ffmpeg.org/) framework to compress and convert the videos. So make sure ffmpeg is already installed on your system. 

### Preferences:
Have a quick look at the ```settings.json``` and make sure to define your 'cc2_folder'. Initially its named 'your_folder_name', but you can name it as you want. You can either create a folder directly in the root directory or define an absolute path. During use, you're going to drag and drop your videos into this folder and automatically start the encoding process.

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
            "cc2_folder" : "your_folder_name/"
        }
    ]
}
```

### Custom flags:

| flags             | crf value     |
| -------------     |:-------------:|
| low               | 30%           | 
| medium            | 60%           |   
| high              | 90%           |   

| container         | codec         |
| -------------     |:-------------:|
| mp4               | libx264       | 
| webm              | libvpx-vp9    |   
| ogv               | libtheora     |   
