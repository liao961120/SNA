import pickle
from math import sqrt

with open('dept_job.pkl', 'rb') as f:
    dept_job = pickle.load(f)

# Extract all jobs and all industries
jobs = set()
industries = set()
for dept in dept_job.values():
    for key in '新鮮人第一份工作', '畢業2~5年', '畢業5~10年':
        if dept[key]['做什麼工作'] is None: continue
        if dept[key]['在哪些產業'] is None: continue
        jobs.update([tup[1] for tup in dept[key]['做什麼工作']])
        industries.update([tup[1] for tup in dept[key]['在哪些產業']])


def toVec(lst_of_tup, vec):
    out_vec = [0]*len(vec)
    for tup in lst_of_tup:
        if tup[1] in vec:
            out_vec[vec.index(tup[1])] = float(tup[0])
    return out_vec

jobs_vec = sorted(list(jobs))
industr_vec = sorted(list(industries))
# add vector info to dict
for key in dept_job.keys():
    for k1 in '新鮮人第一份工作', '畢業2~5年', '畢業5~10年':
        job_tups = dept_job[key][k1]['做什麼工作']
        industr_tups = dept_job[key][k1]['在哪些產業']
        if (job_tups is None) or (industr_tups is None):
            dept_job[key][k1]['job_vec'] = None
            dept_job[key][k1]['industr_vec'] = None
            continue
        # Turn tuple into vector
        jobs_vec_temp = toVec(job_tups, jobs_vec)
        industr_vec_temp = toVec(industr_tups, industr_vec)
        # Save vector to dict
        dept_job[key][k1]['job_vec'] = jobs_vec_temp
        dept_job[key][k1]['industr_vec'] = industr_vec_temp

def eucli_dist(lst1, lst2):
    sum_of_squares = sum([(a - b)**2 for a, b in zip(lst1, lst2)])
    return sqrt(sum_of_squares)

def calc_work_stability(dept_dict):
    """
    extract `job_vec`s and `industr_vec`s from a department
    and return 4 indicies (2 for each) of job stability
    """
    # Job stability
    lst1 = dept_dict['新鮮人第一份工作']['job_vec']
    lst2 = dept_dict['畢業2~5年']['job_vec']
    lst3 = dept_dict['畢業5~10年']['job_vec']
    if (lst1 is None) or (lst2 is None) or (lst3 is None): return None
    job_stability = [eucli_dist(lst1, lst2), eucli_dist(lst2, lst3)]
    # Industry stability
    lst1 = dept_dict['新鮮人第一份工作']['industr_vec']
    lst2 = dept_dict['畢業2~5年']['industr_vec']
    lst3 = dept_dict['畢業5~10年']['industr_vec']
    if (lst1 is None) or (lst2 is None) or (lst3 is None): return None
    industr_stability = [eucli_dist(lst1, lst2), eucli_dist(lst2, lst3)]
    # Return
    return job_stability + industr_stability

with open('job_stability.csv', 'w', encoding='utf-8') as f:
    f.write('dept,job_1st-2nd,job_2nd-3rd,industr_1st-2nd,industr_2nd-3rd\n')
    for key in dept_job.keys():
        out_str = calc_work_stability(dept_job[key])
        if isinstance(out_str, list):
            out_str = ','.join([str(i) for i in out_str])
        else:
            out_str = 'NA,NA,NA,NA'
        f.write(key + ',' + out_str + '\n')
