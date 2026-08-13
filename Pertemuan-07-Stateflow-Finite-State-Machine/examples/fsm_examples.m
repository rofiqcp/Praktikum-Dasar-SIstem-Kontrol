clear; clc; close all;
%% 1) MP3 player FSM
state="STOP";
events=["PLAY","PAUSE","PLAY","NEXT","STOP"];
fprintf('MP3 FSM\n');
for ev=events
    old=state;
    switch state
        case "STOP"
            if ev=="PLAY", state="PLAY"; end
        case "PLAY"
            if ev=="PAUSE", state="PAUSE";
            elseif ev=="STOP", state="STOP";
            elseif ev=="NEXT", state="PLAY";
            end
        case "PAUSE"
            if ev=="PLAY", state="PLAY";
            elseif ev=="STOP", state="STOP";
            end
    end
    fprintf('%s --%s--> %s\n',old,ev,state);
end

%% 2) Traffic light FSM
Tend=30; dt=0.1; t=0:dt:Tend; lamp=zeros(size(t)); % 1 red, 2 green, 3 yellow
state="RED"; entered=0;
for k=1:numel(t)
    elapsed=t(k)-entered;
    switch state
        case "RED"
            lamp(k)=1;
            if elapsed>=5, state="GREEN"; entered=t(k); end
        case "GREEN"
            lamp(k)=2;
            if elapsed>=5, state="YELLOW"; entered=t(k); end
        case "YELLOW"
            lamp(k)=3;
            if elapsed>=2, state="RED"; entered=t(k); end
    end
end
stairs(t,lamp,'LineWidth',1.5); grid on; yticks([1 2 3]); yticklabels({'RED','GREEN','YELLOW'}); xlabel('Time (s)'); ylabel('State'); title('Traffic Light FSM');

%% 3) Turning signal FSM
commands=["LEFT","OFF","RIGHT","OFF","LEFT"];
state="OFF"; fprintf('\nTurning Signal FSM\n');
for cmd=commands
    if cmd=="LEFT", state="LEFT";
    elseif cmd=="RIGHT", state="RIGHT";
    else, state="OFF";
    end
    fprintf('command=%s -> state=%s\n',cmd,state);
end
