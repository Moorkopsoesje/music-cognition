subject = 'e01';

midi = readmidi(strcat('data/',subject,'.mid'))

Notes=midiInfo(midi,0);
whos Notes

last_index = size(Notes,1);

c = Notes(1:last_index,5);

i=1; 
j=2;

while j~=last_index+1
    intervals(i) = c(j)-c(i);
    j=j+1;
    i=i+1;
end

filename = strcat('intervals/',subject,'.txt');

fileID = fopen(filename, 'w+');
fprintf(fileID,'%f\n', intervals);
fclose(fileID);