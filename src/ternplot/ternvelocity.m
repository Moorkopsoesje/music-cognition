function handles = ternvelocity(A, B, C, D, E, F, varargin)

majors = 5;

if nargin < 3
    C = 1 - (A+B);
end;

[fA, fB, fC] = fractions(A, B, C);
[x, y] = terncoords(fA, fB, fC);

[fD, fE, fF] = fractions(D,E,F);
[v, w] = terncoords(fD, fE, fF);

% Make ternary axes
[hold_state, cax, next] = ternaxes(majors);

% plot data quiveroni
    q = quiver(x, y, v-x, w-y, varargin{:}, 'Autoscale','off');

if nargout > 0
    hpol = q;
end
if ~hold_state
    set(gca,'dataaspectratio',[1 1 1]), axis off; set(cax,'NextPlot',next);
end
