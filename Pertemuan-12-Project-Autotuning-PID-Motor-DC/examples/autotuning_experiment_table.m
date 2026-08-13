methods={'Sinestream';'Superposition';'PRBS'}; modes={'Position';'Speed'};
rows={};
for i=1:numel(modes)
 for j=1:numel(methods)
  rows(end+1,:)={modes{i},methods{j},NaN,NaN,NaN,NaN,NaN,NaN}; %#ok<SAGROW>
 end
end
T=cell2table(rows,'VariableNames',{'Mode','Method','Kp','Ki','Kd','RiseTime','SettlingTime','OvershootPct'});
disp(T); writetable(T,'autotuning_results.csv');
