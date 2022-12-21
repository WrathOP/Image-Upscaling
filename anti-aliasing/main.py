import cv2
import numpy as np
from PIL import Image


def anti_alias(image):
    # Downsample the image by a factor of 2 in each dimension
    downsampled_image = image.resize((image.width // 2, image.height // 2), resample=Image.Resampling.LANCZOS)

    # Upscale the downsampled image back to the original size using bicubic interpolation
    upscaled_image = downsampled_image.resize((image.width, image.height), resample=Image.Resampling.BICUBIC)

    return upscaled_image


# Create a video capture object
cap = cv2.VideoCapture(0)

# Set the width and height of the capture frame
width = 640
height = 480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    # Convert the frame to a PIL image
    pil_image = Image.fromarray(frame)

    # Apply the anti-aliasing method
    # aliased_image = anti_alias(pil_image)
    aliased_image = cv2.bilateralFilter(frame,15,80,80)

    # Convert the anti-aliased image back to a NumPy array
    # aliased_frame = np.array(aliased_image)

    # Concatenate the original frame and the anti-aliased frame horizontally
    # output_frame = np.hstack((frame, aliased_frame))

    # Display the output frame
    cv2.imshow('Frame', aliased_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object
cap.release()
cv2.destroyAllWindows()
