# Problem: Find maximally sized subset of compatible (not overlapping) jobs (defined by start and end time)

# Solution: Sort jobs for endtime, take all compatible jobs
def greedy_scheduling(jobs_array):
    # sort jobs by endtime
    sorted_jobs = sorted(jobs_array, key=lambda job: job[1])      # job[1] = endtime

    # initialize
    result = []
    current_job = sorted_jobs[0]
    result.append(current_job)

    # append all jobs that are compatible
    for i in range(0,len(sorted_jobs)):
        if (current_job[1] <= sorted_jobs[i][0]):    # job[0] = starttime
            result.append(sorted_jobs[i])
            current_job = sorted_jobs[i]

    return result

jobs = [(4,5),(6,7), (1,8), (1,4), (9,10), (5,7)]

print(greedy_scheduling(jobs))
