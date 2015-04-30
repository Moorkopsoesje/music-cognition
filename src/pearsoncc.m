error_per_person = [0.051218, 0.057333, 0.095601, 0.062127, 0.060196, 0.057761, ...
    0.057082, 0.044257, 0.047692, 0.068585, 0.058687, 0.048585];

error_per_person_avg = nanmean(error_per_person);
error_per_person_std = nanstd(error_per_person);

gen_mus_exp = [5 3 3 4 2 4 3 3 4 NaN 6 6];
gen_mus_exp_avg = nanmean(gen_mus_exp);
gen_mus_exp_std = nanstd(gen_mus_exp);

nr_instr_avg_score = [7 2 0 2 1 0 2 2 0 0 8 4];
nr_instr_avg_score_avg = nanmean(nr_instr_avg_score);
nr_instr_avg_score_std = nanstd(nr_instr_avg_score);

plot(gen_mus_exp, error_per_person, 'o');
xlabel('General Music Experience');
ylabel('Average error per person');
title('Correlation between musical experience and error');
corr_err_exp = nancov(error_per_person, gen_mus_exp) / (error_per_person_std*gen_mus_exp_std);
%corr_err_exp = -0.2916

plot(nr_instr_avg_score, error_per_person, 'o');
xlabel('#Instruments * Avg Score (Skill)');
ylabel('Average error per person');
title('Correlation between instrument skill and error');
corr_err_instr = nancov(error_per_person, nr_instr_avg_score) / (error_per_person_std*nr_instr_avg_score_std);
%corr_err_instr = -0.3277