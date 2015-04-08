% FRACTIONS normalise ternary data
%   [fA, fB, fC] = FRACTIONS(A, B, C) calculates fractional values for 

function [fA, fB, fC] = fractionserror(A, B, C, D, E, F)
Total = (A+B+C);
fA = D./Total;
fB = E./Total;
fC = F./Total;

