import errno
import librosa
import os
import csv

PATH = os.getcwd() + '/dataset'
PATH_RECORDINGS = PATH + '/RECOLA-Audio-recordings/'
PATH_TIMINGS = PATH + '/RECOLA-Audio_timings/'
PATH_CUTS = PATH + '/RECOLA-Audio_cuts/'


def main():
    loop_over_directory(PATH_RECORDINGS)


def loop_over_directory(path):
    directory = os.fsencode(path)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)

        if filename.endswith(".wav"):
            filename_split = os.path.splitext(filename)[0]
            loop_over_timings(filename_split)
        else:
            continue


def loop_over_timings(filename_split):
    # Open respective csv file with timings corresponding to current wav file
    with open(PATH_TIMINGS+filename_split+'.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        next(csv_reader)

        # Loop over timings in csv file, skip header
        for row in csv_reader:
            start = float(row[0])
            end = float(row[1])
            process_audio_file(filename_split, start, end)


def process_audio_file(filename_split, start, end):
    duration = end - start

    # Load wav file with current timings as delimiter
    y, sr = librosa.load(PATH_RECORDINGS + filename_split + '.wav', offset=start, duration=duration)

    export_part = make_directory(PATH_CUTS+filename_split) + '/'
    name_extension = '-' + str(start) + '-' + str(end) + '.wav'
    audio_cut_name = export_part + filename_split + name_extension

    # Save as new wav file
    librosa.output.write_wav(audio_cut_name, y, sr)


def make_directory(directory_path):
    try:
        os.makedirs(directory_path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    return directory_path


if __name__ == "__main__":
    main()
