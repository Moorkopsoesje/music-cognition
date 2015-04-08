function handles = ternvelocity(A, B, C, D, E, F, varargin)

majors = 5;

if nargin < 3
    C = 1 - (A+B);
end;

[A, B, C] = fractions(A, B, C);
[x, y] = terncoords(A, B, C);

[D, E, F] = fractions(D,E,F);
[v, w] = terncoords(D, E, F);

% Sort data points in x order
%[x, i] = sort(x);
%y = y(i);

% Sort data points in v order
%[v, i] = sort(v);
%w = w(i);



% Make ternary axes
[hold_state, cax, next] = ternaxes(majors);

q = scatter(x,y);
q = scatter(v,w, 'r');
%q = scatter(q1, q2, 'g');

% plot data quiveroni
    q = quiver(x, y, v-x, w-y, varargin{:});

if nargout > 0
    hpol = q;
end
if ~hold_state
    set(gca,'dataaspectratio',[1 1 1]), axis off; set(cax,'NextPlot',next);
end
