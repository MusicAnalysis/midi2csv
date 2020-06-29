import csv
import os
import pretty_midi
import sys

def process_midi(midi_file):
    print("processing " +  midi_file)
    csv_file = midi_file.replace(".mid", ".csv")
    # Load MIDI file into PrettyMIDI object
    midi_data = pretty_midi.PrettyMIDI(midi_file)
    with open(csv_file, mode='w') as output_file:
        csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["pitch", "start", "end", "duration", "velocity"])
        for instrument in midi_data.instruments:
            for note in instrument.notes:
                csv_writer.writerow([pretty_midi.note_number_to_name(note.pitch), "{:0>3.4f}".format(note.start), "{:0>3.4f}".format(note.end), "{:3.4f}".format(note.duration), note.velocity])



try:
    midi_dir = sys.argv[1]
except IndexError:
    raise SystemExit(f"Usage: {sys.argv[0]} <midi directory>")

for filename in os.listdir(midi_dir):
    if filename.endswith(".mid"):
        process_midi(os.path.join(midi_dir, filename))
