
Traffic_light_kr - v1 
==============================

The dataset includes 302 images.
Red-green-yellow-left are annotated in YOLOv8 format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 800x800 (Stretch)

The following augmentation was applied to create 3 versions of each source image:
* 50% probability of vertical flip
* Random rotation of between -7 and +7 degrees
* Random shear of between -10° to +10° horizontally and -10° to +10° vertically


