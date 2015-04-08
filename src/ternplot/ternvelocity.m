function handles = ternvelocity(A, B, C, D, E, F, varargin)

majors = 5;

if nargin < 3
    C = 1 - (A+B);
end;

[fA, fB, fC] = fractions(A, B, C);
[x, y] = terncoords(fA, fB, fC);

[fD, fE, fF] = fractions(D,E,F);
[v, w] = terncoords(fD, fE, fF);

% Sort data points in x order
%[x, i] = sort(x);
%y = y(i);

% Sort data points in v order
%[v, i] = sort(v);
%w = w(i);



% Make ternary axes
[hold_state, cax, next] = ternaxes(majors);

%q = scatter(x,y, 'filled', 'k');
%q = scatter(v,w, 'r');

% plot data quiveroni
    q = quiver(x, y, v-x, w-y, varargin{:});

if nargout > 0
    hpol = q;
end
if ~hold_state
    set(gca,'dataaspectratio',[1 1 1]), axis off; set(cax,'NextPlot',next);
end
