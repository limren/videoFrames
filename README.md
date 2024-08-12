# videoFrames

My program videoFrames is a small program very useful for extracting frames from videos - a common use would be getting frames from a folder containing a lot of videos to create datasets.

Giving an offset is very important, skipping frames will lower overfitting if you're using frames in a training of a ML model.

## Execution

```py
py main.py sourcePath destPath offset
``` 

where sourcePath could be either a file or a directory containing files - non-readable frames or non-readable capture (such as .txt files for instance) will be ignored.

## About offset

Keep in mind that :

- 30FPS videos:
An offset of 30 will skip frames second per second.

- 60FPS videos:
An offset of 60 will skip frames second per second

Currently, I'm working with 60FPS videos and giving an offset of 20 frames per image read, works well to build a dataset that doesn't cause overfitting due to non-generalization.