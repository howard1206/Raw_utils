# Raw_utils

packed_to_unpacked.py

This is a script for unpacking raw,each pixel 10 bits but packed. Please use python3, and please unified the input raw resolution. 

If you want to proceed a process to unpack the Qualcomm packed raw, build the unpack.pp first!!!
Use the build_unpack.sh to build the unpack executable.

Input format should be like this, the script will parse all the raw files in the folder and process them into unpacked raws.

python3 packed_to_unpacked.py /Users/howard1206/temp_raw_dump/50M_RAW_DUMP/ 8192 6144

The first parameter is the input raw folder.
The second and the third parameter are the width and the height of the input raw.

#######################################

CropPackedRaw.py
This is a script for cropping raw(unpack raw),each pixel 10bits. Please use python3, and please unified the input raw resolution.

Input format should be like this, the script will parse all the raw files in the folder and process them into cropped raws.

python3 CropPackedRaw.py /Users/howard1206/temp_raw_dump/ 4096 3072 1024 1536

The first parameter is the input raw folder.
The second and the third parameter are the width and the height of the input raw.
The fourth and the fifth parameter are the width and the height of the cropped raw.
