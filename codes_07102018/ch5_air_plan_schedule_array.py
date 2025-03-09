#coding=utf-8
import time
def air_plan_schedule_array(R, t):
	hours, nowminute, sec = map(int, time.strftime("%H:%M:%S").split(':'))
	if t < (nowminute):            # 与当前时间进行比较
		return "error"
	for i in range (len(R)):       # 查看是否有冲突的降落计划
		if abs(t-R[i]) <3: 
			return "error" 
	R.append(t)                    # 将允许的降落时间点插入到计划列表中     
	return "OK"

if __name__ == "__main__": 
	R=[46, 41, 49, 56]
	t=53
	print(air_plan_schedule_array(R, t))
	print(R)