# ffmpeg -i ricardo_spliff.webm -f segment -segment_time 20 -c copy -reset_timestamps 1 ricardo_spliff_%d.mp4
# ffmpeg -i midnight_0.mp4 -vf "fade=t=in:st=0:d=1,fade=t=out:st=20:d=1" -c:v libx264 midnight_0_faded.mp4
import os
from pathlib import Path

INPUT_VIDEO_FILEPATH = Path("example.mp4").absolute()
INPUT_VIDEO_FILENAME = INPUT_VIDEO_FILEPATH.stem

OUTPUT_DIR = Path("./output").absolute()

# in seconds
SEGMENT_LENGTH = 20

FADE_IN_DURATION = 1
FADE_OUT_DURATION = 1


def make_segments():
    output_path = f"{(OUTPUT_DIR / Path(INPUT_VIDEO_FILENAME)).absolute()}"
    print(output_path)
    os.makedirs(output_path, exist_ok=True)
    command = (
        f'ffmpeg -y -i "{INPUT_VIDEO_FILEPATH}" -f segment -segment_time {SEGMENT_LENGTH} '
        f'-c copy -reset_timestamps 1 "{output_path}\{INPUT_VIDEO_FILENAME}_%d.mp4"'
    )
    print(
        f"Segment length: {SEGMENT_LENGTH} seconds"
        f"\nInput file: {INPUT_VIDEO_FILEPATH}"
        f"\nOutput directory: {output_path}"
    )
    print("Running command: " + command)
    os.system(command)


def fade_segments():
    src_folder = OUTPUT_DIR / Path(f"{INPUT_VIDEO_FILENAME}/")
    dst_folder = OUTPUT_DIR / Path(f"{INPUT_VIDEO_FILENAME}/faded/")
    os.makedirs(dst_folder, exist_ok=True)

    print(
        f"\nFade in duration: {FADE_IN_DURATION} seconds"
        f"\nFade out duration: {FADE_OUT_DURATION} seconds"
    )

    for file in os.listdir(src_folder):
        file_path = os.path.join(src_folder, file)
        if os.path.isdir(file_path):
            continue
        file_name = os.path.basename(file)

        fade_in_string = f"fade=t=in:st=0:d={FADE_IN_DURATION}"
        fade_out_string = f"fade=t=out:st={SEGMENT_LENGTH-1}:d={FADE_OUT_DURATION}"
        fade_string = ""

        if FADE_IN_DURATION > 0:
            fade_string += fade_in_string

        if FADE_OUT_DURATION > 0:
            if FADE_IN_DURATION > 0:
                fade_string += ","
            fade_string += fade_out_string

        command = (
            f'ffmpeg -y -i "{file_path}" -vf '
            f'"{fade_string}" -c:v libx264 "{dst_folder / Path(f"faded_{file_name}")}"'
        )
        print("Running command: " + command)
        os.system(command)


if __name__ == "__main__":
    # make_segments()
    # move_segments()
    fade_segments()
