clear all;
subject = 'e03';

midi = readmidi(strcat('data/',subject,'.mid'))


Notes=midiInfo(midi,0);
whos Notes

last_index = size(Notes,1);

c = Notes(1:last_index,5);

for i = 1:(size(c,1)-1)
    intervals(i) = c(i+1) - c(i);
end

filename = strcat('intervals/',subject,'.txt');

fileID = fopen(filename, 'w+');
fprintf(fileID,'%f\n', intervals);
fclose(fileID);