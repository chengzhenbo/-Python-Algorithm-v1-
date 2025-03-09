#coding=utf-8
def get_max_intervalschdeule(joblist):
    job_schedule = []
    num_jobs = len(joblist)
    joblist.sort(key=lambda x: x[2])  # 按照结束时间对所有的job排序
    for n in range(num_jobs):
        if not job_schedule:
            job_schedule.append(joblist[n])
        else:
            # job(n)是否与job_schedule中的jobs相容
            if job_schedule[-1][2] <= joblist[n][1]:  
                job_schedule.append(joblist[n])
    return job_schedule

if __name__ == '__main__':
    joblist = [['e', 8, 10], ['b', 2, 5], ['c', 4, 7], ['a', 1, 3], ['d', 6, 9]]
    print(get_max_intervalschdeule(joblist))