clear;
clc;
clf;

% dane parametry 
a = 1.2;    % częstość narodzin ofiar
b = .6;     % częstość umierania ofiar
c = .3;     % częstość narodzin drapieżników
d = .8;     % częstość umierania drapieżników

% funkcje obliczające ilość ofiar i drapieżników
fX = @(t,X,Y) a*X-b*X*Y;    % ofiary
fY = @(t,X,Y) c*X*Y-d*Y;    % drapieżniki

% dane do pętli
step = .001;
tend = 20;
n = ceil(tend/step);

% uprzednio stworzone listy, 
% bo jak rośnie w loopie to wyskakuje żółty wykrzyknik
X = zeros(tend/step, 1);
Y = zeros(tend/step, 1);
t = zeros(tend/step, 1);

% początkowe dane liczebności grup
X(1) = 2.0;     % początkowa liczba ofiar
Y(1) = 1.0;     % początkowa liczba drapieżników
t(1) = 0;

% pętla
for i = 1:n

    % zmiana czasu o skok
    t(i+1) = t(i) + step;
    % a(t+1) = a(t) + da/dt * dt, gdzie a należy do {x, y}
    kX = fX(t(i), X(i), Y(i));
    kY = fY(t(i), X(i), Y(i));
    % wyniki dla kolejnych skoków
    X(i+1) = X(i) + step * kX;
    Y(i+1) = Y(i) + step * kY;

end

% tworzenie wykresu
figure(1);
plot(t, X);
hold on
xlim([0, tend]);
plot(t,Y);
xlabel('czas')
ylabel('populacja')
legend('ofiary', 'drapieżniki')