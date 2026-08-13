function save_response_plot(t, sp, pv, filename, titleText)
%SAVE_RESPONSE_PLOT Save publication-friendly response plot.
figure('Color','w');
plot(t,sp,'--','LineWidth',1.2); hold on;
plot(t,pv,'LineWidth',1.4);
grid on; xlabel('Time (s)'); ylabel('Process Value');
legend('Setpoint','PV','Location','best');
title(titleText,'Interpreter','none');
exportgraphics(gcf,filename,'Resolution',180);
end
