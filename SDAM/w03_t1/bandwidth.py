mb = 1000000
max = 1000 * mb
concurrent_user = 200
applicationA = 200000
applicationB = 100000
app_new = 350000
usage_old = concurrent_user * (applicationA + applicationB)
available = max - usage_old
total = applicationA + applicationB + app_new
available_new = max - concurrent_user * total
print("Network capacity: ", max, "\n", "Current usage: ", usage_old, "\n", "Current availability: ",available, "\n", "New applications requirements: ", total, "\n", "New available bandwidth: ", available_new / mb)