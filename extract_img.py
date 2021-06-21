import argparse
import glob
import os
import random
import shutil

import numpy as np


def main(opt):
    random.seed(0)
    img_dir = opt.img_dir
    output_dir = opt.out_dir
    time_range = np.arange(len(glob.glob(img_dir + "/*")) - 1) + 8
    for clock in time_range:
        imgs = glob.glob(os.path.join(img_dir, str(clock)) + "/*")
        output_length = []
        max_extract_imgs = 15
        if len(imgs) < 15:
            max_extract_imgs = len(imgs)
        while len(output_length) < max_extract_imgs:
            img_num = random.randrange(len(imgs))
            os.makedirs("{}/{}".format(output_dir, clock), exist_ok=True)
            shutil.copy(imgs[img_num], "{}/{}/".format(output_dir, clock))
            output_length = glob.glob("{}/{}/*".format(output_dir, clock))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--img_dir",
        type=str,
        default="results/cam1",
        help="The directory contains the extracted images by YOLOv5",
    )
    parser.add_argument(
        "--out_dir", type=str, default="extracted_img/cam1", help="Output directory"
    )
    opt = parser.parse_args()
    main(opt=opt)
    print("DONE")
