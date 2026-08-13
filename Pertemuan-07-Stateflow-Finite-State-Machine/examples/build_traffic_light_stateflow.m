clear; clc;
model='P07_TrafficLight_Stateflow';
if bdIsLoaded(model), close_system(model,0); end
new_system(model); open_system(model);
try
    add_block('sflib/Chart',[model '/TrafficLight'],'Position',[160 100 420 300]);
    rt=sfroot;
    ch=rt.find('-isa','Stateflow.Chart','Path',[model '/TrafficLight']);
    if isempty(ch), error('Chart Stateflow tidak ditemukan.'); end
    red=Stateflow.State(ch); red.Name='RED'; red.Position=[40 40 90 60]; red.LabelString='RED';
    green=Stateflow.State(ch); green.Name='GREEN'; green.Position=[190 40 90 60]; green.LabelString='GREEN';
    yellow=Stateflow.State(ch); yellow.Name='YELLOW'; yellow.Position=[115 150 90 60]; yellow.LabelString='YELLOW';
    t0=Stateflow.Transition(ch); t0.Destination=red; t0.DestinationOClock=9; t0.SourceEndPoint=[20 70]; t0.MidPoint=[30 70];
    t1=Stateflow.Transition(ch); t1.Source=red; t1.Destination=green; t1.LabelString='after(5,sec)';
    t2=Stateflow.Transition(ch); t2.Source=green; t2.Destination=yellow; t2.LabelString='after(5,sec)';
    t3=Stateflow.Transition(ch); t3.Source=yellow; t3.Destination=red; t3.LabelString='after(2,sec)';
    save_system(model,[model '.slx']);
    fprintf('Model dibuat: %s.slx\n',model);
catch ME
    close_system(model,0);
    rethrow(ME);
end
